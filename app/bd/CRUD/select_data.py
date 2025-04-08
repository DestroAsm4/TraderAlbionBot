from sqlalchemy import select
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.bd.bd_connect.bd_sinc_alch import async_session_factory
from app.bd.models.models import ValidNamed, NotValidNamed, OrderSell, MailSell, MailBuy


class AsyncDataSelect():

    @staticmethod
    async def select_valid_name(async_session: async_sessionmaker[AsyncSession] = async_session_factory) -> list[str]:
        async with async_session():
            select_query = select(ValidNamed.name_item)

            async with async_session.begin() as session:
                result = await session.execute(select_query)
                res = [x[0] for x in result.all()]
                return res

    @staticmethod
    async def select_not_valid_name(async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session():
            select_query = select(NotValidNamed.id, NotValidNamed.name_item)

            async with async_session.begin() as session:
                result = await session.execute(select_query)
                res = [x for x in result.all()]
                return res

    @staticmethod
    async def select_order_sell(async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session():
            select_query = select(OrderSell.id, OrderSell.name_item, OrderSell.processed)

            async with async_session.begin() as session:
                result = await session.execute(select_query)
                res = result.all()
                return res

    @staticmethod
    async def select_mail_sell(async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session():
            select_query = select(MailSell.id, MailSell.name_item, MailSell.processed)

            async with async_session.begin() as session:
                result = await session.execute(select_query)
                res = result.all()
                return res

    @staticmethod
    async def select_mail_buy(async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session():
            select_query = select(MailBuy.id, MailBuy.name_item, MailBuy.processed)

            async with async_session.begin() as session:
                result = await session.execute(select_query)
                res = result.all()
                return res