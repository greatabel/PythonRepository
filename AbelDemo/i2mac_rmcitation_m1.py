# coding=utf-8
# https://www.jianshu.com/p/ab7d1ebba3bf
# mac默认/usr/bin/python 是 python2.7，最好不要改变
# 另外注意服务是： 没有输入，具体看图：https://www.jianshu.com/p/0e9e5c2cb2a2

import sys
import re


def split_uppercase_camel(text):
    """
    仅在小写 -> 大写的边界插入空格，用于 CamelCase。
    不会拆分 ALL-CAPS（如 DNA）。
    例如: DoNot -> Do Not；TeXLive -> TeX Live；DNA 保持不变
    """
    return re.sub(r'(?<=[a-z])(?=[A-Z])', ' ', text)


def process_english_string(content):
    """
    安全版英文处理：仅进行 CamelCase 的断开，不处理 ALL-CAPS 和正常英文短语之间的空格
    """
    return split_uppercase_camel(content)


def merge_pdf_split_letters(content):
    """
    合并 PDF 拆开的英文：形如 'T e i c h m i l l e r' / 'T U T' / 'A B C'
    限定：前后不是英文字母，且整个串是由“单字母 + 空格”重复组成，长度>=3个字母
    避免影响正常英文短语
    """
    pattern = re.compile(r'(?<![A-Za-z])(?:[A-Za-z]\s){2,}[A-Za-z](?![A-Za-z])')
    return pattern.sub(lambda m: m.group(0).replace(' ', ''), content)


def smart_merge_lines(content):
    """
    合并 PDF 断行：仅当上一行不以终止类标点结束时合并到同一行；
    段落空行保留；避免破坏诗歌/标题等
    """
    zh_punct = "。！？；：、）》”’"
    en_punct = ".!?;:,)]\"'"

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


def clean_content(content):
    # 如果内容中存在 "摘录来自"，则移除该字符串后面的所有内容
    if "摘录来自" in content:
        content = content[: content.index("摘录来自")].strip()

    # 先做 PDF 断行的智能合并
    content = smart_merge_lines(content)

    # 删除类似 [48] 这种引用格式的内容
    content = re.sub(r"\[\d+\]", "", content).strip()

    # 统一修剪引号/括号紧贴处的空白（仅在边界，不影响内部单词间空格）
    # 开引号/开括号后面的多余空格
    content = re.sub(r'([“（])\s+', r'\1', content)
    # 闭引号/闭括号前面的多余空格
    content = re.sub(r'\s+([”）])', r'\1', content)

    # 合并 PDF 拆开的英文单词或缩写
    content = merge_pdf_split_letters(content)

    # 定义广义“中文/汉字相关”字符集合
    HAN_CLASS = r"\u2E80-\u2FFF\u3400-\u9FFF\uF900-\uFAFF"
    # 常见中日韩标点符号（含特殊符号®）
    punct_chars = "，。！？；：、（）《》“”‘’—…～·「」『』〈〉〔〕【】®："
    PUNCT_CLASS = re.escape(punct_chars)

    # ALL-CAPS 缩写 与 中文之间取消空格：TUT 理论 -> TUT理论；ABC 猜想 -> ABC猜想
    content = re.sub(fr'([A-Z]{{2,}})[ \t\u00A0\u3000]+(?=[{HAN_CLASS}])', r'\1', content)

    # 仅 CamelCase 边界断开（不影响 ALL-CAPS 和正常英文短语）
    content = process_english_string(content)

    # 如果内容以 "“" 开始，并且在后面的第一个 "”" 之前还有其他 "“"，则删除第一个 "“"
    if content.startswith("“"):
        next_end_quote_index = content[1:].find("”") if "”" in content[1:] else -1
        next_start_quote_index = content[1:].find("“") if "“" in content[1:] else -1
        if (
            next_start_quote_index != -1
            and next_end_quote_index > next_start_quote_index
        ):
            content = content[1:]

    # 如果内容以 "”" 结束，并且在最后的 "”" 之前还有 "“"，则删除最后的 "”"
    if content.endswith("”"):
        last_start_quote_index = content[:-1].rfind("“") if "“" in content[:-1] else -1
        last_end_quote_index = content[:-1].rfind("”") if "”" in content[:-1] else -1
        if (
            last_start_quote_index != -1
            and last_end_quote_index != -1
            and content.count("“", 0, last_start_quote_index + 1)
            <= content.count("”", 0, last_end_quote_index + 1)
        ):
            content = content[:-1]

    # 如果 "“" 和 "”" 的数量匹配，并且刚好出现在开始和结束，也删除它们
    if (
        content.startswith("“")
        and content.endswith("”")
        and content.count("“") == content.count("”")
    ):
        content = content[1:-1]

    # 逐行去掉行首行尾空白
    content = re.sub(r"^[ \t\u3000]+|[ \t\u3000]+$", "", content, flags=re.M)

    # 去掉连续中文关联字符之间的空格（包括康熙部首等 PDF 伪字形）
    content = re.sub(
        fr"(?<=[{HAN_CLASS}])[ \t\u00A0\u3000]+(?=[{HAN_CLASS}])", "", content
    )

    # 数字序列中的空格
    content = re.sub(r"(?<=\d)[ \t\u00A0\u3000]+(?=\d)", "", content)
    # 数字与中文关联字符之间的空格（双向）
    content = re.sub(fr"(?<=\d)[ \t\u00A0\u3000]+(?=[{HAN_CLASS}])", "", content)
    content = re.sub(fr"(?<=[{HAN_CLASS}])[ \t\u00A0\u3000]+(?=\d)", "", content)

    # 中文关联字符与常见中文标点之间的空格（双向）
    content = re.sub(fr"(?<=[{HAN_CLASS}])[ \t\u00A0\u3000]+(?=[{PUNCT_CLASS}])", "", content)
    content = re.sub(fr"(?<=[{PUNCT_CLASS}])[ \t\u00A0\u3000]+(?=[{HAN_CLASS}])", "", content)

    # 新增：常见中文标点与中文标点之间的空格（如 "） ，"、"” 。"）
    content = re.sub(fr"(?<=[{PUNCT_CLASS}])[ \t\u00A0\u3000]+(?=[{PUNCT_CLASS}])", "", content)

    # 新增：英文标点（ASCII .!?;:,）前的空格去掉；例如 "信息 ." -> "信息."
    content = re.sub(r"(?<=\S)[ \t\u00A0\u3000]+(?=[\.\!\?\:\;\,])", "", content)

    # 新增：破折号与书名号之间保持一个空格：—《 -> — 《
    content = content.replace("—《", "— 《")

    # 特别处理中文句号后的空格
    content = re.sub(r"(?<=。)[ \t\u00A0\u3000]+", "", content)

    # 检查最后一个 "《" 后面是否有对应的 "》"，如果没有就在内容末尾添加 "》"
    last_open_quote_index = content.rfind("《")
    if last_open_quote_index != -1 and content[last_open_quote_index:].count("》") == 0:
        content += "》"

    return content


def clean_content_from_input():
    content = ""
    for _ in range(10):
        t = sys.stdin.readline()
        content += t
        if "摘录来自" in content:
            break
    print(clean_content(content))


if __name__ == "__main__":
    clean_content_from_input()