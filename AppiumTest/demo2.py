
# 1.导入appium的webdriver
from appium import webdriver
import time 

# 1. 启动软件，获取到手机的句柄
desired_caps = {}
desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '7.1.2'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'V1938CT'                # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'io.appium.android.apis'               # app的名字：就是包名package
                                                        # 安卓8.1之前：adb shell dumpsys activity | findstr "mFocusedActivity"
                                                        # 安卓8.1之后：adb shell dumpsys activity | findstr "mResume"
desired_caps['appActivity'] = '.ApiDemos'              # 同上↑  app的id: 就是 activity
desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘
desired_caps['noReset'] = True                        # 使用app的缓存
# 去打开app，并且返回当前app的操作对象
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 元素定位
# accessibility id
# driver.find_element_by_accessibility_id('App').click()
driver.find_element_by_android_uiautomator('new UiSelector().text("App")').click()


# xpath
driver.find_element_by_xpath('//android.widget.TextView[@content-desc="Search"]').click()


driver.find_element_by_accessibility_id('Invoke Search').click()
# id定位
driver.find_element_by_id('io.appium.android.apis:id/txt_query_prefill').send_keys("测试人加油")
