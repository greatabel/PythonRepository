# coding=utf-8
# https://www.jianshu.com/p/ab7d1ebba3bf
# mac默认/usr/bin/python 是 python2.7，最好不要改变
# 另外注意服务是： 没有输入，具体看图：https://www.jianshu.com/p/0e9e5c2cb2a2

# 使用捷径app

import sys
import re

def split_uppercase(string):
    """将大写字母之前的字符串拆分开"""
    result = ''
    for i in range(len(string)):
        # 如果当前字符为大写字母且不是第一个字符，则在字符之前添加空格
        if string[i].isupper() and i != 0:
            result += ' '
        result += string[i]
    return result

def process_english_string(content):
    """查找并处理英文字符串"""
    # 匹配所有英文字符串的正则表达式
    pattern = r'[A-Za-z]+'

    # 使用 re.findall 找到所有的英文字符串
    english_strings = re.findall(pattern, content)

    # 对每个英文字符串进行处理
    for string in english_strings:
        # 使用 split_uppercase 函数处理字符串
        processed_string = split_uppercase(string)

        # 在原始内容中用处理后的字符串替换原字符串
        content = content.replace(string, processed_string)

    return content

def clean_content(content):
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
        # 需要确保在最后的引号之前，"“"（开放引号）的数量多于"”"（关闭引号）
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

    # 去掉中文句子中字之间的空格，但保留数字标号后的空格，例如：1. 或 1 以及中文字符与非中文字符之间的空格
    # content = re.sub(r"(?<=[^\d\W])\s+(?=[^\d\W])", "", content)
    content = re.sub(r"(?<=[\u4e00-\u9fff])[ \t]+(?=[\u4e00-\u9fff])", "", content)


    # pdf 处理
    # 新增的逻辑: 合并数字序列中的空格
    content = re.sub(r'(?<=\d)\s+(?=\d)', '', content)
    # 去除数字后的空格（如果数字后是中文字符）
    content = re.sub(r'(?<=\d)\s+(?=[\u4e00-\u9fff])', '', content)
    # 去除数字前的空格（如果数字前是中文字符）
    content = re.sub(r'(?<=[\u4e00-\u9fff])\s+(?=\d)', '', content)

    # 新增的逻辑: 去除连续中文字符之间的空格
    content = re.sub(r'(?<=[\u4e00-\u9fff])[ \t]+(?=[\u4e00-\u9fff])', '', content)

    # 新增的逻辑: 去除中文字符与中文标点符号之间的空格
    content = re.sub(r'(?<=[\u4e00-\u9fff])\s+(?=[，。！？；：])', '', content)
    content = re.sub(r'(?<=[，。！？；：])\s+(?=[\u4e00-\u9fff])', '', content)
    # 新增的逻辑: 特别处理中文句号后的空格
    content = re.sub(r'(?<=。)\s+', '', content)


    # 检查最后一个 "《" 后面是否有对应的 "》"，如果没有就在内容末尾添加 "》"
    last_open_quote_index = content.rfind("《")
    if last_open_quote_index != -1 and content[last_open_quote_index:].count("》") == 0:
        content += "》"

    content = process_english_string(content)

    return content


def clean_content_from_input():
    content = ""

    for i in range(10):
        t = sys.stdin.readline()
        content += t
        if "摘录来自" in content:
            break

    print(clean_content(content))


if __name__ == "__main__":
    clean_content_from_input()
