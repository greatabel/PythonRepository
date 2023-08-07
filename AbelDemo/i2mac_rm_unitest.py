import unittest
import difflib
from colorama import Fore, Back, Style, init
from i2mac_rmcitation_m1 import clean_content


class TestCleanContent(unittest.TestCase):
    def color_diff(self, expected, actual):
        """为差异部分添加颜色"""
        diff = difflib.ndiff(expected, actual)
        diff_text = ''.join(diff)

        i = 0
        result = ''
        while i < len(diff_text):
            if diff_text[i:i+2] == '- ':
                result += Fore.RED
                i += 2
            elif diff_text[i:i+2] == '+ ':
                result += Fore.GREEN
                i += 2
            elif diff_text[i:i+2] == '  ':
                result += Style.RESET_ALL
                i += 2
            else:
                if diff_text[i] == ' ':
                    result += Fore.YELLOW + '␣'
                    result += Style.RESET_ALL
                else:
                    result += diff_text[i]
                i += 1

        return result + Style.RESET_ALL



    def assertEqualWithDiff(self, first, second):
        """检查两个字符串是否相等，并在不相等的情况下显示有颜色标记的差异"""
        if first != second:
            diff = self.color_diff(first, second)
            message = '\n'.join([
                "Values are not equal:",
                "Actual (first string):",
                first,
                "Expected (second string):",
                second,
                "Difference:",
                diff,
            ])
            raise AssertionError(message)
        self.assertEqual(first, second)



    def test_normal_content(self):
        content = "“它的拉丁语是“lex parsimoniae”，即节约律。在英文中人们常常用格言“如无必要，勿增实体”（Do not multiply entities beyond necessity）来表达。”\
\
摘录来自\
直觉泵和其他思考工具\
【美】丹尼尔·丹尼特（Daniel C. Dennett）\
https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewBook?id=0\
此材料可能受版权保护。"

        expected_result = "它的拉丁语是“lexparsimoniae”，即节约律。在英文中人们常常用格言“如无必要，勿增实体”（Donotmultiplyentitiesbeyondnecessity）来表达。"
        self.assertEqualWithDiff(clean_content(content), expected_result)


    def test_content_with_extras(self):
        content = "“史特金定律表达得更粗俗一些：“任何事物当中的百分之九十都是垃圾（crap）。”\
\
摘录来自\
直觉泵和其他思考工具\
【美】丹尼尔·丹尼特（Daniel C. Dennett）\
https://itunes.apple.com/WebObjects/MZStore.woa/wa/viewBook?id=0\
此材料可能受版权保护。"
        expected_result = "史特金定律表达得更粗俗一些：“任何事物当中的百分之九十都是垃圾（crap）。”"
        self.assertEqualWithDiff(clean_content(content), expected_result)



    def test_chinese_with_space(self):
        content = "Test it!中 国 人 努力 工作，好  好生活 。加油！计算机科学家约瑟夫·魏岑鲍姆（Joseph Weizenbaum）一直渴望成为一位哲人"

        expected_result = "Test it!国人努力工作，好好生活。加油！计算机科学家约瑟夫·魏岑鲍姆（Joseph Weizenbaum）一直渴望成为一位哲人 haha"
        self.assertEqualWithDiff(clean_content(content), expected_result)

    def test_chinese_with_space2(self):
        content = "1939年8月23日，德国外长里宾特 洛 甫与苏联外交人民委员莫洛托夫，在莫斯科签署《苏德互不侵犯 条约》"

        expected_result = "1939年8月23日，德国外长里宾特洛甫与苏联外交人民委员莫洛托夫，在莫斯科签署《苏德互不侵犯条约》"
        self.assertEqualWithDiff(clean_content(content), expected_result)


if __name__ == "__main__":
    unittest.main()
