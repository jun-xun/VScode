import unittest
from selenium import webdriver
import time

class TestCaseLogin(unittest.TestCase):

    def test_01_login_success(self):
        driver = webdriver.Chrome(executable_path = "driver\chromedriver.exe")
        driver.maximize_window()
        driver.get("http://118.24.255.132:9090/shopxo/admin.php")

        driver.find_element_by_name('username').send_keys("admin")
        driver.find_element_by_name('login_pwd').send_keys("shopxo")
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/form/div/div[3]/button').click()

        time.sleep(5)
        e = driver.find_element_by_xpath('//*[@id="admin-offcanvas"]/div/ul/li[2]/a')
        assert e.text == '系统设置'

if __name__ == "__main__":
    unittest.main()
