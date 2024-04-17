import re
import time
from typing import Literal

import win32gui

from active.cliker import Clicker
from detect.tool_detect.detect import Detect
from detect.tool_detect.reader import Reader
from setting import Pathes, GameName, ActiveText, XYText, XYWHOrderBuy


class ScanOrders:

    def __init__(self, play: bool = False, mod: str = 'test_data'):
        self.detect_red_button = Detect(Pathes.red_button, coef_match=0.8, options='red_button')
        self.detect_next_page = Detect(Pathes.next_page_order, coef_match=0.98) # 0.9 два 0,98 только нужное
        if play:
            self.gamename = GameName.albion
            self.focus_game()
        self.clicker = Clicker()

        self.reader = Reader(mod=mod)

    def focus_game(self, gamename=None):
        if gamename:
            self.gamename = gamename
        hwnd = win32gui.FindWindow(None, self.gamename)
        win32gui.SetForegroundWindow(hwnd)

    def t_read(self, x_y):
        self.reader.read_text(x_y)

    def read_data_scroll(self, points) -> dict:
        count_item = self.reader.read_text(ActiveText.count_item_order(points), config='count_order')
        number_item = self.reader.read_text(ActiveText.number_item_order(points), config='count_order')
        # print(number_item.strip())
        number_item = re.findall(r'\d+', number_item)[0]
        # name = self.reader.read_text(ActiveText.name_item_order(points), config='name_order')
        # name = name.strip()
        # name = name.lower()
        # name = name.split()
        # name = [x.strip() for x in name]
        # name = ' '.join(name)
        # print(count_item)

        # print(name.strip())
        # print(count_item.strip())
        return {
            # 'name': name,
            'count': count_item.strip(),
            'naumber': number_item
        }

    def read_data_item(self):
        name_item = self.reader.read_text(XYText.name_item, config='name_item')
        level_item = self.reader.read_text(XYText.level_item)
        level_item = re.findall(r'\d+', level_item)
        if level_item:
            level_item = level_item[0]

        char_item = self.reader.read_text(XYText.char_item, config='char_item')
        char_item = char_item.lower().strip()
        char_item = char_item.replace('о', '0')

        char_item = re.findall(r'\d+', char_item)[0]
        # print('запись', char_item)
        price_item = self.reader.read_text(XYText.price_item, config='price_item')
        # print(price_item)
        if ',' in price_item:
            price_item = price_item.replace(',', '')
            price_item = re.findall(r'\d+', price_item)[0]
        else:
            price_item = re.findall(r'\d+', price_item)[0]
        min_sell = self.reader.read_text(XYText.min_sell, config='price_item')
        if ',' in min_sell:
            min_sell = min_sell.replace(',', '')
            min_sell = re.findall(r'\d+', min_sell)[0]
        else:
            min_sell = re.findall(r'\d+', min_sell)
            if min_sell:
                min_sell = min_sell[0]
            else:
                min_sell = 'Нет данных'
        max_buy = self.reader.read_text(XYText.max_buy, config='price_item')
        if ',' in max_buy:
            max_buy = max_buy.replace(',', '')
            max_buy = re.findall(r'\d+', max_buy)[0]
        else:
            max_buy = re.findall(r'\d+', max_buy)
            if max_buy:
                max_buy = max_buy[0]
            else:
                max_buy = 'Нет данных'



        res = {
            'name': name_item.strip().lower(),
            'level': level_item,
            'char': char_item,
            'price_gen': price_item,
            'min_sell': min_sell,
            'max_buy': max_buy
        }


        self.clicker.close_item()
        return res

    def t_scan(self):
        gen_res = []
        # points = self.detect.detect()
        # points = self.get_buy_orders(points, mod='buy_orders')
        end = False
        new_numbers_scroll = set()
        old_nubers_scroll = set()
        all_numbers = []

        # points#
        while end == False:
            #получение координат объектов
            time.sleep(0.3)
            points = self.detect_red_button.detect()
            points = self.get_buy_orders(points, mod='buy_orders')


            #перебор объектов
            for i in points:
                #получние первичных данных объекта
                time.sleep(0.3)
                res_scroll = self.read_data_scroll(i)
                number = int(res_scroll['naumber'])

                #запись объектов одного скрола
                new_numbers_scroll.add(number)

                if number not in all_numbers:
                    #проверка счетчика
                    print(number)
                    #действие
                    self.clicker.active_click_red_button(i[0], i[1])
                    time.sleep(0.3)
                    res_item = self.read_data_item()
                    time.sleep(0.5)
                    res_item['count'] = res_scroll['count']
                    print(res_item)
                    gen_res.append(res_item)

                else:
                    continue

                all_numbers.append(number)


            if all_numbers[-1] % 50 == 0:
                self.clicker.next_page()
                time.sleep(0.3)
                old_nubers_scroll = new_numbers_scroll
                new_numbers_scroll = set()
                continue
            elif new_numbers_scroll == old_nubers_scroll:
                break

            old_nubers_scroll = new_numbers_scroll
            new_numbers_scroll = set()
            self.clicker.scroll_order_buy()

        # res = list(res)
        # for i in gen_res:
        #     print(i)


        # print(res)
            # return res

    def next_page(self):
        while True:
            points = self.detect_next_page.detect()
            print(points)
            if points:
                self.clicker.next_page()
            else:
                break


    def scan(self):
        points = self.detect_red_button.detect()
        points = self.get_buy_orders(points, mod='buy_orders')
        res = []
        # print(points)
        # points#
        for i in points:
            time.sleep(0.3)
            res_scroll = self.read_data_scroll(i)
            self.clicker.active_click_red_button(i[0], i[1])
            time.sleep(0.3)
            res_item = self.read_data_item()
            res_item.update(res_scroll)
            res.append(res_item)
            print(res_item)
        return res

    def add_bd_orders(self):
        pass



    def get_buy_orders(self, points, mod: Literal['buy_orders']):
        if mod == 'buy_orders':
            x1 = XYWHOrderBuy.x
            x2 = x1 + XYWHOrderBuy.w
            y1 = XYWHOrderBuy.y
            y2 = y1 + XYWHOrderBuy.h
        res = []
        for i in points:
            if x1 < i[0] < x2 and y1 < i[1] < y2:
                res.append(i)
        return res




if __name__=='__main__':
    scan_test = ScanOrders(play=True)
    scan_test.t_scan()
    # scan_test = ScanOrders(play=True)
    # Clicker.scroll_order_buy()
    # scan_test = ScanOrders(play=True, mod='test_img')
    # scan_test.t_read(XYText.min_sell)