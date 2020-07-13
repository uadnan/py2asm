from py2asm.instructions.base import Instruction


class Add(Instruction):
    name = 'ADD'

    def __init__(self, destination, source):
        super().__init__(destination, source)


class Sub(Instruction):
    name = 'SUB'

    def __init__(self, destination, source):
        super().__init__(destination, source)