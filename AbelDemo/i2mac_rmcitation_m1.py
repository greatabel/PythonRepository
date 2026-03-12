# coding=utf-8
import sys
import re
import subprocess


def _read_all_stdin():
    try:
        data = sys.stdin.read()
        return data if data is not None else ""
    except Exception:
        return ""


def _read_clipboard_text():
    """
    在 macOS 用 pbpaste 拿纯文本。若失败则返回空字符串。
    """
    try:
        out = subprocess.check_output(["pbpaste", "-Prefer", "txt"])
        # 尝试按 UTF-8 解码，失败则退回系统默认
        try:
            return out.decode("utf-8")
        except Exception:
            return out.decode(errors="ignore")
    except Exception:
        return ""


def _normalize_newlines_and_spaces(text):
    """
    标准化换行与常见不可见空白：
    - CRLF/CR -> \n
    - Unicode 行/段分隔符 U+2028/U+2029 -> \n
    - 去掉 BOM/零宽空格 U+FEFF/U+200B/U+200C/U+200D
    - 将 NBSP(U+00A0)、全角空格(U+3000) 统一为空格
    """
    if not text:
        return ""
    # 换行统一
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = text.replace("\u2028", "\n").replace("\u2029", "\n")
    # 去掉不可见字符
    text = text.replace("\ufeff", "").replace("\u200b", "").replace("\u200c", "").replace("\u200d", "")
    # 统一空白
    text = text.replace("\u00A0", " ").replace("\u3000", " ")
    return text


def split_uppercase_camel(text):
    # 仅在小写 -> 大写边界插空格（CamelCase），不拆 ALL-CAPS（DNA）
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', text)


def process_english_string(content):
    # 仅进行 CamelCase 的断开
    return split_uppercase_camel(content)


def merge_pdf_split_letters(content):
    # 合并 PDF 拆开的英文：T e i c h m i l l e r / T U T / A B C
    pattern = re.compile(r'(?<![A-Za-z])(?:[A-Za-z]\s){2,}[A-Za-z](?![A-Za-z])')
    return pattern.sub(lambda m: m.group(0).replace(' ', ''), content)


def smart_merge_lines(content):
    # 智能合并断行：上一行不是终止类标点才合并
    zh_punct = "。！？；：、）》\u201d\u2019"
    en_punct = ".!?;:,)]\"\u2019"

    # 保守做法：逐行合并
    lines = content.splitlines()
    new_lines = []
    for i, line in enumerate(lines):
        line = line.rstrip()
        if i > 0 and new_lines:
            prev_line = new_lines[-1]
            if prev_line and prev_line[-1] not in zh_punct + en_punct:
                new_lines[-1] = prev_line + line.lstrip()
                continue
        new_lines.append(line)
    return "\n".join(new_lines)


def drop_noise_lines(content):
    # 删除噪音行：独立数字行、由横线/破折号/下划线/波浪线/点构成的分隔线
    noise_rule = re.compile(r'^\s*(?:\d+|[—\-–_~·\.]{3,})\s*$', re.U)
    lines = content.splitlines()
    kept = [ln for ln in lines if not noise_rule.match(ln)]
    return "\n".join(kept)


def repair_missing_book_quote_open(content):
    """
    容错修复：iBooks 复制时 "《 紧邻会丢失 《，导致出现孤立的 》。

    策略：用栈找出未配对的 》，然后从 》 往前回溯连续汉字，
    只有在回溯到"非汉字边界"（标点、引号、空格、数字、英文等）
    或字符串开头时才插入 《。
    如果从 》 往前全是汉字一直到开头，也在开头插入 《。
    """
    if content.count("\u300b") <= content.count("\u300a"):
        return content

    HAN_RE = re.compile('[\u2E80-\u2FFF\u3400-\u9FFF\uF900-\uFAFF]')

    chars = list(content)
    stack = []
    unmatched_close = []
    for i, ch in enumerate(chars):
        if ch == "\u300a":  # 《
            stack.append(i)
        elif ch == "\u300b":  # 》
            if stack:
                stack.pop()
            else:
                unmatched_close.append(i)

    if not unmatched_close:
        return content

    for close_idx in sorted(unmatched_close, reverse=True):
        # 从 》 前一个字符往前回溯连续汉字
        insert_idx = close_idx
        found_boundary = False
        for j in range(close_idx - 1, -1, -1):
            if HAN_RE.match(chars[j]):
                insert_idx = j
            else:
                # 遇到非汉字 = 找到了边界，在它后面插入 《
                found_boundary = True
                break

        # 只有找到了明确的非汉字边界，或者回溯到了字符串开头才插入
        if insert_idx < close_idx:
            chars.insert(insert_idx, "\u300a")

    return "".join(chars)


