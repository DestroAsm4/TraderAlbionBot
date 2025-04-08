import asyncio

from sqlalchemy import text

from app.bd.bd_connect.bd_sinc_alch import async_engin, engin


async def async_check_connect() -> str:
    async with async_engin.begin() as conn:
        query = """
        SELECT VERSION()
            """
        res = await conn.execute(text(query))
        return res.first()[0]

def check_connect() -> str:
    with engin.connect() as conn:
        res = conn.execute(text('SELECT VERSION()'))
        return res.first()[0]

if __name__ == '__main__':
    pass
    # print(conect())
    # print(asyncio.run(check_bound()))