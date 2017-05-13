from unittest.mock import patch
import example

def test1(x):
    p = patch('example.func')
    mock_func = p.start()
    example.func(x)
    mock_func.assert_called_with(x)
    p.stop()    

if __name__ == "__main__":
    test1(1)