def clean_content(content):
    # 标准化输入
    content = _normalize_newlines_and_spaces(content)

    # 截断 "摘录来自" 之后
    if "摘录来自" in content:
        content = content[: content.index("摘录来自")].strip()

    # 先删除噪音行（独立数字、分隔线），避免后续被合并到有效文本里
    content = drop_noise_lines(content)

    # 再做 PDF 断行的智能合并
    content = smart_merge_lines(content)

    # 删除 [48] 类引用
    content = re.sub(r"\[\d+\]", "", content).strip()

    # 引号/括号紧贴处边界空格
    content = re.sub(r'([\u201c\uff08])\s+', r'\1', content)
    content = re.sub(r'\s+([\u201d\uff09])', r'\1', content)

    # 合并 PDF 拆开的英文
    content = merge_pdf_split_letters(content)

    # 类别定义
    HAN_CLASS = r"\u2E80-\u2FFF\u3400-\u9FFF\uF900-\uFAFF"
    punct_chars = "，。！？；：、（）《》\u201c\u201d\u2018\u2019—…～·「」『』〈〉〔〕【】®："
    PUNCT_CLASS = re.escape(punct_chars)

    # ALL-CAPS 英文缩写 与 中文之间取消空格：TUT 理论 -> TUT理论
    content = re.sub(fr'([A-Z]{{2,}})[ \t\u00A0\u3000]+(?=[{HAN_CLASS}])', r'\1', content)

    # CamelCase 边界断开
    content = process_english_string(content)

    # 起止 """" 修正
    if content.startswith("\u201c"):
        next_end_quote_index = content[1:].find("\u201d") if "\u201d" in content[1:] else -1
        next_start_quote_index = content[1:].find("\u201c") if "\u201c" in content[1:] else -1
        if next_start_quote_index != -1 and next_end_quote_index > next_start_quote_index:
            content = content[1:]
    if content.endswith("\u201d"):
        last_start_quote_index = content[:-1].rfind("\u201c") if "\u201c" in content[:-1] else -1
        last_end_quote_index = content[:-1].rfind("\u201d") if "\u201d" in content[:-1] else -1
        if (
            last_start_quote_index != -1
            and last_end_quote_index != -1
            and content.count("\u201c", 0, last_start_quote_index + 1)
            <= content.count("\u201d", 0, last_end_quote_index + 1)
        ):
            content = content[:-1]
    if content.startswith("\u201c") and content.endswith("\u201d") and content.count("\u201c") == content.count("\u201d"):
        content = content[1:-1]

    # 逐行去掉行首行尾空白
    content = re.sub(r"^[ \t\u3000]+|[ \t\u3000]+$", "", content, flags=re.M)

    # 中文字符之间空格
    content = re.sub(fr"(?<=[{HAN_CLASS}])[ \t\u00A0\u3000]+(?=[{HAN_CLASS}])", "", content)

    # 数字序列、数字与中文之间空格
    content = re.sub(r"(?<=\d)[ \t\u00A0\u3000]+(?=\d)", "", content)
    content = re.sub(fr"(?<=\d)[ \t\u00A0\u3000]+(?=[{HAN_CLASS}])", "", content)
    content = re.sub(fr"(?<=[{HAN_CLASS}])[ \t\u00A0\u3000]+(?=\d)", "", content)

    # 中文字符与中文标点之间空格（双向）
    content = re.sub(fr"(?<=[{HAN_CLASS}])[ \t\u00A0\u3000]+(?=[{PUNCT_CLASS}])", "", content)
    content = re.sub(fr"(?<=[{PUNCT_CLASS}])[ \t\u00A0\u3000]+(?=[{HAN_CLASS}])", "", content)

    # 标点-标点之间空格（如 "） ，"、"" 。"）
    content = re.sub(fr"(?<=[{PUNCT_CLASS}])[ \t\u00A0\u3000]+(?=[{PUNCT_CLASS}])", "", content)

    # 英文标点（ASCII .!?;:,）前的空格去掉："信息 ." -> "信息."
    content = re.sub(r"(?<=\S)[ \t\u00A0\u3000]+(?=[\.\!\?\:\;\,])", "", content)

    # 破折号与书名号之间保持一个空格：—《 -> — 《
    content = content.replace("—《", "— 《")

    # 中文句号后的空格
    content = re.sub(r"(?<=。)[ \t\u00A0\u3000]+", "", content)

    # 容错：补全 iBooks 丢失的 《
    content = repair_missing_book_quote_open(content)

    # 补全最后一个 "《" 无 "》"
    last_open_book = content.rfind("《")
    if last_open_book != -1 and content[last_open_book:].count("》") == 0:
        content += "》"

    # 补全最后一个 "「" 无 "」"
    last_open_corner = content.rfind("「")
    if last_open_corner != -1 and content[last_open_corner:].count("」") == 0:
        content += "」"

    return content


def clean_content_from_input():
    # 1) 先尝试从 stdin 读取全部输入
    content = _read_all_stdin()

    # 2) 如果 stdin 为空，再回退到 macOS 剪贴板（纯文本）
    if not content.strip() and sys.platform == "darwin":
        content = _read_clipboard_text()

    # 3) 仍然为空就直接返回空
    if not content.strip():
        print("")
        return

    print(clean_content(content))


if __name__ == "__main__":
    clean_content_from_input()