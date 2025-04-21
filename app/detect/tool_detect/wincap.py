import time
from ctypes import windll
import cv2 as cv
import numpy as np
import win32gui, win32ui, win32con

from app.setting import WindowName


class WindowCapture:

    # properties
    w = 1920
    h = 1080
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0

    # constructor
    def __init__(self, window_name = WindowName.steam):

        # find the handle for the window we want to capture
        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception('Window not found: {}'.format(window_name))
        self._get_windows_size()



    def screen_windows(self):
        # self._get_windows_size()
        start_time = time.time()
        windll.user32.SetProcessDPIAware() # DPI - количество точек на дюим изображения
        # Пользователь может выставить масштаб отличный от 100% в настройках экрана. Вызывая эту функцию
        # (SetProcessDPIAware), вы сообщаете системе, что интерфейс вашего приложения умеет сам правильно
        # масштабироваться при высоких значениях DPI (точки на дюйм). Если вы не выставите этот флаг, то интерфейс вашего
        # приложения может выглядеть размыто при высоких значениях DPI.

        # get the window image data
        wDC = win32gui.GetWindowDC(self.hwnd)
        # int = GetWindowDC(hWnd)
        # возвращает контекст устройства (DC) для всего окна, включая строку заголовка, меню и полосы прокрутки.
        # hWnd : int ручка окна
        # DC (Drawing Context)
        # или Device Context
        # Если параметр равен NULL, то функция извлекает контекст устройства для всего экрана.
        """
        Дескриптор контекста устройства (HDC) — это идентификатор структуры данных, 
        связанной с конкретным устройством вывода информации (принтер, дисплей) в графическом интерфейсе Windows (GDI).  12
        
        Контекст устройства содержит информацию о параметрах и атрибутах вывода графики на устройство, в частности:
        
        палитру устройства, определяющую набор доступных цветов; 3
        параметры пера для черчения линий; 3
        параметры кисти для закраски и заливки; 3
        параметры шрифта, использующегося для вывода текста. 3
        Получить дескриптор контекста устройства можно с помощью функции GetDC для клиентской области указанного окна или всего экрана
        """

        dcObj = win32ui.CreateDCFromHandle(wDC)
        # функция, которая создаёт объект DC (Device Context) на основе целочисленного дескриптора
        cDC = dcObj.CreateCompatibleDC()
        # dcObj.CreateCompatibleDC() Функция используется для создания совместимого графического контекста (cDC) на основе объекта dcObj
        dataBitMap = win32ui.CreateBitmap()
        '''
        win32ui.CreateBitmap() — функция, которая создаёт объект битового изображения (bitmap).  25

        Также существует функция win32ui.CreateBitmapFromHandle(), которая создаёт объект битового изображения из HBITMAP.
        '''
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)

        # If Special K is running, this number is 3. If not, 1
        result = windll.user32.PrintWindow(self.hwnd, cDC.GetSafeHdc(), 3)

        bmpinfo = dataBitMap.GetInfo()
        bmpstr = dataBitMap.GetBitmapBits(True)

        img = np.frombuffer(bmpstr, dtype=np.uint8).reshape((bmpinfo["bmHeight"], bmpinfo["bmWidth"], 4))
        img = np.ascontiguousarray(img)[..., :-1]  # make image C_CONTIGUOUS and drop alpha channel

        if not result:  # result should be 1
            win32gui.DeleteObject(dataBitMap.GetHandle())
            cDC.DeleteDC()
            dcObj.DeleteDC()
            win32gui.ReleaseDC(self.hwnd, wDC)
            raise RuntimeError(f"Unable to acquire screenshot! Result: {result}")
        end_time = time.time()  # время окончания выполнения
        execution_time = end_time - start_time
        print(execution_time)

        return img

    def _get_windows_size(self):
        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]

        # account for the window border and titlebar and cut them off
        border_pixels = 1
        titlebar_pixels = 10
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

        # set the cropped coordinates offset so we can translate screenshot
        # images into actual screen positions
        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y


    @staticmethod
    def list_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)




if __name__ == '__main__':
    # WindowCapture().list_window_names()
    wincap = WindowCapture(WindowName.mainwindow)


    # while True:
    img = wincap.screen_windows()
    print(img)
        # img = cv.imread(img, cv.IMREAD_UNCHANGED)
        # cv.imshow('Matches', img)
        # if cv.waitKey(1) == ord('q'):
        #     cv.destroyAllWindows()
        #     break
