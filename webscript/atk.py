from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options=Options()
options.add_argument('--headless')
a= int(0)
b = int(1000)
driver = webdriver.Firefox(options=options)

while a < int(b) :
	driver.get('http://210.38.137.126:8016/default2.aspx')
	a =int( a+int(1))
	print (a)
print ('finished')
