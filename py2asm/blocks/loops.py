from py2asm.constants import JumpTypes
from py2asm.blocks.block import Block


class While(Block):
    template = """{condition}    
    {jmp_type:<8} {name}

{name}:
{children}
    
{condition}
    {jmp_type:<8} {name}
"""

    def __init__(self, exp):
        if type(exp) == JumpTypes:
            self.jump_type = exp
            self.condition_instructions = []
        elif type(exp) == tuple and len(exp) == 2 and type(exp[1]) == JumpTypes:
            self.condition_instructions, self.jump_type = exp
        else:
            raise ValueError('Expected expression got {}'.format(type(exp)))

        super().__init__()

    def get_condition(self):
        lines = '\n'.join(c.render() for c in self.condition_instructions).split('\n')
        return '\n'.join(
            ('    ' * self.indent) + line
            for line in lines
        )

    def render(self):
        i = self.root.loop_counter
        self.root.loop_counter += 1

        return self.template.format(
            name=f"loop{i if i != 0 else ''}",
            jmp_type=self.jump_type.value,
            condition=self.get_condition(),
            children=self.render_children()
        )
