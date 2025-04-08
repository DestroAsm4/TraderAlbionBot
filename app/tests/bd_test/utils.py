import asyncio
from dataclasses import dataclass

from app.bd.CRUD_Scripts.check_connect import async_check_connect
from app.bd.CRUD_Scripts.valid_name_item_scripts import ValidItemName
from app.bd.CRUD_Scripts.orders_scripts import OrderScripts
from app.bd.CRUD_Scripts.mails_scripts import MailScripts
from app.bd.CRUD import crud
from app.bd.bd_connect.bd_sinc_alch import async_session_factory

valid_item_name = ValidItemName()
order = OrderScripts()
mails = MailScripts()

async def list_async_func_t() -> tuple:
    result_test_data = dict()
    result_test_data[ResT.check_conn] = await async_check_connect()
    result_test_data[ResT.valid_name] = await valid_item_name.full_cyckle_valid_item_name()
    result_test_data[ResT.not_valid_name] = await valid_item_name.full_cycle_not_valid_item_name()
    result_test_data[ResT.order_sell] = await order.full_cyckle_order_sell()
    result_test_data[ResT.mail_sell] = await mails.full_cyckle_mail_sell()
    result_test_data[ResT.mail_buy] = await mails.full_cyckle_mail_buy()

    return result_test_data












@dataclass
class ResT():
    check_conn: str = 'check_conn'
    valid_name: str = 'valid_name'
    not_valid_name: str = 'not_valid_name'
    order_sell: str = 'order_sell'
    mail_sell: str = 'mail_sell'
    mail_buy: str = 'mail_buy'