from csv import DictReader
import psycopg2
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent

CSV_FILE_EMPLOYEES = Path.joinpath(ROOT_PATH, 'north_data', 'employees_data.csv')
CSV_FILE_CUSTOMERS = Path.joinpath(ROOT_PATH, 'north_data', 'customers_data.csv')
CSV_FILE_ORDERS = Path.joinpath(ROOT_PATH, 'north_data', 'orders_data.csv')

pg_tables = ['employees', 'customers', 'orders']
csv_list = [CSV_FILE_EMPLOYEES, CSV_FILE_CUSTOMERS, CSV_FILE_ORDERS]

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='t95qsnapQ')

try:
    with conn:
        for index, csv_data in enumerate(csv_list):
            try:
                with open(csv_data) as csv_file:
                    reader = DictReader(csv_file)
                    row: dict
                    with conn.cursor() as cur:
                        for row in reader:
                            values_tup = tuple(row.values())
                            values_str = '%s ' * len(values_tup)
                            cur.execute(f'INSERT INTO {pg_tables[index]} VALUES ({", ".join(values_str.split())})',
                                        values_tup)
            except FileNotFoundError:
                raise FileNotFoundError(f'отсутствует файл {csv_data}')

finally:
    conn.close()
