import pyautogui


class Clicker:

    @classmethod
    def scroll_order_buy(cls):
        pyautogui.moveTo(968, 508, duration=0.3)
        pyautogui.mouseDown()

        pyautogui.moveTo(974, 404, duration=0.3)
        pyautogui.mouseUp()

    @classmethod
    def active_click_mail(cls, x, y):
        pyautogui.moveTo(x - 25, y + 15, duration=0.3)
        pyautogui.click()

    @classmethod
    def active_click_close_mail(cls):
        pyautogui.moveTo(1149, 211, duration=0.3)
        pyautogui.click()

    @classmethod
    def next_page(cls):
        pyautogui.moveTo(992, 583, duration=0.3)
        pyautogui.click()

    @classmethod
    def mail_ind(cls):
        pyautogui.moveTo(1496, 29)
        pyautogui.click()

    @classmethod
    def close_item(cls):
        pyautogui.moveTo(940, 313, duration=0.3)
        pyautogui.click()

    @classmethod
    def active_click_red_button(cls, x, y):
        pyautogui.moveTo(x, y, duration=0.3)
        pyautogui.click()

