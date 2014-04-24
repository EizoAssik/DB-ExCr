-- 创建数据库

CREATE DATABASE IF NOT EXISTS bank;

USE bank;

-- 创建表

CREATE TABLE IF NOT EXISTS branch
   (branch_name char(15),
    branch_city char(30),
    assets     numeric(16,2),
    PRIMARY KEY (branch_name));

CREATE TABLE IF NOT EXISTS customer
   (customer_name char(20),
    customer_street char(30),
    customer_city char(30),
    PRIMARY KEY (customer_name));

CREATE TABLE IF NOT EXISTS loan
   (loan_number char(8),
    branch_name char(15),
    amount numeric(16,2),
    PRIMARY KEY(loan_number),
    FOREIGN KEY(branch_name) REFERENCES branch(branch_name));

CREATE TABLE IF NOT EXISTS borrower
   (customer_name char(20),
    loan_number char(8),
    PRIMARY KEY(customer_name, loan_number),
    FOREIGN KEY(customer_name) REFERENCES customer(customer_name),
    FOREIGN KEY(loan_number) REFERENCES loan(loan_number));

CREATE TABLE IF NOT EXISTS account
   (account_number char(8), 
    branch_name char(15),
    balance numeric(16,2),
    PRIMARY KEY(account_number),
    FOREIGN KEY(branch_name) REFERENCES branch(branch_name));

CREATE TABLE IF NOT EXISTS depositor
   (customer_name char(30),
    account_number char(8),
    PRIMARY KEY(customer_name, account_number),
    FOREIGN KEY(customer_name) REFERENCES customer(customer_name),
    FOREIGN KEY(account_number) REFERENCES account(account_number));
