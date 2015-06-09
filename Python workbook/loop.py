import time

import logging
import os
print(os.getcwd())
logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

i = 0 
while True:
	print(i)
	logging.info(i)
	i+=1
	print("This prints once 1s.")
	time.sleep(1)
