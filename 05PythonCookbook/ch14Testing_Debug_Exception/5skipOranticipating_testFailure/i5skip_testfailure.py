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

    @unittest.skipUnless(platform.system() == 'Darwin', 'Mac specific test')
    def test_3(self):
        print('test_3')
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()