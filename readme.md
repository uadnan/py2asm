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

### 2. Functions
### 3. Raw Instructions: 
