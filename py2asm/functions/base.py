from py2asm.blocks.block import LeafBlock


class InstructionGroupMixin:
    def render(self):
        return '\n'.join(c.render() for c in self.get_instructions())

    def get_instructions(self):
        raise NotImplementedError()


class InstructionGroup(InstructionGroupMixin):
    pass


class Function(InstructionGroupMixin, LeafBlock):
    def render(self):
        return super().render() + '\n'


class Raw(Function):
    def __init__(self, *instructions):
        self.instructions = instructions

        super().__init__()

    def get_instructions(self):
        return self.instructions
