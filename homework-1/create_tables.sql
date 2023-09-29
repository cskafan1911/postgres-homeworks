CREATE TABLE employees
(
	employee_id int PRIMARY KEY NOT NULL,
	first_name varchar(50),
	last_name varchar(50),
	title varchar(100),
	birth_date varchar(10),
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(5) PRIMARY KEY,
	company_name varchar(50),
	contact_name varchar(50)
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY NOT NULL,
	customer_id varchar(5) REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id),
	order_date varchar(10),
	ship_city varchar(50)
);
