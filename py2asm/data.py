from py2asm import Program
from py2asm.formatting import mark_safe, format_argument


class DefineFunction:
    EMPTY = mark_safe('?')

    directive = None
    template = '{name:<16} {directive:<4} {initializers}'

    def __init__(self, name, *initializers):
        if len(initializers) == 0:
            initializers = (self.EMPTY,)

        self.name = name
        self.initializers = initializers

        Program.get_current().define_data(self)

    def render(self):
        return self.template.format(
            name=self.name,
            directive=self.directive,
            initializers=', '.join(
                format_argument(init)
                for init in self.initializers
            )
        )


class DefineWord(DefineFunction):
    directive = 'DW'


class DefineByte(DefineFunction):
    directive = 'DB'


class DefineDoubleWord(DefineFunction):
    directive = 'DD'


class DefineQuardWord(DefineFunction):
    directive = 'DQ'


class DefineTenByte(DefineFunction):
    directive = 'DT'
