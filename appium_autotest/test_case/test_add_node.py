import pytest
from page import ok_page
from page import note_operate
from page import locators


class TestAddNode(object):
    # pytest测试类初始化使用fixture
    @pytest.fixture(scope='module', autouse=True)
    def driver(self, run_app):
        self.driver = run_app
        # 因为 存在Basepage原因，先加载的是页面，传入driver
        # 之后再调用的方式
        ok = ok_page.OkPage(self.driver)
        ok.btn_on()
        # 自动升级部分
        update = locators.app_update
        if update != '':
            ok.cancel()

    def test_add_note(self, run_app):
        add = note_operate.AddNote(run_app)
        add.create_note()
        add.enter_title("adbadb")
        run_app.press_keycode(33)
        run_app.press_keycode(34)
        add.submit_text()
