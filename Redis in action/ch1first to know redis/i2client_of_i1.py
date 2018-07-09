import time
import unittest
from  i1redis_vote import *


class TestCh01(unittest.TestCase):
    def setUp(self):
        import redis
        self.conn = redis.Redis(db=15)
        print('setUp')

    def tearDown(self):
        del self.conn
        print('tearDown')

    def test_article_functionality(self):
        print('start', '#'*20)

        conn = self.conn
        import pprint

        article_id = str(post_article(conn, 'A username', 'A title', 'http://www.google.com'))
        print("We posted a new article with id:", article_id)
        self.assertTrue(article_id)
        print('end  ', '#'*20)

if __name__ == '__main__':
    unittest.main()