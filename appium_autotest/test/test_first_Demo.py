from appium import webdriver

'''
1、通过appium连接模拟器或手机，需要连接参数，
2、连接appium
3、直接在手机查找元素执行操作。（定位操作-xpath，id）
'''
import time
des = {
        "platformName": "android",
        'platformVersion': '7.1.2',  # 版本号
        'deviceName': '127.0.0.1:62001',  # 设备名称
        'app': './youdaonote_android_6.7.18_youdaoweb.apk',
        "noReset": True
    }
# appium远程连接（地址，模拟器信息）
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)
# 通过appium生成的脚本代码
el1 = driver.find_element_by_accessibility_id("Accessibility")
el1.click()
el2 = driver.find_element_by_accessibility_id("Accessibility Node Querying")
el2.click()

time.sleep(5)
driver.close()