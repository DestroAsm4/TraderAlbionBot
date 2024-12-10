треид бот для альбион

для начала работы нужно:
    клонировать репозиторий
    создать виртуальное окружение,
    подгрузить пакеты с помощью поетри "poetry install"
    создать бд постгресс через докер:
        docker run --name my_bd_name -p 5432:5432 -e  POSTGRES_PASSWORD=my_password -d postgres
    переписать данные для соединения с бд в env файл:
        DB_HOST=postgres
        DB_PORT=5432
        DB_USER=postgres
        DB_PASS=my_password
        DB_NAME=my_bd_name
123
