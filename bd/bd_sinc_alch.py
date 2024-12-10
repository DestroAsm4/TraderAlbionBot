from sqlalchemy import create_engine, text
from bd.bd_link_conf import BDSettings

settings = BDSettings()

engin = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=False,
)

