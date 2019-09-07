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

    '''
    print(colored('-'*20, 'red'), t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





