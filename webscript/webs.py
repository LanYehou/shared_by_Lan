# -*- coding:utf-8 -*-
from selenium import webdriver
import time 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Firefox()
driver.get('http://210.38.137.77:8016/')
input=driver.find_element_by_id("txtUserName")
input.send_keys("201911411312")
input=driver.find_element_by_id("Textbox1").click()
input=driver.find_element_by_id("TextBox2").click()
input=driver.find_element_by_id("TextBox2")
input.send_keys("lan1756806422")
time.sleep(7)
input=driver.find_element_by_id("Button1").click()
element=driver.find_element_by_xpath("//*[@id='headDiv']/ul/li[2]/a/span")
ActionChains(driver).move_to_element(element).perform()
# input=driver.find_element_by_xpath("//*[@id='headDiv']/ul/li[2]/a/span").click()
input=driver.find_element_by_xpath("//*[@id='headDiv']/ul/li[2]/ul/li[2]/a").click()
driver.switch_to_frame('iframeautoheight')
time.sleep(2)
input=driver.find_element_by_id("kj").click
# //*[@id="kj"]
input=driver.find_element_by_xpath("//*[@id='kj']/option[8]").click

input=driver.find_element_by_xpath("//*[@id='kcmcGrid__ctl3_xk']").click
time.sleep(2)
input=driver.find_element_by_xpath("//*[@id='Button1']").click
