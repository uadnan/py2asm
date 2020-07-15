import py2asm as asm


if __name__ == "__main__":
    with asm.Program() as p:

        y = asm.Variable('y', asm.VariableType.BYTE)
        x = asm.Variable('x', asm.VariableType.BYTE)

        y <<= (x * 4 - 1) / 8

        print(p.render())
