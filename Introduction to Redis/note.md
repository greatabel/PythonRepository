直接运行: redis-server

启动Redis 默认6379端口，指定端口: redis-server --port 6380
连接Redis也可以自定义：redis-cli -h 127.0.0.1 -p 6379

停止Redis: redis-cli SHUTDOWN

osx配置文件位置：/usr/local/etc/redis.conf