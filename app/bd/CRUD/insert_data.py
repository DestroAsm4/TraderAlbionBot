from datetime import datetime

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from sqlalchemy import exc
from app.bd.bd_connect.bd_sinc_alch import async_session_factory
from app.bd.models.models import ValidNamed, NotValidNamed, MailSell, MailBuy, OrderSell
from app.bd.queries import sql_queryes

test_mail_sell_data = MailSell(
                          name_item = 'test_name_mail_sell',
                          city='test_city',
                          count=3,
                          level_item_name=4,
                          price_one=50,
                          price_gen=150,
                          datetime_order=datetime.now(),
                          processed=True
)

test_mail_buy_data = MailBuy(
                          name_item = 'test_name_mail_buy',
                          city='test_city',
                          count=3,
                          level_item_name=4,
                          price_one=50,
                          price_gen=150,
                          datetime_order=datetime.now(),
                          processed=True
)

test_order_sell_data = OrderSell(
                          name_item = 'test_name_order_sell',
                          city='test_city',
                          count=3,
                          level=1,
                          char=2,
                          min_sell=50,
                          max_buy=30,
                          processed=True
)

class AsyncDataInsert():

    @staticmethod
    async def insert_valid_name(valid_name: str = 'test_name', async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session() as session:
            new_name_item = ValidNamed(name_item=valid_name)
            # insert_query = insert(new_name_item)
            async with session.begin():
                try:
                    session.add_all([new_name_item])
                    return True
                except exc.SQLAlchemyError:
                    return False

    @staticmethod
    async def insert_not_valid_name(not_valid_name: str = 'test_name', async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session() as session:
            new_name_item = NotValidNamed(name_item=not_valid_name)
            # insert_query = insert(new_name_item)
            async with session.begin():
                try:
                    session.add_all([new_name_item])
                    return True
                except exc.SQLAlchemyError:
                    return False

    @staticmethod
    async def insert_mail_sell(mail_data: MailSell = test_mail_sell_data, async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session() as session:

            # insert_query = insert(new_name_item)
            async with session.begin():
                try:
                    session.add_all([mail_data])
                    return True
                except exc.SQLAlchemyError:
                    return False

    @staticmethod
    async def insert_mail_buy(async_session: async_sessionmaker[AsyncSession] = async_session_factory,
                               mail_data: MailBuy = test_mail_buy_data):
        async with async_session() as session:

            # insert_query = insert(new_name_item)
            async with session.begin():
                try:
                    session.add_all([mail_data])
                    return True
                except exc.SQLAlchemyError:
                    return False

    @staticmethod
    async def insert_order_sell(async_session: async_sessionmaker[AsyncSession] = async_session_factory,
                              order_data: OrderSell = test_order_sell_data):
        async with async_session() as session:

            # insert_query = insert(new_name_item)
            async with session.begin():
                try:
                    session.add_all([order_data])
                    return True
                except exc.SQLAlchemyError:
                    return False

if __name__ == '__main__':

    pass

