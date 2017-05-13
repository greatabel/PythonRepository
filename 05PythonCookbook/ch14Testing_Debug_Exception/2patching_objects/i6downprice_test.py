import unittest
from unittest.mock import patch 
import io
import i6downprice

sample_data = io.BytesIO(b'''\
"IBM",91.1\r
"AA",13.25\r
"MSFT",27.72\r

''')

class Tests(unittest.TestCase):
    @patch('i6downprice.urlopen', return_value=sample_data)
    def test_downprices(self, mock_urlopen):
        p = i6downprice.downprices()
        self.assertTrue(mock_urlopen.called)
        self.assertEqual(p, 
            {"IBM":91.1,
            "AA": 13.25,
            "MSFT": 27.72})

if __name__ == "__main__":
    unittest.main()
    