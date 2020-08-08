from .functions.base import Raw
from .instructions import *
from .utils import is_byte


class Operatable:
    def is_byte(self):
        raise NotImplementedError()

    def mov(self, other: 'Operatable') -> 'Operatable':
        Raw(Mov(other, self))
        return other

    #########
    # Arithmetic Operators

    def add(self, other: 'Operatable', with_carry=False) -> 'Operatable':
        """
        Affected Registers: AX
        Affected Flags: CF, ZF, SF, OF, PF, AF
        """
        from .registers import Register, RegisterType

        op1 = self if type(self) is RegisterType else self.mov(Register.AX)

        Raw(Adc(op1, other) if with_carry else Add(op1, other))
        return Register.AX

    def sub(self, other: 'Operatable', with_borrow=False) -> 'Operatable':
        """
        Affected Registers: AX
        Affected Flags: CF, ZF, SF, OF, PF, AF
        """
        from .registers import Register, RegisterType

        op1 = self if type(self) is RegisterType else self.mov(Register.AX)

        Raw(Sbb(op1, other) if with_borrow else Sub(op1, other))
        return Register.AX

    def compare(self, other: 'Operatable') -> None:
        """
        Affected Registers: AX
        Affected Flags: CF, ZF, SF, OF, PF, AF
        """
        from .registers import Register, RegisterType

        op1 = self if type(self) is RegisterType else self.mov(Register.AX)

        Raw(Cmp(op1, other))
        return None

    def mul(self, other: 'Operatable', signed=False) -> 'Operatable':
        from .registers import Register
        op1 = Register.AL if is_byte(other) else Register.AX
        op2 = Register.BL if self.is_byte() else Register.BX

        Raw(
            Mov(op2, self),
            Mov(op1, other),
            IMul(op2) if signed else Mul(op2)
        )
        return Register.AX

    def div(self, other: 'Operatable', signed=False) -> 'Operatable':
        from .registers import Register
        op1 = Register.AL if self.is_byte() else Register.AX
        op2 = Register.BL if self.is_byte() else Register.BX

        Raw(
            Mov(op2, other),
            Mov(op1, self),
            IDiv(op2) if signed else Div(op2)
        )

        return Register.AL if self.is_byte() else Register.AX

    def mod(self, other: 'Operatable', signed=False) -> 'Operatable':
        from .registers import Register
        self.div(other, signed)
        return Register.AH if self.is_byte() else Register.DX

    #########
    # Logical Operators

    def not_(self) -> 'Operatable':
        """
        Invert each bit of the operand.

        No Register affected
        No flag affected
        """
        Raw(Not(self))
        return self

    def and_(self, other: 'Operatable') -> 'Operatable':
        from .registers import Register, RegisterType
        op1 = self if type(self) is RegisterType else self.mov(Register.AX)
        Raw(And(op1, other))
        return Register.AX

    def test(self, other: 'Operatable') -> None:
        from .registers import Register, RegisterType
        op1 = self if type(self) is RegisterType else self.mov(Register.AX)
        Raw(Test(op1, other))
        return None

    def or_(self, other: 'Operatable') -> 'Operatable':
        from .registers import Register
        op1 = self if type(self) is Register else self.mov(Register.AX)
        Raw(Or(op1, other))
        return Register.AX

    def xor(self, other: 'Operatable') -> 'Operatable':
        from .registers import RegisterType, Register
        op1 = self if type(self) is RegisterType else self.mov(Register.AX)
        Raw(Xor(op1, other))
        return Register.AX

    #########
    # Shift Operators

    def shift_left(self, n: int) -> 'Operatable':
        Raw(Shl(self, n))
        return self

    def shift_right(self, n: int) -> 'Operatable':
        Raw(Shr(self, n))
        return self

    def shift_arithmetic_left(self, n) -> 'Operatable':
        Raw(Sal(self, n))
        return self

    def shift_arithmetic_right(self, n) -> 'Operatable':
        Raw(Sar(self, n))
        return self

    #########
    # Rotate Operators

    def rotate_left(self, n: int) -> 'Operatable':
        Raw(Rol(self, n))
        return self

    def rotate_right(self, n: int) -> 'Operatable':
        Raw(Ror(self, n))
        return self

    def rotate_carry_left(self, n) -> 'Operatable':
        Raw(Rcl(self, n))
        return self

    def rotate_carry_right(self, n) -> 'Operatable':
        Raw(Rcr(self, n))
        return self
