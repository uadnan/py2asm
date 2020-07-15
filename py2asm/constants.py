from enum import Enum


class JumpTypes(Enum):
    # Signed Jumps
    JumpLess = "JL"
    JumpLessEqual = "JLE"
    JumpGreater = "JG"
    JumpGreaterEqual = "JGE"

    # Unsigned Jumps
    JumpAbove = "JA"
    JumpAboveEqual = "JAE"
    JumpBelow = "JB"
    JumpBelowEqual = "JBE"

    # Zero Flag Jumps
    JumpEqual = "JE"
    JumpNotEqual = "JNE"

    # Carry Flag Jumps
    JumpCarry = "JC"
    JumpNotCarry = "JNC"

    # Overflow Flag Jumps
    JumpOverflow = "JO"
    JumpNotOverflow = "JNO"

    # Sign Flag Jumps
    JumpNegativeSign = "JS"
    JumpNoNegativeSign = "JNS"

    # Parity Flag Jumps
    JumpParityEven = "JP"
    JumpParityOdd = "JNP"


class Interrupts(Enum):
    pass
