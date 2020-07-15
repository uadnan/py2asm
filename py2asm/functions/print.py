import threading

from py2asm.blocks import Program
from py2asm.variables import Variable
from py2asm.types import Register
from py2asm.functions.base import Function
from py2asm.functions.groups import BiosProcedureCall
from py2asm.instructions import Lea, Mov, Call

_state = threading.local()


class PrintString(Function):
    def __init__(self, data_var):
        if not isinstance(data_var, (int, Variable)):
            raise ValueError('Unsupported type: {}'.format(type(data_var)))

        self.data_var = data_var
        super().__init__()

    def get_instructions(self):
        return (
            Lea(Register.DX, self.data_var),
            BiosProcedureCall(0x9)
        )


class PrintChar(Function):
    def __init__(self, data_var):
        if not isinstance(data_var, (int, str, Variable, Register)):
            raise ValueError('Unsupported type: {}'.format(type(data_var)))

        if isinstance(data_var, str) and len(data_var) != 1:
            raise ValueError('Invalid string length: {}'.format(len(data_var)))

        self.data_var = data_var
        super().__init__()

    def get_instructions(self):
        return (
            Mov(Register.DL, self.data_var),
            BiosProcedureCall(0x2)
        )


class PrintNum(Function):
    def __init__(self, data_var):
        if not isinstance(data_var, (int, Variable, Register)):
            raise ValueError('Unsupported type: {}'.format(type(data_var)))

        self.data_var = data_var
        Program.get_current().includes.add('emu8086.inc')
        Program.get_current().defines.add('DEFINE_PRINT_NUM_UNS')
        Program.get_current().defines.add('DEFINE_PRINT_NUM')
        super().__init__()

    def get_instructions(self):
        # TODO: add call instruction
        return (
            Mov(Register.AX, self.data_var),
            Call("PRINT_NUM")
        )
