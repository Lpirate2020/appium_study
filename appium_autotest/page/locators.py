from appium.webdriver.common.mobileby import MobileBy

# 原地址
# class Locators(object):
#     btn_ok = (MobileBy.ID, "com.youdao.note:id/btn_ok")
#     btn_cancel = (MobileBy.ID, "com.youdao.note:id/btn_cancel")
#     hierarchy = (MobileBy.XPATH,
#                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ImageView[2]")
#
#     add_node = (MobileBy.ID, "com.youdao.note:id/add_note")
#     add_note_floater_add_note = (MobileBy.ID, "com.youdao.note:id/add_note_floater_add_note")
#     note_title = (MobileBy.ID, "com.youdao.note:id/note_title")
#
#     actionbar_complete_text = (MobileBy.ID, "com.youdao.note:id/actionbar_complete_text")
#
#     close1=(MobileBy.ID,'com.youdao.note:id/close')

from appium.webdriver.common.mobileby import MobileBy


class Locators(object):
    # 元素定位写在这里
    btn_ok_agree = (MobileBy.ID, "com.youdao.note:id/btn_ok")  # 同意地址
    btn_ok = (MobileBy.ID, "com.youdao.note:id/btn_ok")  # 同意地址
    permission_allow_button = (MobileBy.ID, "com.android.packageinstaller:id/permission_allow_button")
    # 京东
    add_note = (MobileBy.ID, "com.youdao.note:id/add_note")
    add_icon = (MobileBy.ID, "com.youdao.note:id/add_icon")
    note_title = (MobileBy.ID, "com.youdao.note:id/note_title")
    # 更新提示
    app_update = (MobileBy.ID, "com.youdao.note:id/btn_cancel")
    actionbar_complete_text = (MobileBy.ID, "com.youdao.note:id/actionbar_complete_text")
