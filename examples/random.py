import py2asm as asm


if __name__ == "__main__":
    with asm.Program() as p:
        m = asm.Define('m', 100)
        a = asm.Define('a', 0x1fb9)
        c = asm.Define('c', 0x6efb)

        x = asm.Variable('x', asm.VariableType.WORD)

        asm.Raw(
            asm.Mov(asm.Register.AH, 0),
            asm.Int(0x1A),
            asm.Mov(x, asm.Register.CX)
        )

        with asm.LabeledBlock('loop'):
            x <<= (a * x + c) % m
            asm.PrintNum(x)
            asm.Print(", ")
