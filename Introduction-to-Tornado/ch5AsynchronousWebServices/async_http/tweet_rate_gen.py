import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen

import urllib
import json
import datetime
import time

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

# 测试：siege http://localhost:8000/?q=test -c10 -t10s


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        query = self.get_argument('q')+" test2"
        client = tornado.httpclient.AsyncHTTPClient()
        response = yield tornado.gen.Task(client.fetch,
                "http://baike.baidu.com/api/openapi/BaikeLemmaCardApi?" + \
                urllib.parse.urlencode({"scope":103, "format": "json", "appid": 379020,"bk_key":'test',"bk_length":600}))
        body = json.loads(response.body.decode("utf-8"))
        result_count = len(body['catalog'])
        # now = datetime.datetime.utcnow()
        # raw_oldest_tweet_at = body['results'][-1]['created_at']
        # oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at,
        #         "%a, %d %b %Y %H:%M:%S +0000")
        # seconds_diff = time.mktime(now.timetuple()) - \
        #         time.mktime(oldest_tweet_at.timetuple())
        # tweets_per_second = float(result_count) / seconds_diff
        self.write("""
<div style="text-align: center">
    <div style="font-size: 72px">%s</div>
    <div style="font-size: 144px">%.02f</div>
    <div style="font-size: 24px">tweets per second</div>
</div>""" % (query, result_count))
        self.finish()

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
