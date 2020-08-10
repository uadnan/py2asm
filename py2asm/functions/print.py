import threading
from enum import Enum

from py2asm.blocks import Program
from py2asm.data import Variable
from py2asm.registers import Register
from py2asm.functions.base import Function, Raw
from py2asm.functions.groups import BiosProcedureCall
from py2asm.instructions import Lea, Mov, Cbw, Call, Add
from py2asm.utils import format_argument, is_byte

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
        if is_byte(self.data_var):
            return (
                Mov(Register.AL, self.data_var),
                Cbw(),
                Call("PRINT_NUM")
            )

        return (
            Mov(Register.AX, self.data_var),
            Call("PRINT_NUM")
        )


class PrintNumChar(Function):
    def __init__(self, data):
        if not isinstance(data, (int, Variable, Register)):
            raise ValueError('Unsupported type: {}'.format(type(data)))

        self.data_var = data
        super().__init__()

    def get_instructions(self):
        reg = Register.DL if is_byte(self.data_var) else Register.DX
        return (
            Mov(reg, self.data_var),
            Add(Register.DL, '0'),
            BiosProcedureCall(0x2)
        )


class PrintType(Enum):
    PRINT_STR = PrintStr
    PRINT_STR_BUILTIN = PrintStrBuiltin
    PRINT_CHAR = PrintChar
    PRINT_NUM_CHAR = PrintNumChar
    PRINT_NUM_BUILTIN = PrintNum
    # TODO: PRINT_NUM


class Print:
    def __init__(self, data, print_type=None):
        self.data = data

        if print_type is not None:
            self.printer = print_type
        elif isinstance(data, str) and len(data) > 1:
            self.printer = PrintType.PRINT_STR_BUILTIN
        elif isinstance(data, str) and len(data) == 1:
            self.printer = PrintType.PRINT_CHAR
        elif isinstance(data, int):
            self.printer = PrintType.PRINT_NUM_BUILTIN
        else:
            raise ValueError("print fn_type must be specified for data of type {}".format(type(data)))

        self.printer = self.printer.value(self.data)

    def get_instructions(self):
        return self.printer.get_instructions()
