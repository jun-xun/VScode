from selenium import webdriver
from seleniumtools import find_elemenet
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("https://www.gamersky.com/pcgame/")

# a = ("xpath",'/html/body/div[5]/div[2]/div[2]/a[2]')
# find_elemenet(driver,a).click()
gf = ("xpath",'/html/body/div[9]/div[1]/div[2]/div[2]/ul/li[1]/div[2]/div[1]/div[5]/a')
find_elemenet(driver,gf).click()

print(driver.title)
print(driver.window_handles) # ['CDwindow-B3E03E31DB1F3C03D707383F63686F62', 'CDwindow-69BAE93722C78D969FE0E36C5FED7E3D'],抓住窗口的把柄
driver.switch_to_window(driver.window_handles[-1]) # 把作用域切换到最后一个窗口
print(driver.title)

