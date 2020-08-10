# py2asm

There are 3 level structures in py2asm:
## 1. Blocks

It is a high level block which can contain instructions. Each block should be used with python ```with``` statement.

Some block are listed below:

### Program

It is the main block to create assembly code structure.

```python
import py2asm as asm

with asm.Program(model="small", stack=0x100): # model and stack values are optional
    # Rest of the program goes here
    pass
```

### Labeled Block

It adds an label to set of instructions.

```python
import py2asm as asm

with asm.Program():
    with asm.LabeledBlock('LABEL_NAME'):
        # Some Code
        pass
```

### While Block

Creates While loop.

```python
import py2asm as asm

with asm.Program():
    # exp could be any Jump Type (available at asm.JumpTypes)
    # or it could be any conditional expression (<, >, ==, <=, >=)
    # see also: examples/whileloop.py 
    with asm.While(exp):
        # Some Code
        pass
```

### While Block

Similar to While block but places condition to the end of block.

```python
import py2asm as asm

with asm.Program():
    # exp could be any Jump Type (available at asm.JumpTypes)
    # or it could be any conditional expression (<, >, ==, <=, >=)
    # see also: examples/whileloop.py 
    with asm.DoWhile(exp):
        # Some Code
        pass
```

### Procedure

Creates a procedure

```python
import py2asm as asm

with asm.Program():
    # Automatically adds RET at the end
    with asm.Procedure('PROC_NAME'):
        # Some Code
        pass
```

## 2. Functions
Functions are just collection of instructions for most repeated tasks.

### InputChar
Single character input

```python
import py2asm as asm

with asm.Program():
    asm.InputChar(echo=True) # can be false
```

it should outputs following
```asm
MOV      AH, 1
INT      21h
```

### PrintStr
Prints string that ends with '$'

```python
import py2asm as asm

with asm.Program():
    msg = asm.Variable('msg', asm.VariableType.BYTE, "Hello World!$")
    asm.PrintStr(msg)
```

it should outputs following
```asm
LEA      DX, msg
MOV      AH, 09h
INT      21h
```

### PrintChar
Prints single char

```python
import py2asm as asm

with asm.Program():
    asm.PrintChar('C')
```

it should outputs following
```asm
MOV      DL, 'C'
MOV      AH, 02h
INT      21h
```

### PrintNumChar
Prints single char

```python
import py2asm as asm

with asm.Program():
    asm.PrintNumChar(7)
```

it should outputs following
```asm
MOV      DL, 07h
ADD      DL, '0'
MOV      AH, 02h
INT      21h
```

### PrintNum
Print any unsigned number by including emu8086.inc

```python
import py2asm as asm

with asm.Program():
    asm.PrintNum(1234)
```

it should outputs following
```asm
include emu8086.inc

org 100h

.model small
.stack 0100h

.data


DEFINE_PRINT_NUM_UNS
DEFINE_PRINT_NUM

.code
MOV      AX, 04D2h
CALL     PRINT_NUM
```

### PrintStrBuiltin
Prints string by including emu8086.inc

```python
import py2asm as asm

with asm.Program():
    asm.PrintStrBuiltin("Hello World!$")
```

it should outputs following
```asm
include emu8086.inc

PRINT    "Hello World!$"
```

## 3. Raw Instructions: 
