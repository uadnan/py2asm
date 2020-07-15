from py2asm.instructions.base import Instruction


class Call(Instruction):
    name = 'CALL'

    def __init__(self, proc_name):
        super().__init__(proc_name)

    def render(self):
        return '{name:<8} {proc}'.format(name=self.name, proc=self.args[0])


class Ret(Instruction):
    name = 'RET'

    def __init__(self):
        super().__init__()
