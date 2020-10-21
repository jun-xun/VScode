# 导入 selenium
from selenium import webdriver

# 打开谷歌浏览器： Chrome 的C大写的！！  浏览器的把柄
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
# 打开网址
driver.get("https://www.baidu.com/")

# 查找输入框和搜索框按钮，通过id值来定位元素（这里没有s）
driver.find_element_by_id("kw").send_keys("广西")
driver.find_element_by_id("su").click()

# xpath
# driver.find_element_by_xpath('/html/body/header/div/form/div/input').send_keys("bilibili")
# driver.find_element_by_xpath('//*[@id="su"]').click()

# name
# driver.find_element_by_name('wd').send_keys("包包")
# driver.find_element_by_class_name('wd').click()

# print(driver.title)
# print(driver.current_url)

# driver.quit()