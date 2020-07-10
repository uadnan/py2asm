from enum import Enum


class Register(Enum):
    AX = 'AX'
    AL = 'AL'
    AH = 'AH'

    BX = 'BX'
    BL = 'BL'
    BH = 'BH'

    CX = 'CX'
    CL = 'CL'
    CH = 'CH'

    DX = 'DX'
    DL = 'DL'
    DH = 'DH'

    CS = 'CS'
    DS = 'DS'
    ES = 'ES'
    SS = 'SS'

    IP = 'IP'
    SI = 'SI'
    DI = 'DI'
    SP = 'SP'
    BP = 'BP'
