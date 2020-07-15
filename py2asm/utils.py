from enum import Enum


class SafeStr(str):
    pass


def format_number(n):
    n = '{:02X}'.format(n)
    if len(n) % 2 != 0:
        n = '0' + n

    if not n[0].isdigit():
        n = '0' + n

    return n + 'h'


def format_argument(arg):
    if isinstance(arg, int):
        return format_number(arg)

    if isinstance(arg, SafeStr):
        return arg

    from py2asm.variables import Variable, Define
    from py2asm.types import Register

    if isinstance(arg, Variable) or isinstance(arg, Register) or isinstance(arg, Define):
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
