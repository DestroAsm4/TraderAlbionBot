from typing import Literal

import pytesseract
from PIL import Image
from detect.tool_detect.wincap import WindowCapture
from setting import GameName, Mail_data


class Reader:
    def __init__(self, mod: Literal['test_img', 'test_data']=None):
        self.gamename = GameName.albion
        self.mod = mod
        self.wincap = WindowCapture(self.gamename)
        self.mail_data = Mail_data
        self.config = None

    def read_text(self, x_y_text: tuple, config: Literal[
        'mail_ind', 'read_mail', 'count_order', 'name_order', 'char_item', 'name_order', 'name_item', 'price_item',
        'number_item' ] = None) -> str:

        img = self.wincap.capture_win_alt()

        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        im = Image.fromarray(img, mode='RGB')
        crop_rectangle = x_y_text
        cropped_im = im.crop(crop_rectangle)

        if self.mod == 'test_img':
            cropped_im.show()
        if config == 'read_mail':
            lang = 'eng+rus'
            config = '--oem 3 --psm 6'
        elif config == 'count_order':
            lang = 'eng'
            config = '--psm 7 --oem 3'
        elif config == 'name_order':
            lang = 'rus'
            config = '--oem 3 --psm 3'
        elif config == 'char_item':
            lang = 'rus'
            config = '--psm 10 --oem 3'
        elif config == 'name_item':
            lang = 'rus'
            config = '--psm 6 --oem 3'
        elif config == 'price_item':
            lang = 'rus'
            config = '--psm 7 --oem 3'
        elif config == 'number_item':
            lang = 'eng'
            config = '--psm 7 --oem 3'
        else:
            lang = 'rus'
            config = '--oem 3 --psm 7'

        text = pytesseract.image_to_string(cropped_im, lang=lang, config=config)

        return text