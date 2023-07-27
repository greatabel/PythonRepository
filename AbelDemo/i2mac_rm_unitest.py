import unittest
import difflib
from colorama import Fore, Back, Style, init
from i2mac_rmcitation_m1 import clean_content


class TestCleanContent(unittest.TestCase):
    def color_diff(self, diff):
        """为差异部分添加颜色"""
        for line in diff:
            if line.startswith('-'):
                yield Fore.RED + line[2:] + Style.RESET_ALL
            elif line.startswith('+'):
                yield Fore.GREEN + line[2:] + Style.RESET_ALL
            else:
                yield line[2:]

    def assertEqualWithDiff(self, first, second):
        """检查两个字符串是否相等，并在不相等的情况下显示有颜色标记的差异"""
        if first != second:
            diff = difflib.ndiff(first, second)
            raise AssertionError("Values are not equal:\n" + "".join(self.color_diff(diff)))
        self.assertEqual(first, second)

    def test_normal_content(self):
        content = '“它的拉丁语是“lex parsimoniae”，即节约律。在英文中人们常常用格言“如无必要，勿增实体”（Do not multiply entities beyond necessity）来表达。”\
\
摘录来自\
直觉泵和其他思考工具\
【美】丹尼尔·丹尼特（Daniel C. Dennett）\
https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewBook?id=0\
此材料可能受版权保护。'

        expected_result = '它的拉丁语是“lexparsimoniae”，即节约律。在英文中人们常常用格言“如无必要，勿增实体”（Donotmultiplyentitiesbeyondnecessity）来表达。'
        self.assertEqualWithDiff(clean_content(content), expected_result)


    def test_content_with_extras(self):
        content = '“史特金定律表达得更粗俗一些：“任何事物当中的百分之九十都是垃圾（crap）。”\
\
摘录来自\
直觉泵和其他思考工具\
【美】丹尼尔·丹尼特（Daniel C. Dennett）\
https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewBook?id=0\
此材料可能受版权保护。'
        expected_result = '史特金定律表达得更粗俗一些：“任何事物当中的百分之九十都是垃圾（crap）。”'
        self.assertEqualWithDiff(clean_content(content), expected_result)

if __name__ == '__main__':
    unittest.main()
