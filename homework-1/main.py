"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

# подключаемся к БД
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='1303'
)

cur = conn.cursor()

# работаем с таблицей employees
with open('north_data/employees_data.csv', 'r') as f:
    ed = csv.reader(f)
    for row in ed:
        cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s)', tuple(row))
cur.execute('SELECT * FROM employees')
rows = cur.fetchall()
#for row in rows:
#    print(row)
conn.commit()

# работаем с таблицей customers
with open('north_data/customers_data.csv', 'r') as f:
    cd = csv.reader(f)
    for row in cd:
        cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', tuple(row))
cur.execute('SELECT * FROM customers')
rows = cur.fetchall()
#for row in rows:
#    print(row)
conn.commit()

# работаем с таблицей orders
with open('north_data/orders_data.csv', 'r') as f:
    od = csv.reader(f)
    for row in od:
        cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', tuple(row))
cur.execute('SELECT * FROM orders')
rows = cur.fetchall()
#for row in rows:
#    print(row)
conn.commit()

cur.close()
conn.close()

# emp: "first_name","last_name","title","birth_date","notes"
# cust: "customer_id","company_name","contact_name"
# ord: "order_id","customer_id","employee_id","order_date","ship_city"
