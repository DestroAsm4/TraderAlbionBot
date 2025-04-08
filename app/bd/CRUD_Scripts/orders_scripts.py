import asyncio

from app.bd.CRUD import crud
from app.bd.CRUD_Scripts.utils import TCRUDData
from app.bd.bd_connect.bd_sinc_alch import async_session_factory


class OrderScripts():

    ## OrderSell

    @staticmethod
    async def full_delete_order_sell():
        await crud.delete.full_delete_order_sell()

    @staticmethod
    async def full_cyckle_order_sell():
        res = dict()
        res[TCRUDData.full_delete] = await crud.delete.full_delete_order_sell()
        res[TCRUDData.insert] = await crud.insert.insert_order_sell()
        res[TCRUDData.read] = await crud.read.select_order_sell()
        last_res = res[TCRUDData.read][-1]
        last_id = last_res[0]
        res[TCRUDData.update] = await crud.update.update_order_sell(last_id, False)
        res[TCRUDData.delete] = await crud.delete.delete_order_sell(last_id)

        return res


order_scripts = OrderScripts()

if __name__ == '__main__':
    print(asyncio.run(order_scripts.full_cyckle_order_sell()))