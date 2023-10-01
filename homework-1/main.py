from csv import DictReader
import psycopg2


conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='t95qsnapQ')

file_csv = "C:\\Users\\Dima\\postgres-homeworks\\homework-1\\north_data\\employees_data.csv"

with open(file_csv, 'r', encoding='utf-8-sig') as file:
    reader = DictReader(file)
    for line in reader:
        employees = (line['employee_id'], line['first_name'], line['last_name'], line['title'], line['birth_date'], line['notes'])

        conn = psycopg2.connect(
            host='localhost',
            database='north',
            user='postgres',
            password='t95qsnapQ')
        try:
            with conn:
                with conn.cursor() as cur:
                    cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', employees)
        finally:
            conn.close()
 