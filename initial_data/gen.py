#encoding=utf-8
# 这个简单的脚本支持Python2.7/Python3.3
# 定义转换规则
TRANS_RULE = [(int, lambda x: str(x)),
              (float, lambda x: str(x)),
              ('None', lambda x: 'NULL'),
              (str, lambda x: "'%s'" % x.lstrip().rstrip()),
              (None, lambda x: 'NULL')]


# 解释转换规则
def to_sql_value(term):
    for schema, transformer in TRANS_RULE:
        if isinstance(schema, type):
            try:
                v = transformer(schema(term))
                return v
            except ValueError:
                pass
        elif schema is not None:
            if term.lstrip().rstrip() == schema:
                return transformer(term)
        else:
            return transformer(term)


def clear_whitespace(s):
    return s.lstrip().rstrip()


def translate(file, name):
    rows = file.readlines()
    src = []
    if len(rows) < 1:
        return []
    title = ', '.join([clear_whitespace(t) for t in rows[0].split('|')])
    template = "INSERT INTO %s(%s) VALUES (%s);\n"
    for row in rows[1:]:
        if row.startswith('--'):
            continue
        values = ', '.join([to_sql_value(t) for t in row.split('|')])
        src.append(template % (name, title, values))
    return src


def translate_seq(file):
    for line in sequence:
        columns = line.split()
        name = columns[0]
        with open(name + '.rows') as file:
            src = translate(file, name)
            with open(name + '.sql', 'w') as target:
                target.writelines(src)


import sys

if __name__ == '__main__':
    SEQUENCE = []
    if len(sys.argv) >= 2:
        SEQUENCE = sys.argv[1:]
    for filename in SEQUENCE:
        with open(filename) as sequence:
            translate_seq(sequence)

