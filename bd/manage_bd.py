import sqlite3
from typing import Literal

from bd.data_setting import QueryParam

import os.path

from setting import Mail_data, Order_data





class ManageBD:

    def __init__(self, file_bd: str = 'datatrade'):

        self.file_bd = self.path_to(file_bd)
        self.cursor = None
        self.query = QueryParam

    def path_to(self, name):
        BASE_DIR = os.path.dirname(os.path.abspath(__name__))
        db_path = os.path.join(BASE_DIR, f"{name}.db")
        return db_path



    def _connect(self):
        self.cursor = sqlite3.connect(self.file_bd).cursor()
        return self.cursor

    def _save_close_con(self):
        self.cursor.commit()
        self.cursor.close()

    def _close_con(self):
        self.cursor.close()





    def create(self, active: Literal['buy_mail', 'sell_mail', 'order_sell', 'not_valid', 'valid_data']):

        cursor = self._connect()

        if active == 'buy_mail':
            cursor.execute(self.query.create_mail_buy())
        elif active == 'sell_mail':
            cursor.execute(self.query.create_mail_sell())
        elif active == 'order_sell':
            cursor.execute(self.query.create_order_sell())
        elif active == 'not_valid':
            cursor.execute(self.query.create_not_valid())
        elif active == 'valid_data':
            cursor.execute(self.query.create_valid())

        self._close_con()

    def get_table(self, name_table: Literal['test_order_sell', 'valid_data']) -> list:
        cursor = self._connect()
        sqlite_select_query = f"""SELECT * from {name_table}"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        cursor.close()
        return records



    def new_data_order(self, order_data: Order_data):

        cursor = self._connect()
        cursor.execute(self.query.new_data_order(order_data))
        self._save_close_con()

    def new_t_data_order(self, order_data: Order_data):
        cursor = self._connect()
        cursor.execute(self.query.new_t_data_order(order_data))
        self._save_close_con()

    def new_valid_data(self, name):
        cursor = self._connect()

        cursor.execute(self.query.new_valid(name))
        self._save_close_con()

    def new_data_mail(self, data_mail: Mail_data):

        cursor = self._connect()
        cursor.execute(self.query.new_mail(data_mail))
        self._save_close_con()

    def delete_all_rows(self, table_name):
        cursor = self._connect()
        cursor.execute(f'DELETE FROM `{table_name}`')
        self._save_close_con()

    def del_table(self, name_table: Literal['buy_mail', 'sell_mail', 'order_sell', 'not_valid', 'valid_data']):
        cursor = self._connect()
        cursor.execute(
            f'''
            DROP TABLE IF EXISTS {name_table}
            '''
            )
        self._close_con()


    def agree_valid(self, data):
        order_data = Order_data
        order_data.name = data[1]
        order_data.level = data[2]
        order_data.char = data[3]
        order_data.price_gen = data[4]
        order_data.min_sell = data[5]
        order_data.max_buy = data[6]
        order_data.count = data[7]
        self.new_data_order(order_data)

    def valid_order_data(self):
        print('проверка данных')
        datas = self.get_table('test_order_sell')
        valids = self.get_table('valid_data')
        valids_name = [x[1] for x in valids]
        print(valids_name)
        for i in datas:
            print(i)
            print('проверка в валидах, если есть выполнить запись и континуе')
            if i[1] in valids_name:
                self.agree_valid(i)
                continue
            while True:
                answer = input('y/n: ')
                if answer not in ['y', 'n']:
                    print('не корректный ответ')
                    continue
                elif answer == 'y':
                    print('запись в основу')
                    print('если нет в валидах, то запись в валидные данные')
                    self.agree_valid(i)
                    self.new_valid_data(i[1])
                    break
                elif answer == 'n':
                    print('запись номера плохой записи')
                    break


if __name__=='__main__':
    order_bd = ManageBD()

# order_bd.delete_all_rows('order_sell')
# datas = order_bd.valid_order_data()

# order_bd.del_table('order_sell')
# order_bd.deleteall('order_sell')
#
# mail_bd.set_name_table('buy_mail_table')
#
# mail_bd.create_db_and_table()