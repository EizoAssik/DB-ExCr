# inital_tables #

## 说明 ##

### .schema 文件 ###

.schema 文用于描述各个表的模式, 格式形如:

    branch{+branch_name,
    		branch_city,
    		assets};
    
    customer{+customer_name,
    		  customer_street,
    		  customer_city};
    
    loan{+loan_number,
    	 *branch_name,
    	  amount[numeric(16,2)]};
其中:

+ 大体上，语法就是`表名{列名...};`
+ 列命前面的`+`表示这是一个主键，`*`表示外键，`+*`和`*+`等价
外键自动指向这个列名在.schema文件中第一次出现的地方
+ 列名后缀的`[]`中用于填写数据类型，省略则使用`VARCHAR(64)`
+ 分号是可省略的，尽管我写了……
+ 我还没有给.schema文件添加注释
+ 以上示例来自`Database System Concepts, 5th`

用于词法/语法的`lex&yacc`来自`ply`模块。
推导时使用的产生式如下

	schema -> cine
	        | schema cine
	cine   -> term LCP terms RCP
	        | 
	terms  -> term
	        | terms COMMA
	        | terms COMMA term
	term   -> NAME
	        | REF term
	        | PRI term
	        | term LSP type RSP
	        
其中:

+ schema表示.schema文件
+ cine="CREATE TABLE IF NOT EXISTS"
+ terms...就是列表, 逗号分割的那种
+ term是原子项, 基本上就是个名字或者类型