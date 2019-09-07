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

    '''
    print(colored('-'*20, 'red'), t)

if __name__ == "__main__":
    tic = time.process_time()
    
    main_process()

    toc = time.process_time()
    print("time=",toc - tic)





