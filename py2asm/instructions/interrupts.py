from py2asm.instructions.base import Instruction


class Int(Instruction):
    name = 'INT'

    def __init__(self, immediate_byte):
        super().__init__(immediate_byte)
