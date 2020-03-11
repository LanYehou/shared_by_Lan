# -*- coding:utf-8 -*-
from selenium import webdriver
import time 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
#driver=webdriver.Firefox()
driver.get('https://cloud.tencent.com/')
time.sleep(5)
input=driver.find_element_by_xpath("//*[@id='qcTopNavFstLevel']/div[2]/div/div[2]/a[2]").click
#input.send_keys("201911411312")
time.sleep(5)
input=driver.find_element_by_xpath("//*[@id='loginBox']/div/div/div[4]/div[2]/div[1]/a").click()
#input=driver.find_element_by_id("TextBox2").click()
input=driver.find_element_by_xpath("//*[@id='loginBox']/div/div/div[2]/div[2]/ul/li[1]/div/div/input")
input.send_keys("lanyehou@qq.com")
#time.sleep(7)
input=driver.find_element_by_xpath("//*[@id='loginBox']/div/div/div[2]/div[2]/ul/li[2]/div/div/input")


#element=driver.find_element_by_xpath("//*[@id='headDiv']/ul/li[2]/a/span")
#ActionChains(driver).move_to_element(element).perform()
# input=driver.find_element_by_xpath("//*[@id='headDiv']/ul/li[2]/a/span").click()
input=driver.find_element_by_xpath("//*[@id='loginBox']/div/div/div[2]/div[2]/div[2]/a[1]").click()
#driver.switch_to_frame('iframeautoheight')
time.sleep(2)
input=driver.find_element_by_xpath("//*[@id='appArea']/div/div/div/div[1]/div/div[3]/div/div[2]/div[3]/div[2]/div/div/div[1]/div/div[2]/div[2]/text()").text
print (input)
# //*[@id="kj"]
#input=driver.find_element_by_xpath("//*[@id='kj']/option[8]").click

#input=driver.find_element_by_xpath("//*[@id='kcmcGrid__ctl3_xk']").click
#time.sleep(2)
#input=driver.find_element_by_xpath("//*[@id='Button1']").click
driver.quit
