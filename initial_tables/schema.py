"""
CREATED AT 4/24/14 11:10 AM AS A PART OF Project DBSC
"""

from ply import yacc, lex

tokens = ('NAME', 'REF', 'PRI', 'LP', 'RP', 'LSP', 'RSP', 'LCP', 'RCP', 'COMMA')
t_NAME = r"[A-Za-z0-9_]+"
t_REF = r"\*"
t_PRI = r"\+"
t_LP = r'\('
t_RP = r'\)'
t_LSP = r'\['
t_RSP = r"\]"
t_LCP = r'\{'
t_RCP = r'\}'
t_COMMA = r','
t_ignore = ' \n\r\tS;'


# CREATE IF NOT EXISTS ...
def p_schema(p):
    """ schema : cine
               | schema cine
    """
    if len(p) is 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]


# cine, CREATE TABLE IF NOT EXISTS
def p_cine(p):
    """ cine : term LCP terms RCP """
    # cine 是一个 term - terms 对
    p[0] = (p[1], p[3])


def p_type(p):
    """ type : NAME LP terms RP """
    # type 是一个 NAME - terms 对
    p[0] = (p[1], p[3])


def p_term(p):
    """ term : NAME
             | REF term
             | PRI term
             | term LSP type RSP
    """
    # term是一个四元组
    # (NAME, isPrimary, isForeign, type/None)
    if len(p) is 2:
        p[0] = (p[1], False, False, None)
    if len(p) is 3:
        if p[1] is '+':
            p[0] = (p[2][0], True, p[2][2], None)
        if p[1] is '*':
            p[0] = (p[2][0], p[2][1], True, None)
    if len(p) is 5:
        p[0] = (p[1][0], p[1][1], p[1][2], p[3])


def p_terms(p):
    """ terms : term
              | terms COMMA
              | terms COMMA term
    """
    # terms 是一或多个 term 构成的 list
    if len(p) is 2:
        p[0] = [p[1]]
    if len(p) is 3:
        p[0] = p[1]
    if len(p) is 4:
        p[0] = p[1] + [p[3]]


def parse(filename):
    lexer = lex.lex()
    parser = yacc.yacc()
    with open(filename) as file:
        schema = file.read()
        r = parser.parse(schema, debug=0)
    return r