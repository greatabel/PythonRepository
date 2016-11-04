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

from selenium.webdriver.common.action_chains import ActionChains

with open ("source.html", "r") as myfile:
    src=myfile.read()

import re
# regex = r'"/mapt/book/Web Development/9781784393656/(.*.)"\$'
regex = r'/mapt/book/Web Development/9781784393656/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
results = re.findall(regex, src)
t = list(set(results))
t.sort()
for item in t:
    print('#:',item)
print('url count:', len(t))

print('in load')
# step 2
# driver = webdriver.Chrome() # if you want to use chrome, replace Firefox() with Chrome()
driver = webdriver.Firefox()
# driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])
pre_url = "https://www.packtpub.com/mapt/book/Web Development/9781784393656/"
test_url  = pre_url + "1"
driver.get(test_url) # load the web page


# WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "h2")))

try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "reader-content"))
    )
    # waits till the element with the specific id appears
    src = driver.page_source # gets the html source of the page
    print('#'*20,len(src),src[0:150],'*'*10)
    Html_file= open("filename.html","w")
    Html_file.write(src)
    Html_file.close()
    driver.save_screenshot('screenie.png')
    # save_me = ActionChains(driver).key_down(Keys.CONTROL)\
    #      .key_down('s').key_up(Keys.CONTROL).key_up('s')
    # save_me.perform()

finally:
    driver.quit()



# step 3: analysis list
# print('-'*10,'step 3:')
# filestr = ""
