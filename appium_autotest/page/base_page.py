from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from appium.webdriver.webdriver import WebDriver


class BasePage(object):
    # 在这里写公共的方法
    # click,sendkey，滑动，截图，
    def __init__(self, driver):
        # WebDriver是driver的类型，因为现在没有创建之个方法，所以点不出来，需要把类型加上才可以
        self.driver: WebDriver = driver
        logging.info("初始化手机")

    # 点击
    def click_operate(self, locator):
        if WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)):
            self.driver.find_element(*locator).click()
        else:
            logging.info("没找到元素，无法点击")

    # 发送写入信息
    def send_enter(self, locator, text):
        if WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator)):
            self.driver.find_element(*locator).send_keys(text)
        else:
            logging.info("没找到元素，无法输入")

    # 向左划
    def swipe_left(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        self.driver.swipe(width * 9 / 10, height / 2, width / 10, height / 2, 500)
