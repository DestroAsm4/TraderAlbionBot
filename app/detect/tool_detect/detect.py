from typing import Literal

import pytesseract
import win32gui
from PIL import Image



import cv2 as cv

from app.detect.tool_detect.detect import Vision
from app.detect.tool_detect.wincap import WindowCapture
from app.setting import GameName


class Detect:
    '''
    основные функции detect и read_text
    '''

    def __init__(self,
                 object_detect_img_path=None,
                 mod: Literal['rectangles', 'points', 'play']=None,
                 coef_match: float = 0.6,
                 options: Literal['mail_ind', 'not_read_mail', 'red_button']=None):


        self.gamename = GameName.albion
        self.mod = mod
        self.coef_match = coef_match
        self.options = options

        self.wincap = WindowCapture(self.gamename)

        if options == 'mail_ind':
            self.coef_match = 0.84

        if options == 'not_read_mail':
            self.coef_match = 0.8

        if self.options == 'red_button':
            self.object_detecter = Vision(needle_img_path=object_detect_img_path)
        else:
            self.object_detecter = Vision(object_detect_img_path)

        if mod == 'play':
            self.focus_game()

    def read_text(self, x_y_text: tuple, config: Literal['mail_ind']=None) -> str:



        img = self.wincap.capture_win_alt()

        # filename = r'D:\cods\python\my_pet\albion_bot\textreader\screenshots\new.png'
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        im = Image.fromarray(img, mode='RGB')
        crop_rectangle = x_y_text
        cropped_im = im.crop(crop_rectangle)

        if self.mod:
            cropped_im.show()



        lang = 'eng+rus'
        config = '--oem 3 --psm 13'

        if config == 'mail_ind':

            # psm 4 11 12
            lang = 'eng+rus'
            config = '--oem 3 --psm 12'


        text = pytesseract.image_to_string(cropped_im, lang=lang, config=config)


        return text

    def detect(self):

        img = self.wincap.capture_win_alt()
        points = self.object_detecter.find(img, self.coef_match, self.mod)

        return points



    def loop_detect(self, mod: Literal['print', 'vision']=None):

        while True:
            self.detect()
            if mod == 'print':
                print(self.detect())

            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break


    @classmethod
    def focus_game(self, gamename):
        hwnd = win32gui.FindWindow(None, gamename)
        win32gui.SetForegroundWindow(hwnd)


#coef_match=0.83 видит 0.849 не видит
# detecter = Detect(Pathes.not_read_mail, mod='points', coef_match=0.8)
# detecter.loop_detect()
# while True:
#     res = detecter.read_text(XYText.mail_ind, config='mail_ind')
#     print(Parser.mail_ind(res))
# print(res)

if __name__ == '__main__':
    pass