from unittest.mock import patch
import example

@patch('example.func2')
@patch('example.func1')
@patch('example.func')
def test1(x, mock_func, mock_func1, mock_func2):
    example.func(x)
    example.func1()
    example.func2()
    # print('x=',x)
    mock_func.assert_called_with(x)
    mock_func1.assert_called_with()
    mock_func2.assert_called_with()
    print('in test1')


if __name__ == "__main__":
    test1(1)