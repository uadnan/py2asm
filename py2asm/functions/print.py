import threading
from enum import Enum

from py2asm.blocks import Program
from py2asm.data import Variable
from py2asm.types import Register
from py2asm.functions.base import Function, Raw
from py2asm.functions.groups import BiosProcedureCall
from py2asm.instructions import Lea, Mov, Call
from py2asm.utils import format_argument

_state = threading.local()


class PrintStr(Function):
    def __init__(self, data):
        if not isinstance(data, (int, Variable)):
            raise ValueError('Unsupported type: {}'.format(type(data)))

        self.data_var = data
        super().__init__()

    def get_instructions(self):
        return (
            Lea(Register.DX, self.data_var),
            BiosProcedureCall(0x9)
        )


class PrintChar(Function):
    def __init__(self, data):
        if not isinstance(data, (int, str, Variable, Register)):
            raise ValueError('Unsupported type: {}'.format(type(data)))

        if isinstance(data, str) and len(data) != 1:
            raise ValueError('Invalid string length: {}'.format(len(data)))

        self.data_var = data
        super().__init__()

    def get_instructions(self):
        return (
            Mov(Register.DL, self.data_var),
            BiosProcedureCall(0x2)
        )


class PrintStrBuiltin(Function):
    def __init__(self, data):
        if not isinstance(data, (str, Variable)):
            raise ValueError('Unsupported type: {}'.format(type(data)))

        self.data = data
        Program.get_current().includes.add('emu8086.inc')
        super().__init__()

    def get_instructions(self):
        return (
            Raw(
                "{name:<8} {operand}".format(
                    name="PRINT",
                    operand=format_argument(self.data)
                ),
                should_register=False
            ),
        )


class PrintNum(Function):
    def __init__(self, data):
        if not isinstance(data, (int, Variable, Register)):
            raise ValueError('Unsupported type: {}'.format(type(data)))

        self.data_var = data
        Program.get_current().includes.add('emu8086.inc')
        Program.get_current().defines.add('DEFINE_PRINT_NUM_UNS')
        Program.get_current().defines.add('DEFINE_PRINT_NUM')
        super().__init__()

    def get_instructions(self):
        return (
            Mov(Register.AX, self.data_var),
            Call("PRINT_NUM")
        )


class PrintType(Enum):
    PRINT_STR = PrintStr
    PRINT_STR_BUILTIN = PrintStrBuiltin
    PRINT_CHAR = PrintChar
    PRINT_NUM_BUILTIN = PrintNum
    # TODO: PRINT_NUM


class Print(Function):
    def __init__(self, data, fn_type):
        self.data = data
        self.fn_type = fn_type

    def get_instructions(self):
        return self.fn_type(self.data).get_instructions()
