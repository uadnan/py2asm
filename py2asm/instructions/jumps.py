from py2asm.instructions.base import Instruction


class JumpInstruction(Instruction):
    template = '{name:<8} {label}'

    def __init__(self, label):
        self.label = label

        super().__init__(label)

    def render(self):
        return self.template.format(
            name=self.name,
            label=self.label
        )


class Je(JumpInstruction):
    name = 'JE'


class Jne(JumpInstruction):
    name = 'JNE'
