from enum import Enum


class SafeStr(str):
    pass


def format_number(n):
    s = '{:02X}'.format(abs(n))
    if len(s) % 2 != 0:
        s = '0' + s

    if not s[0].isdigit():
        s = '0' + s

    return ('-' if n < 0 else '') + s + 'h'


def format_argument(arg):
    if isinstance(arg, int):
        return format_number(arg)

    if isinstance(arg, SafeStr):
        return arg

    from py2asm.data import Variable, Define
    from py2asm.registers import Register, RegisterType
    from py2asm.functions import Raw

    if isinstance(arg, (Variable, Register, RegisterType, Define)):
        return arg.name

    if isinstance(arg, str):
        if len(arg) == 1:
            return '\'{}\''.format(arg)

        return '"{}"'.format(arg)

    if isinstance(arg, Enum):
        return arg.value

    raise NotImplementedError('{} (type: {}) is not supported'.format(arg, type(arg)))


def mark_safe(s):
    return SafeStr(s)


def is_byte(value):
    from .types import AsmType
    if type(value) == int and value < 255:
        return True
    elif isinstance(value, AsmType):
        return value.is_byte()
