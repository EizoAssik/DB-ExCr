DB-ExCr
=======

## 关于名字 ##

DB-ExCr, Database Experiment Cracker, 不是杜比前任铬.

为什么要写成DB-ExCr呢？因为我懒得写全啊...囧rz

至于功能，请参考**What's The Functions?**一节; 使用方法请查看各个模块的`README`

## 关于DB-ExCr ##

DB-ExCr的核心目标是设计实现一个用于高效「生成」「多数学校能用的」数据库上机作业的「机制」. 

是的, 机制. `DB-ExCr`的主要目的是探索一个更高校的「生成」上级题的机制, 
所以这里的代码本身应该没什么大用...吧ㄟ( ▔, ▔ )ㄏ

好吧，其实动机也没那么那啥，只是我懒得写作业而已...

另: 项目中附带的样例来自数据库系统概念中文第五版, 题目来自XDU软件学院.

## What's The Function? ##

简单来说，`DB-ExCr`的功能包括但不仅限于：

从

    branch{+branch_name, branch_city};
    
    loan{+loan_number,
	 *branch_name,
	  amount[numeric(16,2)]};
	  
	borrower{+*customer_name, +*loan_number};
生成

    CREATE TABLE IF NOT EXISTS branch
    	(branch_name VARCHAR(64),
    	branch_city VARCHAR(64),
    	PRIMARY KEY(branch_name));
    
    CREATE TABLE IF NOT EXISTS loan
    	(loan_number VARCHAR(64),
    	branch_name VARCHAR(64),
    	amount numeric(16,2),
    	PRIMARY KEY(loan_number),
    	FOREIGN KEY(branch_name) REFERENCES branch(branch_name));
    
    CREATE TABLE IF NOT EXISTS borrower
    	(customer_name VARCHAR(64),
    	loan_number VARCHAR(64),
    	PRIMARY KEY(customer_name, loan_number),
    	FOREIGN KEY(customer_name) REFERENCES borrower(customer_name),
    	FOREIGN KEY(loan_number) REFERENCES loan(loan_number));
    	
从

    branch_name | branch_city | assets
    ------------+-------------+--------
    Brighton    | Brooklyn    | 7100000
    Downtown    | Brooklyn    | 9000000
    Mianus      | Horseneck   |  400000
生成

    INSERT INTO branch(branch_name, branch_city, assets) VALUES ('Brighton', 'Brooklyn', 7100000);
    INSERT INTO branch(branch_name, branch_city, assets) VALUES ('Downtown', 'Brooklyn', 9000000);
    INSERT INTO branch(branch_name, branch_city, assets) VALUES ('Mianus', 'Horseneck', 400000);

## 结构 ##

+ initial_data
    用于生成无聊的批量INSERT语句

+ initial_data
    用于生成无聊的批量建表语句

+ unofficial_solution
    如果你比我还懒，你总是可以……

## CHANGE-LOG ##
+ 2014.04.25
  喜闻乐见的写README

+ 2014.04.25
  CREATE/INSERT生成工具完成

+ 2014.04.23
  考完试, 开工
