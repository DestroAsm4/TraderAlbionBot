import datetime
from typing import Annotated, Optional
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, func, text, Index, CheckConstraint, \
    PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.bd.models.tools_model import Base, str_256, WorkLoad
import enum




intpk = Annotated[int, mapped_column(primary_key=True)] # убирает повторение строк
created_at = Annotated[datetime.datetime, mapped_column(server_default=func.now())] # serer_deoult подставляет текущую дату автоамаатически
    # func.now текущий часовой пояс, text('TIMEZONE("utc", now())') часовой пояс utc, default=datetime.utcnow() - время
    # устанавливается питоном а не субд, но лучше субд
updated_at = Annotated[datetime.datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.datetime.utcnow)]
# обязательно без скобочек что бы данные все время менялись иначе будет одна дата

class OrderSell(Base):

    __tablename__ = 'order_sell'

    id: Mapped[intpk]
    name_item: Mapped[str_256]
    city: Mapped[str_256]
    count: Mapped[int]
    level: Mapped[int]
    char: Mapped[int]
    min_sell: Mapped[int]
    max_buy: Mapped[int]
    processed: Mapped[bool]


    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

class MailBuy(Base):

    __tablename__ = 'mail_buy'

    id: Mapped[intpk]
    name_item: Mapped[str_256]
    city: Mapped[str_256]
    count: Mapped[int]
    level_item_name: Mapped[int]
    price_one: Mapped[int]
    price_gen: Mapped[int]
    datetime_order: Mapped[datetime.datetime]
    processed: Mapped[bool]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


class MailSell(Base):

    __tablename__ = 'mail_sell'

    id: Mapped[intpk]
    name_item: Mapped[str_256]
    city: Mapped[str_256]
    count: Mapped[int]
    level_item_name: Mapped[int]
    price_one: Mapped[int]
    price_gen: Mapped[int]
    datetime_order: Mapped[datetime.datetime]
    processed: Mapped[bool]

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

class ValidNamed(Base):

    __tablename__ = 'valid_named'

    id: Mapped[intpk]
    name_item: Mapped[str_256] = mapped_column(unique=True)


    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


class NotValidNamed(Base):

    __tablename__ = 'not_valid_named'

    id: Mapped[intpk]
    name_item: Mapped[str_256] = mapped_column(unique=True)

    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]