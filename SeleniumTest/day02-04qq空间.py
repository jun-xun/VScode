from selenium import webdriver
from seleniumtools import find_elemenet
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("https://qzone.qq.com/")

# 把作用域切换到小网页
frame = driver.find_element_by_id('login_frame')
driver.switch_to_frame(frame)

driver.find_element_by_id('switcher_plogin').click()  # 点击账号密码登录
driver.find_element_by_id("u").send_keys("123")  # 输入qq号

# 把作用域切换回来
driver.switch_to_default_content()
driver.find_element_by_link_text('官方空间').click()

