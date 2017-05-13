import sys,os
from os.path import abspath, join, dirname 
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# 如果没有上面的引入文件夹 就需要 import src.test
import test

