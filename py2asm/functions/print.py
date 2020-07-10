from py2asm.constants import Register
from py2asm.data import DefineFunction
from py2asm.functions.base import Function
from py2asm.functions.groups import BiosProcedureCall
from py2asm.instructions.transfer import Lea, Mov


class PrintString(Function):
    def __init__(self, data_var):
        if not isinstance(data_var, (int, DefineFunction)):
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
        if not isinstance(data_var, (int, str, DefineFunction, Register)):
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
