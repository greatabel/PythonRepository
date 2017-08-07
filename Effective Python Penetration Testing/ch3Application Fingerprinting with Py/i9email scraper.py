from bs4 import BeautifulSoup
import requests
import requests.exceptions
# import urlparse 
import urllib.parse
from collections import deque
import re

urls = deque(['https://www.packtpub.com/'])
print(type(urls), urls)