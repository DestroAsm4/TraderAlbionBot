from typing import Optional

from sqlalchemy import delete, select, exc
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.bd.bd_connect.bd_sinc_alch import async_engin, async_session_factory
from app.bd.models.models import ValidNamed, NotValidNamed, OrderSell, MailSell, MailBuy
from app.bd.models.tools_model import Base


class AsyncDataDelete():
    # ---------------модель 2---------------
    @staticmethod
    async def async_delete_table():
        '''
        ORM
        '''
        async with async_engin.begin() as conn:
            try:
                await conn.run_sync(Base.metadata.drop_all)
                return True
            except exc.SQLAlchemyError:
                return False

    @staticmethod
    async def delete_valid_name(name_item: str, async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session():
            # Delete rows with null values in acquired_by_warehouse_date column
            delete_query = delete(ValidNamed).where(ValidNamed.name_item == name_item)

            async with async_session.begin() as session:
                try:
                    await session.execute(delete_query)
                    return True
                except exc.SQLAlchemyError:
                    return False


    @staticmethod
    async def full_delete_valid_name(async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session():
            # Delete rows with null values in acquired_by_warehouse_date column
            delete_query = delete(ValidNamed)


            async with async_session.begin() as session:
                try:
                    await session.execute(delete_query)
                    return True
                except exc.SQLAlchemyError:
                    return False

    @staticmethod
    async def delete_not_valid_name(id: Optional[int] = None, name: Optional[str] = None, async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session():
            # Delete rows with null values in acquired_by_warehouse_date column
            if id:
                delete_query = delete(NotValidNamed).where(NotValidNamed.id == id)
            elif name:
                delete_query = delete(NotValidNamed).where(NotValidNamed.name_item == name)
            else:
                return False

            async with async_session.begin() as session:
                try:
                    await session.execute(delete_query)
                    return True
                except exc.SQLAlchemyError:
                    return False

    @staticmethod
    async def full_delete_not_valid_name(async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session():
            # Delete rows with null values in acquired_by_warehouse_date column
            delete_query = delete(NotValidNamed)

            async with async_session.begin() as session:
                try:
                    await session.execute(delete_query)
                    return True
                except exc.SQLAlchemyError:
                    return False

    @staticmethod
    async def delete_order_sell(id: int, async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session():
            # Delete rows with null values in acquired_by_warehouse_date column
            delete_query = delete(OrderSell).where(OrderSell.id == id)

            async with async_session.begin() as session:
                try:
                    await session.execute(delete_query)
                    return True
                except exc.SQLAlchemyError:
                    return False

    @staticmethod
    async def delete_mail_sell(id: int, async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session():
            # Delete rows with null values in acquired_by_warehouse_date column
            delete_query = delete(MailSell).where(MailSell.id == id)

            async with async_session.begin() as session:
                try:
                    await session.execute(delete_query)
                    return True
                except exc.SQLAlchemyError:
                    return False

    @staticmethod
    async def delete_mail_buy(id: int, async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session():
            # Delete rows with null values in acquired_by_warehouse_date column
            delete_query = delete(MailBuy).where(MailBuy.id == id)

            async with async_session.begin() as session:
                try:
                    await session.execute(delete_query)
                    return True
                except exc.SQLAlchemyError:
                    return False


    @staticmethod
    async def full_delete_order_sell(async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session():
            delete_query = delete(OrderSell)

            async with async_session.begin() as session:
                try:
                    await session.execute(delete_query)
                    return True
                except exc.SQLAlchemyError:
                    return False

    @staticmethod
    async def full_delete_mail_sell(async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session():
            delete_query = delete(MailSell)

            async with async_session.begin() as session:
                try:
                    await session.execute(delete_query)
                    return True
                except exc.SQLAlchemyError:
                    return False

    @staticmethod
    async def full_delete_mail_buy(async_session: async_sessionmaker[AsyncSession] = async_session_factory):
        async with async_session():
            delete_query = delete(MailBuy)

            async with async_session.begin() as session:
                try:
                    await session.execute(delete_query)
                    return True
                except exc.SQLAlchemyError:
                    return False
