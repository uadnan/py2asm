from py2asm.instructions.base import Instruction


class Add(Instruction):
    name = 'ADD'

    def __init__(self, destination, source):
        super().__init__(destination, source)


class Adc(Instruction):
    name = 'ADC'

    def __init__(self, destination, source):
        super().__init__(destination, source)


class Sub(Instruction):
    name = 'SUB'

    def __init__(self, destination, source):
        super().__init__(destination, source)


class Sbb(Instruction):
    name = 'SBB'

    def __init__(self, destination, source):
        super().__init__(destination, source)


class Inc(Instruction):
    name = 'INC'

    def __init__(self, destination):
        super().__init__(destination)


class Dec(Instruction):
    name = 'DEC'

    def __init__(self, destination):
        super().__init__(destination)


class Cmp(Instruction):
    name = 'CMP'
    n_args = 2


class Mul(Instruction):
    name = 'MUL'
    n_args = 1


class Div(Instruction):
    name = 'DIV'
    n_args = 1


class IMul(Instruction):
    name = 'IMUL'
    n_args = 1


class IDiv(Instruction):
    name = 'IDIV'
    n_args = 1


class Cbw(Instruction):
    name = 'CBW'
    n_args = 0


class Cwd(Instruction):
    name = 'CWD'
    n_args = 0


class And(Instruction):
    name = 'AND'

    def __init__(self, destination, source):
        super().__init__(destination, source)


class Or(Instruction):
    name = 'OR'

    def __init__(self, destination, source):
        super().__init__(destination, source)


class Xor(Instruction):
    name = 'XOR'

    def __init__(self, destination, source):
        super().__init__(destination, source)


class Not(Instruction):
    name = 'NOT'
    n_args = 1


class Test(Instruction):
    name = 'TEST'
    n_args = 2


class Shl(Instruction):
    name = 'SHL'
    n_args = 2


class Shr(Instruction):
    name = 'SHR'
    n_args = 2


class Sal(Instruction):
    name = 'SAL'
    n_args = 2


class Sar(Instruction):
    name = 'SAR'
    n_args = 2


class Ror(Instruction):
    name = 'SHL'
    n_args = 2


class Rol(Instruction):
    name = 'SHR'
    n_args = 2


class Rcr(Instruction):
    name = 'SAL'
    n_args = 2


class Rcl(Instruction):
    name = 'SAR'
    n_args = 2
