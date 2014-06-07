#encoding=utf-8
LEXER_RULES = [
    ('NAME', r'[A-Za-z]+[_A-Za-z0-9]*'),
    ('CONTENT', r'[\w@]+[\w@"\'!\.=]+'),
    ('SELECTOR', r'\$'),
    # ('BIND', r'='),
    ('LP', r'\('),
    ('RP', r'\)'),
    ('LBP', r'\['),
    ('RBP', r'\]'),
    ('LCP', r'\{'),
    ('RCP', r'\}'),
    ('LAP', r'<'),
    ('RAP', r'>'),
    # ('AT', r'@'),
    ('COMMA', r',')
]

LEXER_IGNORE = r'[\s;]'

TOKEN_NAMES = list(zip(*LEXER_RULES))[0]

PRODUCTION = r"""
SQL -> SELECT
     | SQL FROM
     | SQL CONDITION
     | SQL GATHERING

SELECT -> SELECTOR LP CONTENT RP
        | SELECTOR NAME

FROM   -> LBP CONTENT RBP

CONDITION -> LCP CONTENT RCP

GATHERING -> LAP CONTENT RAP
"""

