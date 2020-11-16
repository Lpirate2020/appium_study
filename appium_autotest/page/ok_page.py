from .base_page import BasePage
from .locators import Locators


class OkPage(BasePage):
    def btn_on(self):
        BasePage.click_operate(self, Locators.btn_ok)

    def close1(self):
        BasePage.click_operate(self, Locators.btn_ok)

    # 拒绝升级
    def cancel(self):
        BasePage.click_operate(self, Locators.app_update)
