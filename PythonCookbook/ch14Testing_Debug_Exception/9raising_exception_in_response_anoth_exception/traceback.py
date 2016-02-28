# pip3.5 取代了过去的pip3
import sys,traceback

try:  
    1/0  
except Exception as e:  
    traceback.print_exc(file=sys.stdout)