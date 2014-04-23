#/bin/python

FILENAME = "tables.template"


def to_sql_value(term):
    try:
        v = float(term)
        return str(v)
    except ValueError:
        pass
    try:
        v = str(term).lstrip().rstrip()
        return "'%s'" % v
    except Exception:
        return 'NULL'


if __name__ == '__main__':
    with open(FILENAME) as template:
        for line in template:
            columns = line.split()
            with open(columns[0] + ".rows") as rows:
                src = "INSERT INTO %s(%s) VALUES (%s);\n"
                table_name = columns[0]
                src_filename = table_name + "_rows.sql"
                row_names = ', '.join(columns[1:])
                with open(src_filename, "w") as src_file:
                    for row in rows:
                        row_values = ', '.join(to_sql_value(value) for value in row.split('|'))
                        final_line = src % (table_name, row_names, row_values)
                        src_file.write(final_line)