from py2asm.constants import JumpTypes
from py2asm.functions.base import Raw
from py2asm.instructions import Add, Sub, Mov, Cmp, IMul, IDiv, Cbw, And, Not, Nop
from .operatable import Operatable
from .utils import is_byte


class AsmType(Operatable):
    def render(self):
        pass

    def is_byte(self):
        pass

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def __mul__(self, other):
        return self.mul(other)

    def __truediv__(self, other):
        return self.div(other)

    def __mod__(self, other):
        return self.mod(other)

    def __not__(self):
        return self.not_()

    def __and__(self, other):
        return self.add(other)

    def __gt__(self, other):
        from .registers import Register
        return (
            (
                Mov(Register.AL, self),
                Cmp(Register.AL, other)
            ),
            JumpTypes.JumpGreater
        )

    def __lt__(self, other):
        from .registers import Register
        return (
            (
                Mov(Register.AL, self),
                Cmp(Register.AL, other)
            ),
            JumpTypes.JumpLess
        )

    def __ge__(self, other):
        from .registers import Register
        return (
            (
                Mov(Register.AL, self),
                Cmp(Register.AL, other)
            ),
            JumpTypes.JumpGreaterEqual
        )

    def __le__(self, other):
        from .registers import Register
        return (
            (
                Mov(Register.AL, self),
                Cmp(Register.AL, other)
            ),
            JumpTypes.JumpLessEqual
        )

    def __eq__(self, other):
        from .registers import Register
        return (
            (
                Mov(Register.AL, self),
                Cmp(Register.AL, other)
            ),
            JumpTypes.JumpEqual
        )