import re
from typing import Literal

import datetime as datetime

from app.bd.manage_bd import ManageBD
from app.detect.tool_detect.reader import Reader
from app.detect.tool_detect.wincap import WindowCapture
from app.setting import GameName, Mail_data, XYText


class ScanMail:

    def __init__(self, mod: Literal['test_img', 'test_data']=None):
        self.gamename = GameName.albion
        self.mod = mod
        self.wincap = WindowCapture(self.gamename)
        self.manag_bd = ManageBD()
        self.mail_data = Mail_data
        self.config = None
        self.reader = Reader()

    @staticmethod
    def is_float(string):
        try:
            if ',' in string:
                string = string.replace(',', '.')
            return float(string) and '.' in string  # True if string is a number contains a dot
        except ValueError:  # String is not a number
            return False


    def genmail(self):
        x_y_text = XYText.mail_text
        base_text = self.reader.read_text(x_y_text, config='read_mail')
        # text = re.findall(r'[А-ЯA-Z]+', text)
        base_split_text = base_text.split()
        text = base_split_text.copy()
        #active
        active = text[1]
        if 'прод' in active:
            active = 'sell'
        elif 'купи' in active:
            active = 'buy'
        del text[:2]
        #name
        start_name_id = [i for i in range(len(text)) if len(text[i]) > 2][0]
        del text[:start_name_id]
        if ')' in base_text and '(' in base_text:
            end_name_id = [i + 1 for i in range(len(text)) if ')' in text[i]][0]
        else:
            end_name_id = [i for i in range(len(text)) if text[i].strip() == 'в'][0]

        name_list = text[:end_name_id]
        name = ' '.join(name_list)
        name = name.lower()
        # print(text, end_name_id + 1)
        del text[:end_name_id + 1]

        #city

        city = text[0]
        city = city.lower()

        #price gen
        id_prices = [i + 1 for i in range(len(text)) if 'слож' in text[i]][0]

        # print(text[id_prices])
        price_gen = text[id_prices]
        if ',' in price_gen or '.' in price_gen:
            price_gen = int(price_gen.replace(',', ''))
        else:
            price_gen = int(price_gen)

        del text[:id_prices]


        #price one
        id_prices = [i + 1 for i in range(len(text)) if 'запл' in text[i] or 'получ' in text[i]][0]
        price_one = text[id_prices]
        if ',' in price_one or '.' in price_one:
            price_one = int(price_one.replace(',', ''))
        else:
            price_one = int(price_one)
        #count items
        count_item = round(price_gen / price_one)
        if ')' in name and '(' in name:
            level_item_name = re.findall(r'\((.+?)\)', name)[0]
            level_item_name = level_item_name.lower()
        else:
            level_item_name = 'без уровня'


        # return base_split_text

        return {
            'name': name,
            'active': active,
            'city': city,
            'count': count_item,
            'level_item_name': level_item_name,
            'price_one': price_one,
            'price_gen': price_gen
        }



    def head_mail(self):
        x_y_text = XYText.time_trade
        base_text = self.reader.read_text(x_y_text, config='read_mail')
        text = base_text.split()
        full_data = text[1].split('.')
        date = {
            'day': int(full_data[0]),
            'month': int(full_data[1]),
            'year': int(full_data[2])
        }
        time_list = text[2].split(':')
        time = {
            'hour': int(time_list[0]),
            'minut': int(time_list[1])
        }
        return {
            'date': date,
            'time': time
        }




    def is_trade_mail(self):
        x_y_text = XYText.is_trade_mail
        base_text = self.reader.read_text(x_y_text, config='read_mail')
        base_text = base_text.lower()
        if 'прод' in base_text or 'купи' in base_text:
            return True
        else:
            return False



    def mail(self):
        if not self.is_trade_mail():
            print('Это не торговое письмо')
            return 'Это не торговое письмо'
        res_head = self.head_mail()
        res_gen = self.genmail()
        res_mail = {**res_gen, **res_head}

        self.mail_data.name = res_mail['name']
        self.mail_data.active = res_mail['active']
        self.mail_data.city = res_mail['city']
        self.mail_data.count = res_mail['count']
        self.mail_data.level_item_name = res_mail['level_item_name']
        self.mail_data.price_one = res_mail['price_one']
        self.mail_data.price_gen = res_mail['price_gen']
        self.mail_data.datetime = datetime.datetime(res_mail['date']['year'], res_mail['date']['month'],
                                                    res_mail['date']['day'], hour=res_mail['time']['hour'],
                                                    minute=res_mail['time']['minut'])
        self.mail_data.processed = False

        if self.mod == 'test_data':
            print(1, self.mail_data)

        self.data_mail_to_bd()


    def data_mail_to_bd(self):
        self.manag_bd.new_data_mail(self.mail_data)







if __name__=='__main__':

    reader = ScanMail()
    reader.mail()
    reader.data_mail_to_bd()
    # reader.data_mail_to_bd()
