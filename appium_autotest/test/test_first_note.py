from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
    'unicodeKeyboard': True,
    'resetKeyboard': True,
    # adb devices返回的值
    'deviceName':'127.0.0.1:62001',
    'appPackage':'com.youdao.note',
    'appActivity':'.activity2.MainActivity'

    # 先安装再打开
    # 'app':'E:\untitled1\appium_autotest\test\youdaonote_android_6.7.18_youdaoweb.apk'
}
# appium远程连接（地址，模拟器信息）
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)
# 加延时防止点的太快报错
time.sleep(2)

# 等待    死等time.sleep(3)     智能等待driver.implicitly_wait(30)
driver.implicitly_wait(30)

# 封装起来，和下面功能一样
elm = (MobileBy.ID,"com.youdao.note:id/btn_ok")
driver.find_element(*elm).click()
# driver.find_element_by_id("com.youdao.note:id/btn_ok").click()
# time.sleep(2)

# 提示的更新和广告
# driver.find_element_by_id("com.youdao.note:id/btn_cancel").click()
# time.sleep(2)
# el2 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView[2]")
# el2.click()

driver.find_element_by_id("com.youdao.note:id/add_note").click()
time.sleep(2)
driver.find_element_by_id("com.youdao.note:id/add_note_floater_add_note").click()
time.sleep(2)
driver.find_element_by_id("com.youdao.note:id/note_title").send_keys("日记标题")
time.sleep(4)

# 下面写内容不好使
# driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View[1]/android.view.View/android.view.View").send_keys("今天心情不错，打算吃100个饺子")
# driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.EditText").send_keys("sjlfsflds")
# time.sleep(4)
# 用另一种方式写内容
# 回车
driver.press_keycode(66)
# tap模拟手指点击手机屏幕，[(x,y),(x1,y1)]
driver.tap([(70,396),(1105,468)],500)
# 字母e，f
driver.press_keycode(33)
driver.press_keycode(34)

ela = (MobileBy.ID,"com.youdao.note:id/actionbar_complete_text")
driver.find_element(*ela).click()
# 条件等待-显示等待
# if WebDriverWait(driver,10).until(EC.presence_of_element_located(add_node)):
#     driver.find_element(*add_node).seed_keys("32456789")
