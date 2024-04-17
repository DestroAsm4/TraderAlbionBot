import sqlite3



import os.path

from setting import Mail_data


def path_to(name):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, f"{name}.db")
    return db_path


class ManageBD:

    def __init__(self, file_bd: str = 'datatrade'):

        self.file_bd = path_to(file_bd)
        self.connection = None

    def set_name_table(self, name_table: str):
        self.name_table = name_table

    def con(self):
        self.connection = sqlite3.connect(self.file_bd)

    def get_table(self):
        self.con()
        cursor = self.connection.cursor()
        sqlite_select_query = f"""SELECT * from {self.name_table}"""
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        print(records)

        cursor.close()
        # return data

    def create_db_and_table_order(self, name_table):

        # Создаем подключение к базе данных (файл my_database.db будет создан)
        #'count': count_item.strip()
        # 'name': name_item.strip().lower(),
        # 'level': level_item,
        # 'char': char_item,
        # 'price_gen': price_item,
        # 'min_sell': min_sell,
        # 'max_buy': max_buy
        self.con()
        cursor = self.connection.cursor()

        # Создаем таблицу Users
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {name_table} (
        id INTEGER PRIMARY KEY,
        nameitem TEXT NOT NULL,
        city TEXT NOT NULL,
        count INTEGER,
        level INTEGER NOT NULL,
        char INTEGER,
        min_sell INTEGER,
        max_buy INTEGER
        )
        ''')

        self.save_close_con()

    def new_data_order(self, data_mail: Mail_data):
        self.con()
        cursor = self.connection.cursor()

        if data_mail.active == 'buy':
            self.name_table = 'buy_mail_table'
        if data_mail.active == 'sell':
            self.name_table = 'sell_mail_table'

        cursor.execute(
            f'''
            INSERT INTO {self.name_table} (nameitem, city, count, level_item_name, price_one, price_gen, datetime, processed)
             VALUES('{data_mail.name}', '{data_mail.city}', '{data_mail.count}',
              '{data_mail.level_item_name}', '{data_mail.price_one}', '{data_mail.price_gen}',
               '{data_mail.datetime}', {data_mail.processed} )
            '''
        )
        self.save_close_con()


    def create_db_and_table(self, name_table):

        # Создаем подключение к базе данных (файл my_database.db будет создан)
        self.con()
        cursor = self.connection.cursor()

        # Создаем таблицу Users
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {name_table} (
        id INTEGER PRIMARY KEY,
        nameitem TEXT NOT NULL,
        city TEXT NOT NULL,
        count INTEGER,
        level_item_name TEXT NOT NULL,
        price_one INTEGER,
        price_gen INTEGER,
        datetime DATETIME,
        processed BOOL
        )
        ''')

        self.save_close_con()

        # Сохраняем изменения и закрываем соединение

    def save_close_con(self):
        self.connection.commit()
        self.connection.close()

    def new_data_mail(self, data_mail: Mail_data):
        self.con()
        cursor = self.connection.cursor()

        if data_mail.active == 'buy':
            self.name_table = 'buy_mail_table'
        if data_mail.active == 'sell':
            self.name_table = 'sell_mail_table'

        cursor.execute(
            f'''
            INSERT INTO {self.name_table} (nameitem, city, count, level_item_name, price_one, price_gen, datetime, processed)
             VALUES('{data_mail.name}', '{data_mail.city}', '{data_mail.count}',
              '{data_mail.level_item_name}', '{data_mail.price_one}', '{data_mail.price_gen}',
               '{data_mail.datetime}', {data_mail.processed} )
            '''
        )
        self.save_close_con()

    def deleteall(self, table_name):
        self.con()
        cursor = self.connection.cursor()
        cursor.execute(f'DELETE FROM `{table_name}`')
        self.save_close_con()

    def del_table(self, name_table):
        self.con()
        cursor = self.connection.cursor()
        cursor.execute(
            f'''
            DROP TABLE IF EXISTS {name_table}
            '''
            )
        self.save_close_con()

# order_bd = ManageBD(name_table='order_sell')
# order_bd.del_table('mail_data')
# mail_bd.deleteall('buy_mail_table')
#
# mail_bd.set_name_table('buy_mail_table')
#
# mail_bd.create_db_and_table()