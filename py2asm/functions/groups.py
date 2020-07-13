from py2asm.types import Register
from py2asm.functions.base import InstructionGroup
from py2asm.instructions import Mov
from py2asm.instructions.interrupts import Int


class BiosProcedureCall(InstructionGroup):
    def __init__(self, tele_type):
        self.tele_type = tele_type
        super().__init__()

    def get_instructions(self):
        return (
            Mov(Register.AH, self.tele_type),
            Int(0x21)
        )
