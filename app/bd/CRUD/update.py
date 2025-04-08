from sqlalchemy import select, exc
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.bd.bd_connect.bd_sinc_alch import async_session_factory
from app.bd.models.models import ValidNamed, OrderSell, MailSell, MailBuy


class AsincUpdateData():

    @staticmethod
    async def update_valid_name(name_item: str, new_name_item: str, async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session() as session:

            item_name_refactor_data = await session.execute(select(ValidNamed).where(ValidNamed.name_item == name_item))
            item_name_refactor_data = item_name_refactor_data.scalars().one()
            item_name_refactor_data.name_item = new_name_item
            try:
                await session.commit()
                return True
            except exc.SQLAlchemyError:
                return False

    @staticmethod
    async def update_order_sell(id: int, processed: bool,
                                async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session() as session:
            order_refactor_data = await session.execute(select(OrderSell).where(OrderSell.id == id))
            order_refactor_data = order_refactor_data.scalars().one()
            order_refactor_data.processed = processed
            try:
                await session.commit()
                return True
            except exc.SQLAlchemyError:
                return False

    @staticmethod
    async def update_mail_sell(id: int, processed: bool,
                                async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session() as session:
            mail_refactor_data = await session.execute(select(MailSell).where(MailSell.id == id))
            mail_refactor_data = mail_refactor_data.scalars().one()
            mail_refactor_data.processed = processed
            try:
                await session.commit()
                return True
            except exc.SQLAlchemyError:
                return False

    @staticmethod
    async def update_mail_buy(id: int, processed: bool,
                               async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session() as session:
            mail_refactor_data = await session.execute(select(MailBuy).where(MailBuy.id == id))
            mail_refactor_data = mail_refactor_data.scalars().one()
            mail_refactor_data.processed = processed
            try:
                await session.commit()
                return True
            except exc.SQLAlchemyError:
                return False