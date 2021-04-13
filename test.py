from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
site_url = 'https://output.jsbin.com/radara'
print("before get()")
sleep(5)
driver.get(site_url)
print("before quit()")
sleep(5)
driver.quit()
