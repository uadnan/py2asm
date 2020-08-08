from enum import Enum

from py2asm.types import AsmType
from py2asm.instructions import Mov
from py2asm.functions import Raw


class RegisterType(AsmType):
    def __init__(self, name, is_byte=True):
        self.name = name
        self.is_byte_reg = is_byte

    def render(self):
        return self.name

    def __ilshift__(self, other):
        Raw(Mov(self, other))
        return self

    def is_byte(self):
        return self.is_byte_reg


class SegmentRegisterType(RegisterType):
    pass


class Register:
    AX = RegisterType('AX', False)
    AL = RegisterType('AL')
    AH = RegisterType('AH')

    BX = RegisterType('BX', False)
    BL = RegisterType('BL')
    BH = RegisterType('BH')

    CX = RegisterType('CX', False)
    CL = RegisterType('CL')
    CH = RegisterType('CH')

    DX = RegisterType('DX', False)
    DL = RegisterType('DL')
    DH = RegisterType('DH')

    IP = RegisterType('IP', False)
    SI = RegisterType('SI', False)
    DI = RegisterType('DI', False)
    SP = RegisterType('SP', False)
    BP = RegisterType('BP', False)

    CS = SegmentRegisterType('CS', False)
    DS = SegmentRegisterType('DS', False)
    ES = SegmentRegisterType('ES', False)
    SS = SegmentRegisterType('SS', False)
