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

    from py2asm.data import DefineFunction

    if isinstance(arg, DefineFunction):
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
