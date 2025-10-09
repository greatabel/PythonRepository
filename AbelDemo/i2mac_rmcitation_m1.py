# coding=utf-8
# https://www.jianshu.com/p/ab7d1ebba3bf
# mac默认/usr/bin/python 是 python2.7，最好不要改变
# 另外注意服务是： 没有输入，具体看图：https://www.jianshu.com/p/0e9e5c2cb2a2

import sys
import re


def split_uppercase(string):
    """将大写字母之前的字符串拆分开"""
    result = ""
    for i in range(len(string)):
        # 如果当前字符为大写字母且不是第一个字符，则在字符之前添加空格
        if string[i].isupper() and i != 0:
            result += " "
        result += string[i]
    return result


def process_english_string(content):
    """查找并处理英文字符串"""
    pattern = r"[A-Za-z]+"
    english_strings = re.findall(pattern, content)
    for string in english_strings:
        processed_string = split_uppercase(string)
        content = content.replace(string, processed_string)
    return content


def smart_merge_lines(content):
    # 按行分割
    lines = content.split('\n')
    merged_lines = []
    i = 0
    zh_punct = "。！？；：、）》”’"
    en_punct = ".!?;:,)]\"'"
    while i < len(lines):
        line = lines[i].rstrip()
        if not line:
            # 空行保留
            merged_lines.append('')
            i += 1
            continue
        # 判断：如果下一行存在且不是空行，而且本行不是标点结尾
        while (i + 1 < len(lines)
               and lines[i + 1].strip() != ''
               and (not line or line[-1] not in zh_punct + en_punct)):
            # 合并下一行
            next_line = lines[i + 1].lstrip()
            line += next_line
            i += 1
        merged_lines.append(line)
        i += 1
    # 合并为字符串
    return '\n'.join(merged_lines)


def clean_content(content):
    content = smart_merge_lines(content)

    # 如果内容中存在 "摘录来自"，则移除该字符串后面的所有内容
    if "摘录来自" in content:
        content = content[: content.index("摘录来自")].strip()

    # 删除类似 [48] 这种引用格式的内容
    content = re.sub(r"\[\d+\]", "", content).strip()

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

    # 定义广义“中文/汉字相关”字符集合：含部首、扩展区、兼容等
    HAN_CLASS = r"\u2E80-\u2FFF\u3400-\u9FFF\uF900-\uFAFF"
    # 常见中日韩标点符号（含特殊符号®），用于去除与汉字之间的空格
    punct_chars = "，。！？；：、（）《》“”‘’—…～·「」『』〈〉〔〕【】®："
    PUNCT_CLASS = re.escape(punct_chars)

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

    # 特别处理中文句号后的空格
    content = re.sub(r"(?<=。)[ \t\u00A0\u3000]+", "", content)

    # 检查最后一个 "《" 后面是否有对应的 "》"，如果没有就在内容末尾添加 "》"
    last_open_quote_index = content.rfind("《")
    if last_open_quote_index != -1 and content[last_open_quote_index:].count("》") == 0:
        content += "》"

    # 英文字符串处理（大写内部分割）
    content = process_english_string(content)

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