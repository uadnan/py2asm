import py2asm as asm


if __name__ == "__main__":
    with asm.Program() as p:
        n1 = asm.Variable('n1', asm.VariableType.WORD, 1)
        n2 = asm.Variable('n2', asm.VariableType.WORD, 1)
        count = asm.Variable('count', asm.VariableType.BYTE, 0)

        with asm.While(count < 10):
            asm.Print(n1, asm.PrintType.PRINT_NUM_BUILTIN)
            asm.Print(", ")
            n1 + n2
            n1 <<= n2
            n2 <<= asm.Register.AX
            count += 1

        print(p.render())
