# 导入 selenium
from selenium import webdriver
import time

# 打开谷歌浏览器： Chrome 的C大写的！！  浏览器的把柄
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
# 打开网址
driver.get("https://www.taobao.com/")
# 搜索
driver.find_element_by_xpath('//*[@id="q"]').send_keys("机械键盘")
driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()

# 手动扫码登录
time.sleep(10)


# 结果页面
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[2]/div[1]/div/div[1]').click()
# 商品详情页面
driver.implicitly_wait(10)

# driver.switch_to_window(driver.window_handles[-3])

# 选取商品规格
driver.find_element_by_xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[4]/div/div/dl[1]/dd/ul/li[19]/a/span').click()
driver.find_element_by_xpath('//*[@id="J_regionSellServer"]/dd/ul/li[1]/a').click()
driver.find_element_by_xpath('//*[@id="J_LinkBuy"]').click()
# driver.implicitly_wait(10)
# driver.find_element_by_xpath('//*[@id="J_LinkBuy"]').click()






