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

# driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true'])
pre_url = "https://www.packtpub.com"
test_url = "https://www.packtpub.com/mapt"
#  https://www.packtpub.com/mapt/book/Web Development/9781784393656/1
driver = webdriver.Firefox()
# for websites that need you to login to access the information
driver.get(test_url) 


driver.find_element_by_css_selector('.btn.btn-warning.navbar-btn.mr15.ml15').click()
# driver.switch_to_window(driver.window_handles[-1])



print('driver.title=', driver.title)
element = WebDriverWait(driver, 12).until(
            EC.presence_of_element_located((By.ID, "exampleInputPassword1"))
        )



email = driver.find_element_by_id("wrapper").find_element_by_id("exampleInputEmail1") # Find the email input field of the login form
print('email=',email)
driver.execute_script("$(arguments[0]).click(); $(arguments[0]).value='greatabel1@126.com'", email)
# email.click()

# email.send_keys("greatabel1@126.com") # Send the users email
pwd = driver.find_element_by_id("wrapper").find_element_by_id("exampleInputPassword1") # Find the password field of the login form
driver.execute_script("$(arguments[0]).click(); $(arguments[0]).value='1048576'", pwd)
print('pwd=',pwd)
# pwd.click()
# pwd.send_keys("1048576") # send the users password
# elem.send_keys(Keys.RETURN) # press the enter key
# driver.find_element_by_name("submit").click()
submit = driver.find_element_by_id("wrapper").find_elements_by_class_name('btn btn-primary btn-block btn-lg') # Find the password field of the login form
driver.execute_script("$(arguments[0]).click();",submit)
print('login')

# WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "h2")))
counter = 0
for item in t[0:2]:
    try:
        counter += 1
        # driver = webdriver.Firefox()
        driver.get(pre_url+item) # load the web page
        element = WebDriverWait(driver, 12).until(
            EC.presence_of_element_located((By.ID, "reader-content"))
        )
        # waits till the element with the specific id appears
        # src = driver.page_source # gets the html source of the page
        # print('#'*20,len(src),src[0:150],'*'*10)
        # Html_file= open("filename.html","w")
        # Html_file.write(src)
        # Html_file.close()
        shotname = str(counter) +'test.png'
        print(shotname)
        driver.save_screenshot(shotname)
        # driver.quit()
        # save_me = ActionChains(driver).key_down(Keys.CONTROL)\
        #      .key_down('s').key_up(Keys.CONTROL).key_up('s')
        # save_me.perform()

    finally:
        # driver.quit()
        print('in finally')
driver.quit()



# step 3: analysis list
# print('-'*10,'step 3:')
# filestr = ""
