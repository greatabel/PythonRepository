import unittest
import os
import platform

class Tests(unittest.TestCase):
    def test_0(self):
        print('test_0')
        self.assertTrue(True)

    @unittest.skip('skipped test')
    def test_1(self):
        self.fail('should have failed')

    @unittest.skipIf(os.name=='posix', 'Not support on Unix')
    def test_2(self):
        print('test_2')
        import winreg


if __name__ == "__main__":
    unittest.main()