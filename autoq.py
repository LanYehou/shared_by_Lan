# -*- coding:utf-8 -*-
from selenium import webdriver
import time 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
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
element=driver.find_element_by_xpath("//*[@id='headDiv']/ul/li[3]/a/span")
ActionChains(driver).move_to_element(element).perform()
# input=driver.find_element_by_xpath("//*[@id='headDiv']/ul/li[2]/a/span").click()
input=driver.find_element_by_xpath("//*[@id='headDiv']/ul/li[3]/ul/li[2]/a").click()
#input=driver.find_element_by_xpath("//*[@id='pjkc']").click
#input=driver.find_element_by_xpath("//*[@id='pjkc']/option[7]").click
driver.switch_to_frame('iframeautoheight')
time.sleep(2)
#element=driver.find_element_by_xpath("//*[@id='pjkc']")
#ActionChains(driver).move_to_element(element).perform()
s=driver.find_element_by_xpath("//*[@id='pjkc']")
time.sleep(1)
Select(s).select_by_index("1")
time.sleep(1)
s=driver.find_element_by_xpath("//*[@id='DataGrid1__ctl2_JS1']")
Select(s).select_by_index("2")
s=driver.find_element_by_xpath("//*[@id='DataGrid1__ctl3_JS1']")
Select(s).select_by_index("7")
s=driver.find_element_by_xpath("//*[@id='DataGrid1__ctl4_JS1']")
Select(s).select_by_index("2")
s=driver.find_element_by_xpath("//*[@id='DataGrid1__ctl5_JS1']")
Select(s).select_by_index("2")
s=driver.find_element_by_xpath("//*[@id='DataGrid1__ctl6_JS1']")
Select(s).select_by_index("1")
s=driver.find_element_by_xpath("//*[@id='DataGrid1__ctl7_JS1']")
Select(s).select_by_index("1")
s=driver.find_element_by_xpath("//*[@id='DataGrid1__ctl8_JS1']")
Select(s).select_by_index("1")
s=driver.find_element_by_xpath("//*[@id='DataGrid1__ctl9_JS1']")
Select(s).select_by_index("2")
s=driver.find_element_by_xpath("//*[@id='DataGrid1__ctl10_JS1']")
Select(s).select_by_index("2")
s=driver.find_element_by_xpath("//*[@id='DataGrid1__ctl11_JS1']")
Select(s).select_by_index("1")
s=driver.find_element_by_xpath("//*[@id='DataGrid1__ctl12_JS1']")
Select(s).select_by_index("3")
s=driver.find_element_by_xpath("//*[@id='DataGrid1__ctl13_JS1']")
Select(s).select_by_index("1")
s=driver.find_element_by_xpath("//*[@id='DataGrid1__ctl14_JS1']")
Select(s).select_by_index("3")
s=driver.find_element_by_xpath("//*[@id='DataGrid1__ctl15_JS1']")
Select(s).select_by_index("3")

driver.find_element_by_xpath("//*[@id='Button1']").click



