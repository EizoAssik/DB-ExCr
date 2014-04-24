"""
CREATED AT 4/24/14 12:47 PM AS A PART OF Project DBSC
"""

from schema import parse
from translator import translate

if __name__ == '__main__':
    p = parse('tables.schema')
    s = translate(p)
    with open('tables.sql', 'w') as f:
        f.writelines(s)