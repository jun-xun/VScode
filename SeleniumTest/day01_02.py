# 导入 selenium
from selenium import webdriver
import time

# 打开谷歌浏览器： Chrome 的C大写的！！  浏览器的把柄
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
# 打开网址
driver.get("http://ljtest.net:9090/shopxo/")
# 搜索
driver.find_element_by_id("search-input").send_keys("裙子")
driver.find_element_by_id("ai-topsearch").click()

# 固定等待
time.sleep(10)
# 隐式等待，自动检测网页是否加载完成
driver.implicitly_wait(8)

# 寻找对应的元素判断结果 
e = driver.find_element_by_xpath("/html/body/div[4]/div/ul/li/div/p[2]/strong")
assert e.text == '￥0.01-128.00'
print("成功！")