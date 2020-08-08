import py2asm as asm


if __name__ == "__main__":
    with asm.Program() as p:
        x = asm.Variable('x', asm.VariableType.WORD, 10)
        y = asm.Variable('y', asm.VariableType.WORD, 20)

        _1 = (y / 2 - 4) * y
        _1 = _1.mov(asm.Register.CX)
        _2 = x * 5
        x <<= _2 + _1

        asm.PrintNum(x)

        print(p.render())
