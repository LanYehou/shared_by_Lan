# -*- coding:utf-8 -*-
from selenium import webdriver
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.get('http://210.38.137.126:8016/default2.aspx')
input=driver.find_element_by_id("txtUserName")
input.send_keys("201911411312")
input=driver.find_element_by_id("Textbox1").click()
input=driver.find_element_by_id("TextBox2").click()
input=driver.find_element_by_id("TextBox2")
input.send_keys("lan1756806422")

