import unittest

import py2asm as asm


class FunctionTests(unittest.TestCase):
    def test_print(self):
        with asm.Program() as program:
            with asm.Procedure('main'):
                message = asm.DefineByte('message', 'Hello World', 0x0d, 0xa, '$')

                asm.PrintStr(message)

            self.assertEqual(program.render(), """org 100h

.model small
.stack 0100h

.data
message          DB   "Hello World", 0Dh, 0Ah, '$'

.code
main proc
    LEA      DX, message
    MOV      AH, 09h
    INT      21h
    
main endp
end main""")

    def test_echo(self):
        with asm.Program() as program:
            with asm.Procedure('main'):
                asm.PrintChar('?')
                asm.InputChar()

                asm.Raw(
                    asm.Mov(asm.Register.BL, asm.Register.AL)
                )

                asm.PrintChar(0x0D)  # \r
                asm.PrintChar(0x0A)  # \n
                asm.PrintChar(asm.Register.BL)

            self.assertEqual(program.render(), """org 100h

.model small
.stack 0100h

.data


.code
main proc
    MOV      DL, '?'
    MOV      AH, 02h
    INT      21h
    
    MOV      AH, 01h
    INT      21h
    
    MOV      BL, AL
    
    MOV      DL, 0Dh
    MOV      AH, 02h
    INT      21h
    
    MOV      DL, 0Ah
    MOV      AH, 02h
    INT      21h
    
    MOV      DL, BL
    MOV      AH, 02h
    INT      21h
    
main endp
end main""")

    def test_labeled_block(self):
        with asm.Program() as program:
            with asm.LabeledBlock('test') as test:
                asm.PrintChar('?')

            print(program.render())
