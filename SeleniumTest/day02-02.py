# 导入 selenium
from selenium import webdriver
from seleniumtools import find_elemenet
import time 

# 打开谷歌浏览器： Chrome 的C大写的！！  浏览器的把柄
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
# 打开网址
driver.get("http://ctw.testgoup.com/ljmanage/login.html")

username = ("id","username")
password = ("id","password")
loginbtn = ("id","adminLogin")
homepage = ("xpath",'//*[@id="sidebar"]/ul/li[3]/a/span')

find_elemenet(driver,username).send_keys("admin")
find_elemenet(driver,password).send_keys("admin1234")
find_elemenet(driver,loginbtn).click()

time.sleep(5)
driver.switch_to_alert().accept()  # 去点击alert 的确定按钮
# driver.switch_to_alert().dismiss()  # 去点击alert 的取消按钮

e = find_elemenet(driver,homepage)
assert e.text == "用户管理"
print("执行成功")
time.sleep(3)
driver.quit()