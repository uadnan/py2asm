from py2asm.blocks.block import Block


class LabeledBlock(Block):
    template = """{name}:
{children}
"""

    def __init__(self, name):
        self.name = name

        super().__init__()

    def render(self):
        return self.template.format(
            name=self.name,
            children=self.render_children()
        )