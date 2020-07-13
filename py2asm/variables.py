from enum import Enum

from py2asm.blocks import Program
from py2asm.formatting import mark_safe, format_argument
from py2asm.instructions import Add, Sub, Mov
from py2asm.functions.base import Raw
from py2asm.types import AsmType


class VariableType:
    BYTE = 'DB'
    WORD = 'DW'
    DOUBLE_WORD = 'DD'
    QUARD_WORD = 'DQ'
    TEN_BYTE = 'TB'


class Variable(AsmType):
    EMPTY = mark_safe('?')
    template = '{name:<16} {directive:<4} {initializers}'

    def __init__(self, name, var_type=VariableType.BYTE, *initializers):
        if len(initializers) == 0:
            initializers = (self.EMPTY,)

        self.name = name
        self.var_type = var_type
        self.initializers = initializers

        Program.get_current().define_data(self)

    def render(self):
        return self.template.format(
            name=self.name,
            directive=self.var_type,
            initializers=', '.join(
                format_argument(init)
                for init in self.initializers
            )
        )

    def __iadd__(self, other):
        Raw(Add(self, other))
        return self

    def __isub__(self, other):
        Raw(Sub(self, other))
        return self

    def __ilshift__(self, other):
        Raw(Mov(self, other))
        return self
