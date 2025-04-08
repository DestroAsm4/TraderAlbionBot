from app.setting import Order_data, Mail_data


class QueryParam:

    @staticmethod
    def create_mail_buy():
        return f'''
        CREATE TABLE IF NOT EXISTS buy_mail (
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
        '''

    @staticmethod
    def create_mail_sell():
        return f'''
            CREATE TABLE IF NOT EXISTS sell_mail (
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
            '''

    @staticmethod
    def create_valid():
        return f'''
        CREATE TABLE IF NOT EXISTS valid_data (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
        )
        '''

    @staticmethod
    def create_not_valid():
        return f'''
           CREATE TABLE IF NOT EXISTS not_valid (
           id INTEGER PRIMARY KEY,
           name TEXT NOT NULL
           )
           '''

    @staticmethod
    def create_order_sell():
        return f'''
                CREATE TABLE IF NOT EXISTS order_sell (
                id INTEGER PRIMARY KEY,
                nameitem TEXT NOT NULL,
                city TEXT NOT NULL,
                count INTEGER,
                level INTEGER NOT NULL,
                char INTEGER,
                min_sell INTEGER,
                max_buy INTEGER,
                number INTEGER
                )
                '''

    @staticmethod
    def new_data_order(order_data: Order_data):
        if order_data.min_sell == 'Нет данных':
            order_data.min_sell = 'NULL'
        if order_data.max_buy == 'Нет данных':
            order_data.min_sell = 'NULL'

        return f'''
            INSERT INTO order_sell (name, level, char, price_gen, min_sell, max_buy, count)
             VALUES('{order_data.name}', '{order_data.level}', '{order_data.char}',
              '{order_data.price_gen}', '{order_data.min_sell}', '{order_data.max_buy}',
               '{order_data.count}' )
            '''

    @staticmethod
    def new_t_data_order(order_data: Order_data):
        if order_data.min_sell == 'Нет данных':
            order_data.min_sell = 'NULL'
        if order_data.max_buy == 'Нет данных':
            order_data.min_sell = 'NULL'

        return f'''
            INSERT INTO test_order_sell (name, level, char, price_gen, min_sell, max_buy, count)
             VALUES('{order_data.name}', '{order_data.level}', '{order_data.char}',
              '{order_data.price_gen}', '{order_data.min_sell}', '{order_data.max_buy}',
               '{order_data.count}' )
            '''

    @staticmethod
    def new_valid(name):

        return f'''
                    INSERT INTO valid_data (name)
                     VALUES('{name}' )
                    '''

    @staticmethod
    def new_mail(data_mail: Mail_data):

        if data_mail.active == 'buy':
            name_table = 'buy_mail_table'
        if data_mail.active == 'sell':
            name_table = 'sell_mail_table'

        return f'''
            INSERT INTO {name_table} (nameitem, city, count, level_item_name, price_one, price_gen, datetime, processed)
             VALUES('{data_mail.name}', '{data_mail.city}', '{data_mail.count}',
              '{data_mail.level_item_name}', '{data_mail.price_one}', '{data_mail.price_gen}',
               '{data_mail.datetime}', {data_mail.processed} )
            '''