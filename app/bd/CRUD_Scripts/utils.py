from dataclasses import dataclass



@dataclass
class TCRUDData():
    full_delete: str = 'full_delete'
    insert: str = 'insert'
    read: str = 'read'
    update: str = 'update'
    delete: str = 'delete'

