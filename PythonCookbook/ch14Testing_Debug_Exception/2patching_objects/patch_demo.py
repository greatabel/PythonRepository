# https://docs.python.org/3/library/unittest.mock.html
from unittest.mock import MagicMock, Mock, patch

class ProductClass:
    def test():
        print('test')

thing = ProductClass()
thing.method = MagicMock(return_value=3)
print( thing.method(3,4,5, key='value') )
thing.method.assert_called_with(3, 4, 5, key='value')
# thing.method.assert_called_with(1, 2, 3, 4, 5, key='value')

mock = Mock(side_effect=KeyError('testerror'))
# mock()

import moduletest

@patch('moduletest.ClassName2')
@patch('moduletest.ClassName1')
def test(MockClass1, MockClass2):
    moduletest.ClassName1()
    moduletest.ClassName2()
    assert MockClass1 is moduletest.ClassName1
    assert MockClass2 is moduletest.ClassName2
    assert MockClass1.called
    assert MockClass2.called

test()
