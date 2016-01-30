# https://docs.python.org/3/library/unittest.mock.html
from unittest.mock import MagicMock, Mock

class ProductClass:
    def test():
        print('test')

thing = ProductClass()
thing.method = MagicMock(return_value=3)
print( thing.method(3,4,5, key='value') )
thing.method.assert_called_with(3, 4, 5, key='value')
# thing.method.assert_called_with(1, 2, 3, 4, 5, key='value')

mock = Mock(side_effect=KeyError('testerror'))
mock()
