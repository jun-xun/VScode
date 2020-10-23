import time
from selenium import webdriver
from seleniumtools import find_elemenet

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("https://www.bilibili.com/")
# step1：手动登录，去获取登录之后的cookie
# time.sleep(30)
# print(driver.get_cookies())

# step2:删掉未登录的cookie，然后把登录之后的cookie发给bilibili
driver.delete_all_cookies()
cookie = [{'domain': '.bilibili.com', 'httpOnly': False, 'name': 'bili_jct', 'path': '/', 'secure': False, 'value': '21a0c9c31c619f75d526bfc30275ee30'}, {'domain': '.bilibili.com', 'httpOnly': True, 'name': 'SESSDATA', 'path': '/', 'secure': False, 'value': '69171379%2C1618927315%2C178c0*a1'}, {'domain': '.bilibili.com',  'httpOnly': False, 'name': 'DedeUserID', 'path': '/', 'secure': False, 'value': '474277953'}, {'domain': '.bilibili.com',  'httpOnly': False, 'name': 'sid', 'path': '/', 'secure': False, 'value': 'kifihnrh'}, {'domain': 'www.bilibili.com', 'httpOnly': False, 'name': 'finger', 'path': '/', 'secure': False, 'value': '158939783'}, {'domain': '.bilibili.com',  'httpOnly': False, 'name': 'buvid3', 'path': '/', 'secure': False, 'value': 'BF7F3C13-90AA-4B8D-979B-9DFF3819B366143073infoc'}, {'domain': '.bilibili.com',  'httpOnly': False, 'name': 'DedeUserID__ckMd5', 'path': '/', 'secure': False, 'value': '24f173672564bca2'}, {'domain': '.bilibili.com', 'httpOnly': False, 'name': '_uuid', 'path': '/', 'secure': False, 'value': '108CFF15-B84E-B693-AD40-4D447D8FB1B594294infoc'}]
for c in cookie:
    driver.add_cookie(c)
driver.refresh()
