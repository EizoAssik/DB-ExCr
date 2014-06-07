# Design for the Simplified Notation of SQL #

In short, the main syntax is

+ A `$` for `SELECT`
+ `()` for the `FROM` clause
+ `[]` for the `SELECT` clause, ** `@` will be replaced by the table name in `FROM` clause **
+ `<>` for gathering. `GROUP BY` for MariaDB
+ `{}` for the condition, `WHERE`, `WITH` and `HAVING` for example. All names besides `@` will just keep in their raw style.
+ `[[]]` for optional options, `ORDER BY`, `LIMIT`, etc
+ `=` for local binding, but `@` no more available:(

`$(branch);`
 ```SQL
 SELECT * FROM branch;
 ```
`$(branch)[@_name, @_city]`
```SQL
SELECT branch_name, branch_city FROM branch;
```
`$(branch)[@_name, @_city]{@_name="Foo"}`
```SQL
 SELECT branch_name, branch_city FROM branch WHERE branch_name="Foo";
```
`$(branch)[@_name, @_city]<@_city>{@_city!="Rye"}`
```SQL
SELECT branch_name, branch_city FROM branch GROUP BY branch_city HAVING branch_name!="Rye";
```
`$(branch)[[SORT BY @_name]];`

s = $(branch);
$s[branch_name];
SELECT branch_name FROM (SELECT * FROM branch) as s;

Operators

and or

|X |X| x|

## Production ##

SQL -> SELECT
     | SQL FROM
     | SQL CONDITION
     | SQL GATHERING

SELECT -> SELECTOR LP CONTENT RP
        | SELECTOR NAME

FROM   -> LBP CONTENT RBP

CONDITION -> LCP CONTENT RCP

GATHERING -> LAP CONTENT RAP