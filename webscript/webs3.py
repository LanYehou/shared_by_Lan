# -*- coding:utf-8 -*-
from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
#options=Options()
#options.add_argument('--headless')
#driver=webdriver.Firefox(options=options)
driver=webdriver.Firefox()
driver.get('http://139.199.75.55/owncloud/index.php/login')

input=driver.find_element_by_id("user")
input.send_keys("1193")
#input=driver.find_element_by_id("Textbox1").click()
#input=driver.find_element_by_id("TextBox2").click()
input=driver.find_element_by_id("password")
input.send_keys("jz1193")
input=driver.find_element_by_id("submit").click()
#driver.get('http://139.199.75.55/owncloud/index.php/login')

