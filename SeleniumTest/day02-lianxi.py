from selenium import webdriver
from seleniumtools import find_elemenet
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("http://ctw.testgoup.com/ljmanage/login.html")

username = ("xpath",'//*[@id="username"]')
password = ("xpath",'//*[@id="password"]')
login_button = ("xpath",'//*[@id="adminLogin"]')
homepage = ("xpath",'//*[@id="sidebar"]/ul/li[2]/a/span')

find_elemenet(driver,username).send_keys("admin")
find_elemenet(driver,password).send_keys("admin123")
find_elemenet(driver,login_button).click()

cf = find_elemenet(driver,homepage)
assert cf.text == '首页'
print('执行成功')
# driver.quit()

