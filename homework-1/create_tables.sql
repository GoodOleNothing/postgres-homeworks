-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	first_name varchar(100),
	last_name varchar(100),
	title text,
	birth_date date,
	notes text
);
SELECT * FROM employees;

CREATE TABLE customers
(
	customer_id char(5) PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100)
);
SELECT * FROM customers;

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id char(5) REFERENCES customers(customer_id) NOT NULL,
	employee_id int,
	order_date date,
	ship_city varchar(100)
);
SELECT * FROM orders
