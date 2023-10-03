"""Скрипт для заполнения данными таблиц в БД Postgres."""

import csv

import psycopg2
from psycopg2.extensions import connection, cursor

from settings import PASSWORD, LST_TABLES


def upload_data_to_table(cur: cursor, path: str, table_name: str) -> None:
    """
    Загружает данные из CSV-файла в таблицу
    :param cur: :class:`psycopg2.extensions.cursor`
    :param path: путь до CSV-файла
    :param table_name: имя таблицы
    :return: None
    """

    with open(path, 'r', encoding='utf-8') as file:
        reader: csv.reader = csv.reader(file)
        lst = next(reader)
        columns_name = ", ".join(lst)
        values = ", ".join(["%s"] * len(lst))
        query = f'INSERT INTO {table_name} ({columns_name}) VALUES ({values})'
        for row in reader:
            cur.execute(query, row)


def main():
    conn: connection = psycopg2.connect(host='localhost', database='north', user='postgres', password=PASSWORD)
    try:
        with conn:
            with conn.cursor() as cur:
                for table_name, path in LST_TABLES:
                    upload_data_to_table(cur, path, table_name)
    except Exception as e:
        raise e
    finally:
        conn.close()


if __name__ == '__main__':
    main()
