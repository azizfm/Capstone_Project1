
CREATE TABLE employee_table (
     sales_team_lead VARCHAR (100),
     pay_grade VARCHAR(3),
     region  VARCHAR(2),
     empID   VARCHAR(6),
     is_found   BOOL
);

select * from capstone1_sales_team_data;
select * from capstone1_sunday_data;
select * from capstone1_product_data;


CREATE TABLE products (
prod_code VARCHAR(8),
prod_name VARCHAR(100),
url VARCHAR(100),
link VARCHAR(100),
manufacturer VARCHAR(100),
extended_service_plan VARCHAR(7),
warranty_price INT,
2019Q1 INT,
2019Q2 INT,
2019Q3 INT,
2019Q4 INT,
2020Q1 INT,
2020Q2 INT,
2020Q3 INT,
2020Q4 INT
);

select * from products;

#SET GLOBAL local_infile = 1;
# infile loading SET GLOBAL local_infile=1


load data local infile "C:\Users\azizs\TEKsystems\Capstone_Project1\raw_data\\capstone1_rawdata - sheet2.csv" into table capston_project_schema.employee_table fields terminated by ','
lines terminated by '\n'
ignore 2 lines
(sales_team_lead, pay_grade, region, empID, is_found)