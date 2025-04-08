import asyncio

from .utils import list_async_func_t, ResT
from app.bd.CRUD_Scripts.utils import TCRUDData

data_testing_asinc_func = asyncio.run(list_async_func_t())


class TestBDAsync():
    def test_async_not_async_connect(self):
        # print(data_testing_asinc_func)
        res = data_testing_asinc_func[ResT.check_conn]
        assert res == 'PostgreSQL 10.8, compiled by Visual C++ build 1800, 32-bit'


    def test_async_valid_name(self):
        res = data_testing_asinc_func[ResT.valid_name]
        assert res[TCRUDData.full_delete]
        assert res[TCRUDData.insert]
        assert res[TCRUDData.read][0] == 'test_name_valid'
        assert res[TCRUDData.update]
        assert res[TCRUDData.delete]

    def test_async_not_valid_name(self):
        res = data_testing_asinc_func[ResT.not_valid_name]
        assert res[TCRUDData.full_delete]
        assert res[TCRUDData.insert]
        assert res[TCRUDData.read][0][1] == 'test_name_not_valid'
        assert res[TCRUDData.delete]

    def test_async_order_sell(self):
        res = data_testing_asinc_func[ResT.order_sell]
        assert res[TCRUDData.full_delete]
        assert res[TCRUDData.insert]
        assert res[TCRUDData.read][0][1] == 'test_name_order_sell'
        assert res[TCRUDData.update]
        assert res[TCRUDData.delete]

    def test_async_mail_sell(self):
        res = data_testing_asinc_func[ResT.mail_sell]
        assert res[TCRUDData.full_delete]
        assert res[TCRUDData.insert]
        assert res[TCRUDData.read][0][1] == 'test_name_mail_sell'
        assert res[TCRUDData.update]
        assert res[TCRUDData.delete]

    def test_async_mail_buy(self):
        res = data_testing_asinc_func[ResT.mail_buy]
        assert res[TCRUDData.full_delete]
        assert res[TCRUDData.insert]
        assert res[TCRUDData.read][0][1] == 'test_name_mail_buy'
        assert res[TCRUDData.update]
        assert res[TCRUDData.delete]
