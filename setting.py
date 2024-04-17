from dataclasses import dataclass

import datetime as datetime


SELL_PERCENT = 2.5

@dataclass
class Pathes:

    # button_order_buy: str = r'D:\cods\python\my_pet\albion_bot\gendata\detect\screenshot\needle_img\order_buy_button.jpg'
    mail: str = r'D:\cods\python\my_pet\albion_bot\gendata\detect\screenshot\needle_img\mail.jpg'
    market: str = r'D:\cods\python\my_pet\albion_bot\gendata\detect\screenshot\needle_img\market.jpg'
    mail_ind: str = r'D:\cods\python\my_pet\albion_bot\gendata\detect\screenshot\needle_img\mail_ind.jpg'
    not_read_mail: str = r'D:\cods\python\my_pet\albion_bot\gendata\detect\screenshot\needle_img\not_read_mail.jpg'
    red_button: str = r'D:\cods\python\my_pet\albion_bot\gendata\detect\screenshot\needle_img\red_button.jpg'
    next_page_order: str = r'D:\cods\python\my_pet\TraderAlbionBot\detect\screenshot\needle_img\next_page_order.jpg'


@dataclass
class GameName:
    albion: str = r'Albion Online Client'


#при окне на весь экран без рамки, x_y для определения подхиодит иделально

@dataclass
class XYText:
    name_item: tuple = (540, 304, 905, 335)
    minpricebuy: tuple = (1030, 325, 1140, 345)
    mail_ind: tuple = (1505, 5, 1525, 20)
    mail_text: tuple = (790, 526, 1102, 631)
    time_trade: tuple = (796, 409, 1020, 425)
    is_trade_mail: tuple = (876, 375, 1020, 396)
    level_item: tuple = (514, 394, 529, 409)
    char_item: tuple = (700, 396, 716, 409)
    price_item: tuple = (567, 724, 722, 743)
    min_sell: tuple = (1018, 370, 1098, 386)
    max_buy: tuple = (1260, 369, 1365, 386)


class ActiveText:

    @staticmethod
    def count_item_order(x_y: tuple):
        x1 = x_y[0] - 380
        x2 = x_y[0] - 335
        y1 = x_y[1] - 20
        y2 = x_y[1] + 20
        return (x1, y1, x2, y2)

    @staticmethod
    def number_item_order(x_y: tuple):
        x1 = x_y[0] - 640
        x2 = x_y[0] - 620
        y1 = x_y[1] - 10
        y2 = x_y[1] + 10
        return (x1, y1, x2, y2)

    @staticmethod
    def name_item_order(x_y: tuple):
        x1 = x_y[0] - 540
        x2 = x_y[0] - 388
        y1 = x_y[1] - 20
        y2 = x_y[1] + 20
        return (x1, y1, x2, y2)

@dataclass
class Mail_data:

    name: str
    active: str
    city: str
    count: int
    level_item_name: str
    price_one: int
    price_gen: int
    datetime: datetime.datetime
    processed: bool

@dataclass
class BaseXYWH:
    x: int
    y: int
    w: int
    h: int


@dataclass
class XYWHOrderBuy(BaseXYWH):
    x: int = 576
    y: int = 387
    w: int = 771
    h: int = 207