
def Addition(rega,regb,regc):
    reg={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110'}
    s="0000000"
    s=s+reg[rega]+reg[regb]+reg[regc]
    return(s)

def Subtraction(rega,regb,regc):
    reg={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110'}
    s="0000100"
    s=s+reg[rega]+reg[regb]+reg[regc]
    return(s)

def Multiplication(rega,regb,regc):
    reg={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110'}
    s="0011000"
    s=s+reg[rega]+reg[regb]+reg[regc]
    return(s)

def Exclusive_OR(rega,regb,regc):
    reg={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110'}
    s="0101000"
    s=s+reg[rega]+reg[regb]+reg[regc]
    return(s)

def OR(rega,regb,regc):
    reg={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110'}
    s="0101100"
    s=s+reg[rega]+reg[regb]+reg[regc]
    return(s)

def AND(rega,regb,regc):
    reg={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110'}
    s="0110000"
    s=s+reg[rega]+reg[regb]+reg[regc]
    return(s)


def Halt():
    s="1001100000000000"
    return(s)



