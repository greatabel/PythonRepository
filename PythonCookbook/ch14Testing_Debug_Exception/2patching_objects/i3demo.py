from unittest.mock import MagicMock

class ProductClass:
    def test():
        print('test')

thing = ProductClass()
thing.method = MagicMock(return_value=3)
print( thing.method(3,4,5, key='value') )

