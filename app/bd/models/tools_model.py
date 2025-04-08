import enum
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase

str_256 = Annotated[str, 256]

class Base(AsyncAttrs, DeclarativeBase):
    type_annotation_map = {
        str_256: String(256)
    } # cоздание типов колонок с ограничениями

    def __repr__(self):
        cols = []
        for col in self.__table__.columns.keys():
            cols.append(f'{col}={getattr(self, col)}')
        return f"<{self.__class__.__name__} {','.join(cols)}>"

class WorkLoad(str, enum.Enum): # enum - перечисление
    parttime = 'parttime'
    fulltime = 'fulltime'