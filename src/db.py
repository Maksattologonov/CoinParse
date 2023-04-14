import psycopg2

from src.settings import DATABASE_CONNECTION

try:
    connection = psycopg2.connect(
        host=DATABASE_CONNECTION.get("db_host"),
        port=DATABASE_CONNECTION.get("db_port"),
        dbname=DATABASE_CONNECTION.get("db_name"),
        user=DATABASE_CONNECTION.get("db_user"),
        password=DATABASE_CONNECTION.get("db_password"),
    )

    with connection.cursor() as cursor:
        cursor.execute(
            "select version();"
        )
        print(f'Server version: {cursor.fetchone()}')

except psycopg2.Error as e:
    print("Ошибка подключения к базе данных:", e)
