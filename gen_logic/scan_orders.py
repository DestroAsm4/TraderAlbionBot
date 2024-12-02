import re
import time
from typing import Literal

import win32gui

from active.cliker import Clicker
from bd.manage_bd import ManageBD
from detect.tool_detect.detect import Detect
from detect.tool_detect.reader import Reader
from setting import Pathes, GameName, ActiveText, XYText, XYWHOrderBuy, Order_data


class ScanOrders:

    def __init__(self, play: bool = False, mod: str = 'test_data'):
        self.detecter_red_button = Detect(Pathes.red_button, coef_match=0.8, options='red_button')
        self.detecter_next_page_button = Detect(Pathes.next_page_order, coef_match=0.98) # 0.9 два 0,98 только нужное
        if play:
            self.gamename = GameName.albion
            self.focus_game()
        self.clicker = Clicker()

        self.reader = Reader(mod=mod)
        self.data_order = Order_data
        self.manage_bd = ManageBD()
        self.all_numbers = []
        self.numbers_100 = False

    def focus_game(self, gamename=None):
        if gamename:
            self.gamename = gamename
        hwnd = win32gui.FindWindow(None, self.gamename)
        win32gui.SetForegroundWindow(hwnd)

    def t_read(self, x_y):
        self.reader.read_text(x_y)

    def read_number_item(self, points):
        if self.all_numbers:
            if self.all_numbers[-1] == 99 or self.all_numbers[-1] > 99:
                self.numbers_100 = True

        if not self.numbers_100:
            points_number = ActiveText.number_item_order(points)
        else:
            points_number = ActiveText.number_item_order_100(points)

        while True:
            number_item = self.reader.read_text(points_number, config='number_item')
            # print(number_item.strip())
            # print(number_item)
            number_item = re.findall(r'\d+', number_item)

            if number_item:
                number_item = number_item[0]
                break
        return number_item

    def read_data_scroll(self, points) -> dict:
        while True:
            count_item = self.reader.read_text(ActiveText.count_item_order(points), config='count_order')
            print(count_item)
            count_item = re.findall(r'\d+', count_item)
            if count_item:
                count_item = count_item[0]
                break
        number_item = self.read_number_item(points)



        return {
            # 'name': name,
            'count': count_item,
            'naumber': number_item
        }

    def read_data_item(self):
        name_item = self.reader.read_text(XYText.name_item, config='name_item')
        while True:
            level_item = self.reader.read_text(XYText.level_item)
            level_item = re.findall(r'\d+', level_item)
            if level_item:
                level_item = level_item[0]
                break
        while True:
            char_item = self.reader.read_text(XYText.char_item, config='char_item')
            # print(char_item)
            char_item = char_item.lower().strip()
            char_item = char_item.replace('о', '0')
            char_item = re.findall(r'\d+', char_item)
            if char_item:
                char_item = char_item[0]
                break
        while True:
        # print('запись', char_item)
            price_item = self.reader.read_text(XYText.price_item, config='price_item')
        # print(price_item)
            if ',' in price_item:
                price_item = price_item.replace(',', '')
                price_item = re.findall(r'\d+', price_item)
                if price_item:
                    price_item = price_item[0]
                    break
            else:
                price_item = re.findall(r'\d+', price_item)
                if price_item:
                    price_item = price_item[0]
                    break
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

    def t_scan(self, mod: Literal['save'] = None):
        gen_res = []
        # points = self.detect.detect()
        # points = self.get_buy_orders(points, mod='buy_orders')
        end = False
        new_numbers_scroll = set()
        old_nubers_scroll = set()


        # points#
        while end == False:
            #получение координат объектов
            time.sleep(0.3)
            points = self.detecter_red_button.detect()
            points = self.get_buy_orders(points, mod='buy_orders')


            #перебор объектов
            for i in points:
                #получние первичных данных объекта
                time.sleep(1)
                res_scroll = self.read_data_scroll(i)
                number = int(res_scroll['naumber'])

                #запись объектов одного скрола
                new_numbers_scroll.add(number)

                if number not in self.all_numbers:
                    #проверка счетчика
                    #действие
                    self.clicker.active_click_red_button(i[0], i[1])
                    time.sleep(0.3)
                    res_item = self.read_data_item()
                    time.sleep(0.5)
                    res_item['count'] = res_scroll['count']
                    res_item['naumber'] = number
                    print(res_item)
                    gen_res.append(res_item)

                else:
                    continue

                self.all_numbers.append(number)


            if self.all_numbers[-1] % 50 == 0:
                self.clicker.next_page()
                time.sleep(0.3)
                old_nubers_scroll = new_numbers_scroll
                new_numbers_scroll = set()
                if mod == 'save':
                    self.add_bd_orders(gen_res)
                    gen_res = []
                continue
            elif new_numbers_scroll == old_nubers_scroll:
                if mod == 'save':
                    self.add_bd_orders(gen_res)
                break

            old_nubers_scroll = new_numbers_scroll
            new_numbers_scroll = set()
            self.clicker.scroll_order_buy()
        return gen_res
        # res = list(res)
        # for i in gen_res:
        #     print(i)


        # print(res)
            # return res

    def next_page(self):
        while True:
            points = self.detecter_next_page_button.detect()
            # print(points)
            if points:
                self.clicker.next_page()
            else:
                break


    def scan(self):
        points = self.detecter_red_button.detect()
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

    def add_bd_orders(self, data_order: list[dict]):
        '''
        'name': name_item.strip().lower(),
            'level': level_item,
            'char': char_item,
            'price_gen': price_item,
            'min_sell': min_sell,
            'max_buy': max_buy
        '''
        for order in data_order:
            self.data_order.name = order['name']
            self.data_order.level = order['level']
            self.data_order.char = order['char']
            self.data_order.price_gen = order['price_gen']
            self.data_order.min_sell = order['min_sell']
            self.data_order.max_buy = order['max_buy']
            self.data_order.count = order['count']

            self.manage_bd.new_t_data_order(self.data_order)



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
    # char_item = scan_test.reader.read_text(XYText.char_item, config='char_item')
    # print(char_item)
    # scan_test.reader.read_text(ActiveText.count_item_order(points), config='count_order')
    gen_res = scan_test.t_scan(mod='save')
    # scan_test.add_bd_orders(gen_res)
    # scan_test = ScanOrders(play=True)
    # Clicker.scroll_order_buy()
    # scan_test = ScanOrders(play=True, mod='test_img')
    # scan_test.t_read(XYText.min_sell)