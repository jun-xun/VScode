# 导入 selenium
from selenium import webdriver
import time

# 打开谷歌浏览器： Chrome 的C大写的！！  浏览器的把柄
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
# 打开网址
driver.get("http://ljtest.net:9090/shopxo/admin.php?s=/admin/logininfo.html")
# 搜索
driver.implicitly_wait(10)
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[1]/input').send_keys("admin")
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[2]/input').send_keys("shopxo")
driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[3]/button').click()









