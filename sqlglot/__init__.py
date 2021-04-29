from sqlglot.dialects import Dialect
from sqlglot.expressions import Expression
from sqlglot.generator import Generator
from sqlglot.tokens import Tokenizer, TokenType
from sqlglot.parser import Parser


__version__ = '0.17.3'


def parse(code, read=None):
    dialect = Dialect.get(read, Dialect)()
    return dialect.parse(code)


def transpile(code, read=None, write=None, identity=True, **opts):
    write = write or read if identity else write
    return [
        Dialect.get(write, Dialect)().generate(expression, **opts)
        for expression in parse(code, read)
    ]
