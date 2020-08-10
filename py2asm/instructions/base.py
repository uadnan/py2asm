from py2asm.utils import format_argument


class Instruction:
    name = None
    template = '{name:<8} {operands}'

    n_args = None

    def __init__(self, *args):
        if self.n_args is not None and len(args) != self.n_args:
            raise TypeError('{} expected {} arguments got: {}'.format(
                self.__class__.__name__, self.n_args, len(args)
            ))

        self.args = args

    def render(self):
        if self.n_args == 2 and self.args[0] == self.args[1]:
            return ''

        return self.template.format(
            name=self.name,
            operands=self.render_operands()
        )

    def render_operands(self):
        return ', '.join(format_argument(arg) for arg in self.args)


class Nop(Instruction):
    name = 'NOP'
    n_args = 0
