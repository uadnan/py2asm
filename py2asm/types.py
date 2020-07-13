from enum import Enum

from py2asm.functions.base import Raw
from py2asm.instructions import Add, Sub, Mov


class AsmType:
    def render(self):
        pass

    def __add__(self, other):
        Raw(
            Mov(Register.AX, self),
            Add(Register.AX, other)
        )
        return self

    def __sub__(self, other):
        Raw(
            Mov(Register.AX, self),
            Sub(Register.AX, other)
        )
        return self

    def __mul__(self, other):
        raise NotImplementedError()

    def __truediv__(self, other):
        raise NotImplementedError()

    def __mod__(self, other):
        raise NotImplementedError()

    def __pow__(self, other):
        raise NotImplementedError()

    def __not__(self, other):
        raise NotImplementedError()

    def __and__(self, other):
        raise NotImplementedError()

    def __gt__(self, other):
        raise NotImplementedError()

    def __lt__(self, other):
        raise NotImplementedError()

    def __ge__(self, other):
        raise NotImplementedError()

    def __le__(self, other):
        raise NotImplementedError()


class Register(AsmType):
    def __init__(self, name):
        self.name = name

    def render(self):
        return self.name


class SegmentRegister(Register):
    pass


# SegmentRegisters:
SegmentRegister.CS = SegmentRegister('CS')
SegmentRegister.DS = SegmentRegister('DS')
SegmentRegister.ES = SegmentRegister('ES')
SegmentRegister.SS = SegmentRegister('SS')


# Data Registers
Register.AX = Register('AX')
Register.AL = Register('AL')
Register.AH = Register('AH')

Register.BX = Register('BX')
Register.BL = Register('BL')
Register.BH = Register('BH')

Register.CX = Register('CX')
Register.CL = Register('CL')
Register.CH = Register('CH')

Register.DX = Register('DX')
Register.DL = Register('DL')
Register.DH = Register('DH')

Register.IP = Register('IP')
Register.SI = Register('SI')
Register.DI = Register('DI')
Register.SP = Register('SP')
Register.BP = Register('BP')


