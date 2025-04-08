import asyncio

from app.bd.CRUD import crud
from app.bd.CRUD_Scripts.utils import TCRUDData
from app.bd.bd_connect.bd_sinc_alch import async_session_factory


class ValidItemName():

    @staticmethod
    async def full_delete_item_name():
        await crud.delete.full_delete_valid_name(async_session_factory)


    @staticmethod
    async def new_valid_item_name(item_name: str):
        res = await crud.insert.insert_valid_name(async_session_factory, item_name)
        return res

    @staticmethod
    async def delete_valid_item_name(item_name):
        res = await crud.delete.delete_and_select_valid_name(async_session_factory, item_name)
        return res

    @staticmethod
    async def select_valid_item_name():
        res = await crud.read.select_valid_name(async_session_factory)
        return res

    @staticmethod
    async def update_valid_item_name(name: str, new_name: str):
        res = await crud.update.update_valid_name(async_session_factory, name, new_name)
        return res

    @staticmethod
    async def full_cyckle_valid_item_name() -> dict:
        res = dict()

        res[TCRUDData.full_delete] = await crud.delete.full_delete_valid_name(async_session_factory)
        res[TCRUDData.insert] = await crud.insert.insert_valid_name('test_name_valid')
        res[TCRUDData.read] = await crud.read.select_valid_name()
        res[TCRUDData.update] = await crud.update.update_valid_name('test_name_valid', 'updated_name')
        res[TCRUDData.delete] = await crud.delete.delete_valid_name('updated_name')

        return res

    @staticmethod
    async def full_cycle_not_valid_item_name() -> dict:
        res = dict()
        res[TCRUDData.full_delete] = await crud.delete.full_delete_not_valid_name()
        res[TCRUDData.insert] = await crud.insert.insert_not_valid_name(not_valid_name='test_name_not_valid')
        res[TCRUDData.read] = await crud.read.select_not_valid_name()
        last_res = res[TCRUDData.read][-1]
        last_id = last_res[0]
        res[TCRUDData.delete] = await crud.delete.delete_not_valid_name(id=last_id)

        return res



valid_name = ValidItemName()
if __name__ == '__main__':


    print(asyncio.run(valid_name.full_cycle_not_valid_item_name()))
