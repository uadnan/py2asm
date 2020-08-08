from py2asm.blocks import Program
from py2asm.utils import mark_safe, format_argument
from py2asm.instructions import Add, Sub, Mov, Inc, Dec
from py2asm.functions.base import Raw
from py2asm.types import AsmType
from py2asm.registers import Register


class Define(AsmType):
    template = '{name:<16} EQU  {value}'

    def __init__(self, name, value):
        self.name = name
        self.value = value

        Program.get_current().define_data(self)

    def render(self):
        return self.template.format(
            name=self.name,
            value=self.value
        )

    def is_byte(self):
        if type(self.value) == int and self.value < 255:
            return True
        elif type(self.value) == Variable and self.value.is_byte:
            return True
        return None


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
        if other == 1:
            Raw(Inc(self))
        else:
            Raw(Add(self, other))
        return self

    def __isub__(self, other):
        if other == 1:
            Raw(Dec(self))
        else:
            Raw(Sub(self, other))
        return self

    def __ilshift__(self, other):
        if isinstance(other, Variable):
            reg = Register.DL if other.var_type == VariableType.BYTE else Register.DX
            Raw(
                Mov(reg, other),
                Mov(self, reg),
            )
        else:
            Raw(Mov(self, other))
        return self

    def is_byte(self):
        return self.var_type == VariableType.BYTE
