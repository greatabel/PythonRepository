import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient

import urllib
import json
import datetime
import time

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

#http://stackoverflow.com/questions/28906859/module-has-no-attribute-urlencode
#被墙了twitter后，http://www.jincon.com/archives/361/ 测试调用：http://localhost:8000/?q=test


class IndexHandler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	def get(self):
		query = self.get_argument('q')
		client = tornado.httpclient.AsyncHTTPClient()
		client.fetch("http://baike.baidu.com/api/openapi/BaikeLemmaCardApi?" + \
				urllib.parse.urlencode({"scope":103, "format": "json", "appid": 379020,"bk_key":'test',"bk_length":600}),
				callback=self.on_response)

	def on_response(self, response):
		print('len(body)=',len(response.body),'0-10:',response.body[0:10])
		body = json.loads(response.body.decode("utf-8"))
		result_count = len(body['catalog'])
		# now = datetime.datetime.utcnow()
		# raw_oldest_tweet_at = '2015-07-10'
		# oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at,
		# 		"%a, %d %b %Y %H:%M:%S +0000")
		# seconds_diff = time.mktime(now.timetuple()) - \
		# 		time.mktime(oldest_tweet_at.timetuple())
		# tweets_per_second = float(result_count) / seconds_diff

		self.write("""
<div style="text-align: center">
	<div style="font-size: 72px">%s</div>
	<div style="font-size: 144px">%.02f</div>
	<div style="font-size: 24px">tweets per second</div>
</div>""" % (self.get_argument('q'), result_count))
		self.finish()

if __name__ == "__main__":
	tornado.options.parse_command_line()
	app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
