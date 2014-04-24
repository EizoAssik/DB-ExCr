inital_data
===========

## 说明 ##

### .rows 文件 ###

.rows 文用于描述每行的内容, 格式形如:

![SAMPLE][sample_img]

> 注: 第一行是必须的, 用于表述列名
> 
> 第二行是可选的, 以双连字符'--'开头的行会被视为注释,
>
> 这一行是为了让表格看上去更像表格而添加的

+ 目前支持的数据类型: String, int, float.
+ 对于多数作业来说似乎大概也许可能还是够的...覆盖会慢慢扩充的...

### .seq 文件 ###

.seq 文件用于描述由各个.rows文件成生的.SQL文件的连接顺序

每行一个basename, 不含后缀

[sample_img]: https://github.com/EizoAssik/DB-ExCr/raw/insmod/initial_data/sample.png
