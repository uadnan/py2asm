import threading

from py2asm.blocks.block import Block
from py2asm.formatting import format_number

_state = threading.local()


class Program(Block):
    template = """org 100h

.model {model}
.stack {stack}

.data
{data}

.code
{children}"""

    def __init__(self, model='small', stack=0x100):
        self.model = model
        self.stack = stack

        self.data = []
        super().__init__()

    def render(self):
        return self.template.format(
            model=self.model,
            stack=format_number(self.stack),
            data='\n'.join(d.render() for d in self.data),
            children=self.render_children()
        )

    def __enter__(self):
        _state.current_program = self
        return super().__enter__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        _state.current_program = None
        super().__exit__(exc_type, exc_val, exc_tb)

    @staticmethod
    def get_current():
        return getattr(_state, 'current_program', None)

    def define_data(self, data):
        self.data.append(data)
