#encoding=utf-8
from ply.lex import lex
from ply.yacc import yacc
from nssql.ast_node import Condition, Source, Target, Gathering, Option, SQL, Expr, REF, NAME

td = """
$(branch);
$(branch)[@_name, @_city];
$(branch)[@_name, @_city]{@_name="Foo"};
$(branch)[@_name, @_city]<@_city>{@_city!="Rye"};
$(branch)[[ORDER BY @_name]];
"""

tokens = (
    'NAME',
    'CONTENT',
    'SELECTOR',
    # 'BIND',
    'LP',
    'RP',
    'LBP',
    'RBP',
    'LCP',
    'RCP',
    'LAP',
    'RAP',
    # 'AT',
    'COMMA',
)

t_NAME = r"[A-Za-z]+[_A-Za-z0-9]*"
t_CONTENT = r'[\w@]+[\w@"\'!\.=]+'
t_SELECTOR = r'\$'
# t_BIND = r'=',
t_LP = r'\('
t_RP = r'\)'
t_LBP = r'\['
t_RBP = r'\]'
t_LCP = r'\{'
t_RCP = r'\}'
t_LAP = r'<'
t_RAP = r'>'
t_COMMA = r','
t_ignore = ' \n\r;'


def t_error(t):
    raise ValueError(t)


lexer = lex()


def p_collection(p):
    """
    collection : sql
               | collection sql
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]


def p_sql(p):
    """
    sql : select
        | sql from
        | sql condition
        | sql gathering
        | sql option
    """
    if len(p) == 2:
        p[0] = SQL(p[1])
        p[0].source = p[1]
    else:
        if isinstance(p[2], Target) and isinstance(p[1], SQL):
            p[1].target = p[2]
        elif isinstance(p[2], Condition):
            p[1].condition = p[2]
        elif isinstance(p[2], Gathering):
            p[1].gathering = p[2]
        elif isinstance(p[2], Option):
            p[1].option = p[2]
        else:
            raise TypeError(p[2])
        p[0] = p[1]


def p_expr(p):
    """
    expr : CONTENT
         | NAME
         | expr NAME
         | expr CONTENT
         | expr COMMA CONTENT
         | expr COMMA NAME
    """
    if len(p) == 2:
        p[0] = Expr(p[1])
    if len(p) == 3:
        p[1].append(p[2])
        p[0] = p[1]
    if len(p) == 4:
        p[1].append(p[3])
        p[0] = p[1]


def p_gathering(p):
    """
    gathering : LAP expr RAP
    """
    p[0] = Gathering(p[2])


def p_select_content(p):
    """
    select : SELECTOR LP expr RP
    """
    p[0] = Source(NAME, p[3])


def p_select_name(p):
    """
    select : SELECTOR expr
    """
    p[0] = Source(REF, p[2])


def p_condition(p):
    """
    condition : LCP expr RCP
    """
    p[0] = Condition(p[2])


def p_from(p):
    """
    from : LBP expr RBP
    """
    p[0] = Target(p[2])


def p_option(p):
    """
    option : LBP LBP expr RBP RBP
    """
    p[0] = Option(p[3])


def p_error(p):
    print(p)


parser = yacc()
res = parser.parse(td, debug=0)
print('\n'.join(map(str, res)))
