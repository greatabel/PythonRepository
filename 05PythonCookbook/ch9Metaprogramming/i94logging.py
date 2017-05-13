import logging
import os
# http://blog.csdn.net/jgood/article/details/4340740
if __name__ == "__main__":
    # logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'),
    # level = logging.DEBUG)
    # logging.debug('This is a message')

    # logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'),  
    # level = logging.WARN, filemode = 'w', format = '%(asctime)s - %(levelname)s: %(message)s')  
    # logging.debug('debug')  #被忽略  
    # logging.info('info')    #被忽略  
    # logging.warning('warn')  
    # logging.error('error')  

    logging.basicConfig(filename = os.path.join(os.getcwd(), 'log1.txt'), level = logging.DEBUG)
    log = logging.getLogger('root.test')  
    log.setLevel(logging.WARN)  #日志记录级别为WARNNING  
    log.info('info')    #不会被记录  
    log.debug('debug')  #不会被记录  
    log.warning('warnning')  
    log.error('error')  
#----- 结果  
#2009-07-13 21:42:15,592 - WARNING: warn  
#2009-07-13 21:42:15,640 - ERROR: error  