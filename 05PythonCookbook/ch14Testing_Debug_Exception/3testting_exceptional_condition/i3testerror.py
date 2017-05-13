import errno
import unittest

class  TestIO(unittest.TestCase):
    def test_file_not_found(self):
        try:
            f = open('file/test_file_not_found')
        except IOError as e:
            self.assertEqual(e.errno,errno.ENOENT)
        else:
            self.fail('IOError not rasied')

if __name__ == "__main__":
    unittest.main()
