# The standard library modules
import os
import sys

# The wget module
import wget

# The BeautifulSoup module
from bs4 import BeautifulSoup

# The selenium module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# step 2
driver = webdriver.Chrome() # if you want to use chrome, replace Firefox() with Chrome()
# driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])
pre_url = "https://www.packtpub.com/mapt/book/Web Development/9781784393656/"
test_url  = pre_url + "1"
driver.get(test_url) # load the web page

# step 3: analysis list
