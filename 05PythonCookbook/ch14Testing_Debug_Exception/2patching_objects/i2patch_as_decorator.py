from unittest.mock import patch
import example

@patch('example.func')
def test1(x, mock_func):
    example.func(x)
    # print('x=',x)
    mock_func.assert_called_with(x)
    print('in test1')


if __name__ == "__main__":
    test1(1)
    # example.func(10)
