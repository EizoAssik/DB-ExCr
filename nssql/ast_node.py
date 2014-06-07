#encoding=utf-8

from rply.token import BaseBox

NAME = 0
REF = 1


class Clause(BaseBox):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return self.value

    def __repr__(self):
        return '<SQL # {eval}>'.format(eval=self.eval())

    def __str__(self):
        return self.eval()


class Empty(Clause):
    def __init__(self, value, *args, **kwargs):
        super().__init__(value)

    def eval(self, *args, **kwargs):
        return ''


_empty = Empty(None)


class Expr(BaseBox):
    def __init__(self, elem):
        self.value = [elem]

    def append(self, elem):
        self.value.append(elem)

    def __str__(self):
        return self.eval()

    def eval(self, split_with_comma=False):
        join_char = ', ' if split_with_comma else ' '
        return join_char.join(map(str, self.value))


class Source(Clause):
    def __init__(self, t, value: Expr):
        super().__init__(value)
        self.type = t

    def eval(self):
        if self.type is REF:
            return '({}) as {}'.format(self.value.eval(), 'REF-NAME')
        elif self.type is NAME:
            return self.value.eval(split_with_comma=True)


class Target(Clause):
    def __init__(self, value: Expr):
        super().__init__(value)

    def eval(self):
        return self.value.eval(split_with_comma=True)


class Condition(Clause):
    def __init__(self, value: Expr):
        super().__init__(value)

    def eval(self):
        return self.value.eval()


class Gathering(Clause):
    def __init__(self, value: Expr):
        super().__init__(value)

    def eval(self):
        if self.value:
            return 'GROUP BY {}'.format(self.value.eval())
        return ''


class Option(Clause):
    def __init__(self, value: Expr):
        super().__init__(value)

    def eval(self):
        return self.value.eval()


class SQL(Clause):
    def __init__(self, value: str):
        super().__init__(value)
        self.condition = _empty
        self.gathering = _empty
        self.source = _empty
        self.target = _empty
        self.option = _empty

    def eval(self):
        template = "SELECT{target} FROM{source}{gather}{condition}{option};"
        tn = self.source.eval()
        sql_args = {
            'target': (self.target.eval(), ' *'),
            'source': (self.source.eval(), ' *'),
            'gather': (self.gathering.eval(), ''),
            'condition': (self.condition.eval(), ''),
            'option': (self.option.eval(), '')
        }
        for key, val in sql_args.items():
            sql_args[key] = ' ' + val[0] if val[0] else val[1]
        if sql_args['condition']:
            condition_expr = self.condition.eval()
            condition_prefix = 'HAVING' if sql_args['gather'] else 'WHERE'
            sql_args['condition'] = '{} {}'.format(condition_prefix, condition_expr)
        expr = template.format(**sql_args)
        expr = expr.replace('@', tn)
        return expr