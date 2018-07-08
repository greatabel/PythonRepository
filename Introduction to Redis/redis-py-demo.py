import redis  
#http://blog.csdn.net/chosen0ne/article/details/7319807  
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)  
r = redis.Redis(connection_pool=pool)  
r.set('one', 'first')  
r.set('two', 'second')  
print(r.get('one') )
print(r.get('two') )