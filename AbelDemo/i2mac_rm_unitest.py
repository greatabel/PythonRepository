# coding=utf-8
import time
import unittest
import difflib
from colorama import Fore, Back, Style, init
from i2mac_rmcitation_m1 import clean_content


class TestCleanContent(unittest.TestCase):
    def color_diff(self, expected, actual):
        """为差异部分添加颜色"""
        diff = difflib.ndiff(expected, actual)
        diff_text = "".join(diff)

        i = 0
        result = ""
        while i < len(diff_text):
            if diff_text[i : i + 2] == "- ":
                result += Fore.RED
                i += 2
            elif diff_text[i : i + 2] == "+ ":
                result += Fore.GREEN
                i += 2
            elif diff_text[i : i + 2] == "  ":
                result += Style.RESET_ALL
                i += 2
            else:
                if diff_text[i] == " ":
                    result += Fore.GREEN + "␣"
                    result += Style.RESET_ALL
                else:
                    result += diff_text[i]
                i += 1

        return result + Style.RESET_ALL

    def assertEqualWithDiff(self, first, second):
        """检查两个字符串是否相等，并在不相等的情况下显示有颜色标记的差异"""
        if first != second:
            diff = self.color_diff(first, second)
            message = "\n".join(
                [
                    "Values are not equal:",
                    "我们清理算法结果 (first string):",
                    first,
                    "完美期望结果 (second string):",
                    second,
                    "Difference:",
                    diff,
                ]
            )
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

        expected_result = "它的拉丁语是“lex parsimoniae”，即节约律。在英文中人们常常用格言“如无必要，勿增实体”（Do not multiply entities beyond necessity）来表达。"
        start_time = time.time()  # 记录开始时间
        actual_result = clean_content(content)
        end_time = time.time()  # 记录结束时间

        duration = end_time - start_time
        print(f"Test 'test_normal_content' took {duration:.6f} seconds to run.")

        self.assertEqualWithDiff(actual_result, expected_result)

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

    def test_chinese_with_space1(self):
        content = "What a good day!中 国 人 努力 工作，好  好生活。加油！计算机科学家约瑟夫·魏岑鲍姆（Joseph Weizenbaum）一直渴望成为一位哲人。"

        expected_result = "What a good day!中国人努力工作，好好生活。加油！计算机科学家约瑟夫·魏岑鲍姆（Joseph Weizenbaum）一直渴望成为一位哲人。"
        self.assertEqualWithDiff(clean_content(content), expected_result)

    def test_chinese_with_space2(self):
        content = "1939年8月23日，德国外长里宾特 洛 甫与苏联外交人民委员莫洛托夫，在莫斯科签署《苏德互不侵犯 条约》"

        expected_result = "1939年8月23日，德国外长里宾特洛甫与苏联外交人民委员莫洛托夫，在莫斯科签署《苏德互不侵犯条约》"
        self.assertEqualWithDiff(clean_content(content), expected_result)

    def test_chinese_with_space3(self):
        content = " 以 及 1 9 4 4 年 年 初 解 放 该 城 ， 反 映 并 影 响 了 苏 联 的战 时 军 事 战 略。 1 9 4 1 年 战 争初期。"

        expected_result = "以及1944年年初解放该城，反映并影响了苏联的战时军事战略。1941年战争初期。"
        self.assertEqualWithDiff(clean_content(content), expected_result)

    def test_chinese_with_space4(self):
        content = "  虽 然这 座 城 市 几 乎 被 完 全 封 锁， 但 红 军 粉 碎 了德 国 人从 东 面彻 底 包 围列 宁格 勒 的 企图"

        expected_result = "虽然这座城市几乎被完全封锁，但红军粉碎了德国人从东面彻底包围列宁格勒的企图"
        self.assertEqualWithDiff(clean_content(content), expected_result)

    def test_chinese_with_line5(self):
        content = '''“但愿一直没到夏天
夏天就永远在路上
——［丹麦］亨里克·诺德布兰德《在以色列广场”

摘录来自
春山多胜事：四时读诗
三书
此材料可能受版权保护。"'''

        # 修改为合并后的预期结果
        expected_result = "但愿一直没到夏天夏天就永远在路上——［丹麦］亨里克·诺德布兰德《在以色列广场》"
        self.assertEqualWithDiff(clean_content(content), expected_result)


    def test_pdf_like_kangxi_radicals_spacing(self):
        content = """示 显 现 妄 念 ， 本 体 未 成 者 ：
    ⽆ 知 愚 稚 别 ® 倒 相 ， ⼼ 造 诸 显 有 相 法 ，
    由 习 ⽓ ⽣ ⽆ 实 有 ， 对 此 不 起 能 所 执 ，
    应 悟 ⼀ 切 超 ⾔ 诠"""

        # 预期结果和实际一致，保留首行换行
        expected_result = (
            "示显现妄念，本体未成者：\n"
            "⽆知愚稚别®倒相，⼼造诸显有相法，由习⽓⽣⽆实有，对此不起能所执，应悟⼀切超⾔诠"
        )
        self.assertEqualWithDiff(clean_content(content), expected_result)


    def test_pdf_sentence_linebreak_merge(self):
        content = """劳 埃 德 认 他 找 到 了 ⼀ 种 新 的 ⽅ 式 来 解 释 科 学 中 最 基 本 的 问
    题 ： 世 界 为 何 如 此 复 杂 ？ 他 的 回 答 回 到 了 这 样 的 观 念 ， 即 信 息 总 是
    会 产 ⽣ 更 多 的 信 息 . D N A 、 性 别 和 意 识 的 最 终 出 现 实 际 上 是 不 可 避 免
    的 . 这 是 ⼀ 个 令 ⼈ 着 迷 且 令 ⼈ 深 感 欣 慰 的 想 法 .
    — 《 纽 约 时 报 》"""

        expected_result = """劳埃德认他找到了⼀种新的⽅式来解释科学中最基本的问题：世界为何如此复杂？他的回答回到了这样的观念，即信息总是会产⽣更多的信息 . D N A 、性别和意识的最终出现实际上是不可避免的 . 这是⼀个令⼈着迷且令⼈深感欣慰的想法 .\n— 《纽约时报》"""
        self.assertEqualWithDiff(clean_content(content), expected_result)

if __name__ == "__main__":
    unittest.main()