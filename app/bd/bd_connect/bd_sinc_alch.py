from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from app.bd.bd_connect.bd_link_conf import BDSettings

settings = BDSettings()

engin = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False,
)

async_engin = create_async_engine(
    url=settings.DATABASE_URL_asyncpg,

    echo=False,
)

async_session_factory = async_sessionmaker(async_engin, expire_on_commit=False,)




if __name__ == "__main__":
    s()