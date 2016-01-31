from unittest.mock import patch
import example

def test1(x):
    with patch('example.func') as mock_func:
        example.func(x)
        mock_func.assert_called_with(x)    

if __name__ == "__main__":
    test1(1)