'''



#----------------------------#



'''

import time
from termcolor import colored


def main_process():
    t = '''
    1. 什么是flask?
    ans: Flask是Python编写的一款轻量级Web应用框架。其 WSGI 工具箱采用 Werkzeug ，
    模板引擎则使用 Jinja2。
    Flask使用 BSD 授权。其中两个环境依赖是Werkzeug和jinja2，这意味着它不需要依赖外部库。
    正因如此，我们将其称为轻量级框架
    --------------------
    2. flask是一个MVC模型？
    flask是个经典的MVC框架

    3. flask中连接数据库？
    在脚本中以用第三方库正常连接，用sql语句正常操作数据库，如mysql关系型数据库的pymsql库
    用ORM来进行数据库连接，flask中典型的flask_sqlalchemy，已面向对象的方式进行数据库的连接与操

    4.列举Http请求中的状态码?
    200 访问正常
    201 创建了资源
    300 多种选择。请求的资源可包括多个位置，相应可返回一个资源特征与地址的列表用于用户终端（例如：浏览器）选择
    301 永久性重定向
    302 临时性重定向
--  4XX 服务器无法处理请求
    400 请求报文中存在错误，服务器无法理解
    404 服务器无法根据客户端的请求找到资源
--  5XX 服务器内部错误
    500 internal Server Error 服务器内部错误
    503 服务器暂时处于超负载或正在进行停机维护，现在无法处理请求

    5. HTTP协议里的请求头有什么用?

    Accept-Encoding:用于告诉服务器，客户机支持的数据压缩格式
    User-Agent：用于告诉服务器，客户机的软件环境
    Cookie：客户机通过这个头可以想服务器带数据
    ETag：缓存相关的头，和Last-Modified功能一样，不过实时性更强
    
    request 里的 Accept-* 可有钦定的意思？
    Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
    Accept-Encoding:gzip, deflate, sdch
    Accept-Language:zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4

    response 里的 Content-* 才是已经决定了就是你了这个意思好吗
    Content-Encoding:gzip
    Content-Length:5506
    Content-Type:text/html;charset=utf-8


    '''
    print(colored('-'*20, 'red'), t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





