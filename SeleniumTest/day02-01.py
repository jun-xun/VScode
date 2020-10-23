# 导入 selenium
from selenium import webdriver
from seleniumtools import find_elemenet
import time 

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()

driver.get("http://ctw.testgoup.com/ljmanage/login.html")

username = ("id","username")
password = ("id","password")
loginbtn = ("id","adminLogin")
homepage = ("xpath",'//*[@id="sidebar"]/ul/li[3]/a/span')

find_elemenet(driver,username).send_keys("admin")
find_elemenet(driver,password).send_keys("admin123")
find_elemenet(driver,loginbtn).click()



e = find_elemenet(driver,homepage)
assert e.text == "用户管理"
print("执行成功")
time.sleep(3)
driver.quit()