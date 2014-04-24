"""
CREATED AT 4/24/14 12:58 PM AS A PART OF Project DBSC
提供中间格式向MariaDB转换的一些方法
好吧 现在这些代码很是不优雅
"""

TABLES = []
CURRENT = None


def translate(schema):
    r = [translate_cine(cine) for cine in schema]
    TABLES.clear()
    CURRENT = None
    return r


def join_comma(items):
    return ', '.join(items)


def join_cnt(items):
    return ',\n\t'.join(items)


def translate_cine(cine):
    global CURRENT, TABLES
    src = "CREATE TABLE IF NOT EXISTS %s\n\t(%s);\n\n"
    table_name = cine[0][0]
    CURRENT = list()
    TABLES.append([table_name, CURRENT])
    items = join_cnt([translate_term(t) for t in cine[1]])
    pris = join_comma([t[0] for t in cine[1] if t[1]])
    refs = [find_ref(t[0]) for t in cine[1] if t[2]]
    contains = items + ',\n\t' + "PRIMARY KEY(" + pris + ")" + (',\n\t' if len(refs) > 0 else '')
    contains += join_cnt(["FOREIGN KEY(%s) REFERENCES %s(%s)" % r for r in refs])
    return src % (table_name, contains)


def translate_term(term):
    name, primary, ref, t = term
    CURRENT.append(name)
    return "%s %s" % (name, translate_type(t))


def find_ref(name):
    for table in TABLES:
        table_name = table[0]
        columns = table[1]
        if name in columns:
            return name, table_name, name
    raise KeyError()


def translate_type(t):
    if t is None:
        # 对于MariaDB的InnoDB引擎, VARCHAR更合适
        return 'VARCHAR(64)'
    else:
        return '%s(%s)' % (t[0], ','.join(x[0] for x in t[1]))