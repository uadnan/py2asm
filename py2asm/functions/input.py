from py2asm.functions.base import Function
from py2asm.functions.groups import BiosProcedureCall


class InputChar(Function):
    def __init__(self, echo=True):
        self.echo = echo

        super().__init__()

    def get_instructions(self):
        return (
            BiosProcedureCall(0x01 if self.echo else 0x07),
        )


class Input(Function):
    def __init__(self, echo=True):
        self.echo = echo

        super().__init__()

    def get_instructions(self):
        return (
            BiosProcedureCall(0x01 if self.echo else 0x07),
        )
