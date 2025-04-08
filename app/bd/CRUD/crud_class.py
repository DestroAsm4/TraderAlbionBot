from dataclasses import dataclass

from .delete_data import AsyncDataDelete
from .insert_data import AsyncDataInsert
from .select_data import AsyncDataSelect
from .update import AsincUpdateData


@dataclass
class CRUD():
    insert = AsyncDataInsert()
    delete = AsyncDataDelete()
    read = AsyncDataSelect()
    update = AsincUpdateData()