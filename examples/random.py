import py2asm as asm


if __name__ == "__main__":
    with asm.Program() as p:
        m = asm.Define('m', 100)
        a = asm.Define('a', 0x1fb9)
        c = asm.Define('c', 0x6efb)

        count = asm.Variable('count', asm.VariableType.BYTE, 0)
        n = asm.Variable('n', asm.VariableType.BYTE, 10)
        x = asm.Variable('x', asm.VariableType.WORD)

        asm.Raw("PRINT    \"How many random numbers you want: \"")
        asm.InputChar()
        asm.Raw("PRINT    \", \"")

        asm.Raw(
            asm.Mov(n, asm.Register.AL),
            asm.Sub(n, 48),
        )

        with asm.While(count < n):
            x <<= (a * x + c) % m
            asm.PrintNum(x)
            asm.Raw("PRINT    \", \"")
            count += 1

        print(p.render())
