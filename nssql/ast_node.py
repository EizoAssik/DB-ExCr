#encoding=utf-8

from rply.token import BaseBox

NAME = 0
REF = 1
QUERY = 2


class Clause(BaseBox):
    def __init__(self, value):
        self.parent = None
        self.root = None
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


class Args(BaseBox):
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
    def __init__(self, t, value: Args):
        super().__init__(value)
        self.type = t

    def eval(self):
        if self.type is REF:
            symbol = self.value.eval()
            return '({}) as {}'.format(self.parent.root.symbols[symbol].eval(),
                                       symbol)
        elif self.type is NAME:
            return self.value.eval(split_with_comma=True)
        elif self.type is QUERY:
            return self.value.eval()


class Target(Clause):
    def __init__(self, value: Args):
        super().__init__(value)

    def eval(self):
        return self.value.eval(split_with_comma=True)


class Condition(Clause):
    def __init__(self, value: Args):
        super().__init__(value)

    def eval(self):
        return self.value.eval()


class Gathering(Clause):
    def __init__(self, value: Args):
        super().__init__(value)

    def eval(self):
        if self.value:
            return 'GROUP BY {}'.format(self.value.eval())
        return ''


class Option(Clause):
    def __init__(self, value: Args):
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
        self.bind_name = None

    def set_source(self, source):
        source.parent = self
        self.source = source

    def set_target(self, target):
        target.parent = self
        self.target = target

    def set_cond(self, cond):
        cond.parent = self
        self.condition = cond

    def set_gathering(self, ga):
        ga.parent = self
        self.gathering = ga

    def set_option(self, op):
        op.parent = self
        self.option = op

    def eval(self):
        template = "SELECT{target} FROM{source}{gather}{condition}{option}"
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


class Collection(object):
    def __init__(self, elements: list):
        self.elements = elements
        self.symbols = {}
        for elem in self.elements:
            if elem.bind_name:
                self.symbols[elem.bind_name] = elem
            elem.root = self

    def dumps(self):
        src = filter(lambda x: not x.bind_name, self.elements)
        return list(map(str, src))