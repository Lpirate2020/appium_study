from appium import webdriver

'''
1、通过appium连接模拟器或手机，需要连接参数，
2、连接appium
3、直接在手机查找元素执行操作。（定位操作-xpath，id）
'''
import time
des = {
    'platformName':'Android',
    # android版本号
    # 'platformVersion':'6.0',

    # adb devices返回的值
    'deviceName':'127.0.0.1:62001',
    'appPackage':'com.youdao.calculator',
    'appActivity':'.activities.GuideActivity'

    # 先安装再打开
    # 'app':'E:\untitled1\appium_autotest\test\youdaonote_android_6.7.18_youdaoweb.apk'
}
# appium远程连接（地址，模拟器信息）
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)
# 滑动三次  最后是500毫秒
driver.swipe(800,500,50,500,500)
driver.swipe(800,500,50,500,500)
driver.swipe(800,500,50,500,500)
el1 = driver.find_element_by_id("com.youdao.calculator:id/guide_button")
el1.click()
time.sleep(2)

seven=driver.find_element_by_id("com.youdao.calculator:id/iv_icon")
seven.click()
seven.click()
seven.click()
seven.click()
seven.click()

el1 = driver.find_element_by_xpath("//android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout[7]/android.widget.FrameLayout/android.widget.ImageView")
el1.click()
el2 = driver.find_element_by_xpath("//android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout[20]/android.widget.FrameLayout/android.widget.ImageView")
el2.click()
el3 = driver.find_element_by_xpath("//android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout[8]/android.widget.FrameLayout/android.widget.ImageView")
el3.click()
el4 = driver.find_element_by_xpath("//android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.view.ViewGroup/android.widget.GridView/android.widget.FrameLayout[25]/android.widget.FrameLayout/android.widget.ImageView")
el4.click()

time.sleep(5)
driver.close_app()