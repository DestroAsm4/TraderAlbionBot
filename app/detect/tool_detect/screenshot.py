import win32gui
import win32ui
import win32con
import numpy as np

from matplotlib import pyplot as plt
from cv2 import getTickCount, getTickFrequency
import PIL, numpy

from app.setting import WindowName

class ScreenClass:

    def __init__(self, title_of_window):
        self.title_of_window = title_of_window

    def getScreenShot(self, title_of_window):

        hwnd = win32gui.FindWindow(None, self.title_of_window)
        wDC = win32gui.GetWindowDC(hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        dataBitMap = win32ui.CreateBitmap()
        rect = np.array(list(win32gui.GetWindowRect(hwnd)))
        w, h = tuple(rect[2:] - rect[0:2])
        dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
        cDC = dcObj.CreateCompatibleDC()
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)
        bmpinfo = dataBitMap.GetInfo()
        bmpstr = dataBitMap.GetBitmapBits(True)
        img = np.array(PIL.Image.frombuffer('RGB', (bmpinfo['bmWidth'], bmpinfo['bmHeight']), bmpstr, 'raw', 'BGRX', 0, 1))
        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        return img

    def get_and_show_screen(self):
        import cv2 as cv
        img = self.getScreenShot(self.title_of_window)
        while True:

            cv.imshow('Matches', img)
            if cv.waitKey(1) == ord('q'):
                cv.destroyAllWindows()
                break

    def get_and_show_screen_alter(self):

        img = self.getScreenShot(self.title_of_window)
        plt.imshow(img)
        plt.show()


# t0 = getTickCount()
screen_instance = ScreenClass(WindowName.mainwindow)
# t1 = getTickCount()
# print((t1 - t0) / getTickFrequency())
screen_instance.get_and_show_screen_alter()
    # cv2.imshow('Matches', img)
    # if cv2.waitKey(1) == ord('q'):
    #     cv2.destroyAllWindows()
    #     break