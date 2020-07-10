from py2asm.instructions.base import Instruction


class Lea(Instruction):
    name = 'LEA'

    def __init__(self, register, memory):
        super().__init__(register, memory)


class Mov(Instruction):
    name = 'MOV'
    n_args = 2

    def __init__(self, destination, source):
        super().__init__(destination, source)
