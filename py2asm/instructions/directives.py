from py2asm.instructions.base import Instruction


class Include(Instruction):
    def __init__(self, name):
        super().__init__()

    def render(self):
        pass
