import py2asm as asm


with asm.Program():
    asm.Variable('msg', asm.VariableType.BYTE, asm.mark_safe('50 DUP(?)'))

    with asm.DoWhile(asm.Register.AL == 13):
        asm.Raw(
            asm.Mov(asm.Register.AH, 1),
            asm.BiosProcedureCall(0x1),
            'mov [si],al',
            'inc si'
        )
