import py2asm as asm


with asm.Program():
    x = asm.Variable('x', asm.VariableType.BYTE, 0)

    with asm.While(x < 10):
        asm.PrintNumChar(x)
        x += 1

    with asm.While(asm.JumpTypes.JumpAbove):
        x += 1
