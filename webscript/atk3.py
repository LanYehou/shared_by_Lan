from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
options=Options()
options.add_argument('--headless')
a= int(0)
b = int(1000)
c = int(1)
driver = webdriver.Firefox(options=options)
driver.get('http://210.38.137.125:8016/default2.aspx')
while c < b :
	driver.get('http://210.38.137.125:8016/default2.aspx')
	driver.close
	a =int( a+int(1))
	print (a)
	time.sleep(0.5)
driver.quit
print ('finished')
