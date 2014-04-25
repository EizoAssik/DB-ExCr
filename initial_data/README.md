# inital_data #

## 说明 ##

### .rows 文件 ###

`.rows` 文用于描述每行的内容, 格式形如:

    account_number | branch_name | balance
    ---------------+-------------+--------
    A-101          | Downtown    | 500
    A-102          | Perryridge  | 400
    A-201          | Brighton    | 900
    A-215          | Mianus      | 700
    A-217          | Brighton    | 750
    A-222          | Redwood     | 700
    A-305          | Round Hill  | 350

注: 

+ 第一行是必须的, 用于表述列名
+ 第二行是可选的, 以双连字符'--'开头的行会被视为注释,
这一行是为了让表格看上去更像表格而添加的
+ 目前支持的数据类型: `String, int, float`.
+ 对于多数作业来说似乎大概也许可能还是够的...覆盖会慢慢扩充的...

### .seq 文件 ###

`.seq` 文件用于描述由各个`.rows`文件成生的`.SQL`文件的连接顺序

每行一个`basename`, 不含后缀

### makefile ###

`make`的默认动作是按照`.seq`文件中描述的顺序，从`.rows`文件中生成`.sql`文件片段，并连接形成`pieces.sql`

`make clean`将清除所有`.sql`文件