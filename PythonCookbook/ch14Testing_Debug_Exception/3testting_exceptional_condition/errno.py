import unittest

def parse_int(s):
    return int(s)

class TestConversation(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, 'N/A')

if __name__ == "__main__":
    unittest.main()