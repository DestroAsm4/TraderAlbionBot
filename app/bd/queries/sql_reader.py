import enum
from dataclasses import dataclass


@dataclass
class Files():
    check_connect: str = 'check_version_connect'



class SQLReader():

    def __reader(self, name_file):
        with open(f'{name_file}.sql', 'r') as file:
            data = file.read().replace('\n', ' ').replace('\r', ' ')
            return data


    def check_connect(self):
        return self.__reader(Files.check_connect)




