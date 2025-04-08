import os

from pydantic_settings import BaseSettings, SettingsConfigDict

from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')




def path_env():
    '''
    если sqlite
    '''
    BASE_DIR = os.path.dirname(os.path.abspath(__name__))
    db_path = os.path.join(BASE_DIR, f".env")
    return db_path

class BDSettings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL_asyncpg(self):
        # postgresql+asyncpg://postgres:postgres@localhost:5432/sa
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL_psycopg(self):
        # DSN
        # postgresql+psycopg://postgres:postgres@localhost:5432/sa
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL_sqlite_async(self):
        # DSN
        # postgresql+psycopg://postgres:postgres@localhost:5432/sa
        return f"sqlite+aiosqlite:///users.db"

    @property
    def DATABASE_URL_sqlite(self):
        # DSN
        # postgresql+psycopg://postgres:postgres@localhost:5432/sa
        return f"sqlite+pysqlite:///users.db"

    model_config = SettingsConfigDict(env_file='.env')



if __name__=='__main__':
    settings = BDSettings()
    print(settings.DATABASE_URL_psycopg)
# print(path_env())