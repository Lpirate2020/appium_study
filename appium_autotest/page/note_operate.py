from .base_page import BasePage
from .locators import Locators


class AddNote(BasePage):
    def create_note(self):
        BasePage.click_operate(self, Locators.add_note)
        BasePage.click_operate(self, Locators.add_icon)


    def enter_title(self, text):
        BasePage.send_enter(self, Locators.note_title, text)

    def submit_text(self):
        BasePage.click_operate(self, Locators.actionbar_complete_text)

    def result_title(self):
        pass


class DeleteNote(BasePage):
    pass
