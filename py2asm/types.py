from py2asm.constants import JumpTypes
from py2asm.functions.base import Raw
from py2asm.instructions import Add, Sub, Mov, Cmp, IMul, IDiv, Cbw, And, Not, Nop
from .utils import is_byte


class AsmType:
    def render(self):
        pass

    def is_byte(self):
        pass

    def __add__(self, other):
        Raw(
            Mov(Register.AX, self),
            Add(Register.AX, other)
        )
        return Register.AX

    def __sub__(self, other):
        Raw(
            Mov(Register.AX, self),
            Sub(Register.AX, other)
        )
        return Register.AX

    def __mul__(self, other):
        if is_byte(other):
            op1 = Register.AL
        else:
            op1 = Register.AX

        if is_byte(self):
            op2 = Register.BL
        else:
            op2 = Register.BX

        Raw(
            Mov(op1, other),
            Mov(op2, self),
            IMul(op2)
        )
        # TODO: handle DX also
        return Register.AX

    def __truediv__(self, other):
        if is_byte(self):
            op1 = Register.AL
            op2 = Register.BL
        else:
            op1 = Register.AX
            op2 = Register.BX

        Raw(
            Mov(op2, other),
            Mov(op1, self),
            IDiv(op2)
        )
        if is_byte(self):
            return Register.AL
        else:
            return Register.AX

    def __mod__(self, other):
        if is_byte(self):
            op1 = Register.AL
            op2 = Register.BL
        else:
            op1 = Register.AX
            op2 = Register.BX


        Raw(
            Mov(op2, other),
            Mov(op1, self),
            IDiv(op2)
        )
        if is_byte(self):
            return Register.AH
        else:
            return Register.DX

    def __not__(self):
        Raw(
            Mov(Register.AX, self),
            Not(Register.AX)
        )
        return Register.AX

    def __and__(self, other):
        Raw(
            Mov(Register.AX, self),
            And(Register.AX, other)
        )
        return Register.AX

    def __gt__(self, other):
        return (
            (
                Mov(Register.AL, self),
                Cmp(Register.AL, other)
            ),
            JumpTypes.JumpGreater
        )

    def __lt__(self, other):
        return (
            (
                Mov(Register.AL, self),
                Cmp(Register.AL, other)
            ),
            JumpTypes.JumpLess
        )

    def __ge__(self, other):
        return (
            (
                Mov(Register.AL, self),
                Cmp(Register.AL, other)
            ),
            JumpTypes.JumpGreaterEqual
        )

    def __le__(self, other):
        return (
            (
                Mov(Register.AL, self),
                Cmp(Register.AL, other)
            ),
            JumpTypes.JumpLessEqual
        )


class Register(AsmType):
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


class SegmentRegister(Register):
    pass


# SegmentRegisters:
SegmentRegister.CS = SegmentRegister('CS', False)
SegmentRegister.DS = SegmentRegister('DS', False)
SegmentRegister.ES = SegmentRegister('ES', False)
SegmentRegister.SS = SegmentRegister('SS', False)


# DataRegisters
Register.AX = Register('AX', False)
Register.AL = Register('AL')
Register.AH = Register('AH')

Register.BX = Register('BX', False)
Register.BL = Register('BL')
Register.BH = Register('BH')

Register.CX = Register('CX', False)
Register.CL = Register('CL')
Register.CH = Register('CH')

Register.DX = Register('DX', False)
Register.DL = Register('DL')
Register.DH = Register('DH')

Register.IP = Register('IP', False)
Register.SI = Register('SI', False)
Register.DI = Register('DI', False)
Register.SP = Register('SP', False)
Register.BP = Register('BP', False)

