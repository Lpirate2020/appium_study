from appium import webdriver
import pytest


@pytest.fixture(scope='session')
def run_app(request):
    des = {
        "platformName": "android",
        'platformVersion': '7.1.2',  # 版本号
        'deviceName': '127.0.0.1:62001',  # 设备名称
        'unicodeKeyboard': True,
        'resetKeyboard': True,
        'appPackage': 'com.youdao.note',
        'appActivity': '.activity2.MainActivity'
        # 'appPackage': 'com.youdao.note',
        # 'appActivity': '.activity2.MainActivity',

        # 'app': 'E:\\1 学习\\4大四上\\课设\\测试部分\\2020-11-10\\测试apk\\youdaonote_android_6.7.18_youdaoweb.apk',
        # "noReset": True

    }
    # appium远程连接（地址，模拟器信息）
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", des)

    def close_app():
        driver.quit()

    request.addfinalizer(close_app)
    return driver
