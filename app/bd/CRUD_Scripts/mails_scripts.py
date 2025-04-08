import asyncio

from app.bd.CRUD import crud
from app.bd.CRUD_Scripts.utils import TCRUDData


class MailScripts():

    ## OrderSell

    @staticmethod
    async def full_delete_mail_sell():
        await crud.delete.full_delete_mail_sell()


    @staticmethod
    async def full_cyckle_mail_sell():
        res = dict()
        res[TCRUDData.full_delete] = await crud.delete.full_delete_mail_sell()
        res[TCRUDData.insert] = await crud.insert.insert_mail_sell()
        res[TCRUDData.read] = await crud.read.select_mail_sell()
        last_res = res[TCRUDData.read][-1]
        last_id = last_res[0]
        res[TCRUDData.update] = await crud.update.update_mail_sell(last_id, False)
        res[TCRUDData.delete] = await crud.delete.delete_mail_sell(last_id)

        return res

    @staticmethod
    async def full_cyckle_mail_buy():
        res = dict()
        res[TCRUDData.full_delete] = await crud.delete.full_delete_mail_buy()
        res[TCRUDData.insert] = await crud.insert.insert_mail_buy()
        res[TCRUDData.read] = await crud.read.select_mail_buy()
        last_res = res[TCRUDData.read][-1]
        last_id = last_res[0]
        res[TCRUDData.update] = await crud.update.update_mail_buy(last_id, False)
        res[TCRUDData.delete] = await crud.delete.delete_mail_buy(last_id)

        return res

mail_scripts = MailScripts()

if __name__ == '__main__':
    print(asyncio.run(mail_scripts.full_cyckle_mail_sell()))