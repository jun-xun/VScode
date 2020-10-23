# 导入 selenium
from selenium import webdriver
import time

# 打开谷歌浏览器： Chrome 的C大写的！！  浏览器的把柄
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
# 打开网址
driver.get("https://www.baidu.com/")

# 查找输入框和搜索框按钮，通过id值来定位元素（这里没有s）
# driver.find_element_by_id("kw").send_keys("重阳节")

# driver.find_element_by_id("su").click()

# xpath
# driver.find_element_by_xpath('//*[@id="kw"]').send_keys("祭祖")
# driver.find_element_by_xpath('//*[@id="su"]').click()

# name
# driver.find_element_by_name('wd').send_keys("hello world!")
# driver.find_element_by_id("su").click()

# clssname
# driver.find_element_by_class_name('s_ipt').send_keys("重庆小面")
# driver.find_element_by_id("su").click()

# css selector
# driver.find_element_by_css_selector('#kw').send_keys("红烧猪蹄")

# link text
# driver.find_element_by_link_text('贴吧').click()
# driver.find_element_by_partial_link_text("贴").click()

# tag
# driver.find_element_by_tag_name("a")

# time.sleep(5)
# driver.find_element_by_xpath('//*[@id="wd1"]').send_keys("软件测试")
# driver.find_element_by_xpath('//*[@id="tb_header_search_form"]/span[2]/a').click()

e = driver.find_element_by_id("kw")
e.send_keys("红烧猪蹄儿")
# driver.find_element_by_id("su").click()
print(e)

# 浏览器标题
print(driver.title)  # 有括号的是方法，没有括号的是变量；driver.title是一个变量
print(driver.current_url)  # driver.current_url浏览器地址

# 退出测试，自动关闭浏览器
driver.quit()