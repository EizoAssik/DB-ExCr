#!/bin/python3
"""
CREATED AT 4/24/14 12:47 PM AS A PART OF Project DBSC
"""

from schema import parse
from translator import translate
from sys import argv


def main():
    if len(argv) > 1:
        fn = argv[1]
    else:
        fn = 'tables.schema'
    p = parse(fn)
    nm = fn.split('.')[0]
    tg = '.'.join(fn.split('.')[:-1]+['sql'])
    s = ['USE %s;\n\n' % nm] + translate(p)
    with open(tg, 'w') as f:
        f.writelines(s)
        
        
if __name__ == '__main__':
    main()
