
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


# FOR ALL THE TYPE C INTRUCTIONS

#for moving values of reg2 to reg1--
def moveRegister(reg1 , reg2):
    print("00011" + "00000" + registers.reg1 + registers.reg2)

#for dividing the register values--
def divide(reg3,reg4):
    print("00111" + "00000" + registers.reg3 + registers.reg4)

#for bitwise NOT operation--
def invert(reg1 , reg2):
    print("01101" + "00000" + registers.reg1 + registers.reg2)

#for comparing the register values--
def compare(reg1 , reg2):
    print("01110" + "00000" + registers.reg1 + registers.reg2)

#FOR ALL THE TYPE D INTRUCTIONS

#for loading data from memory address to register value--
def load(reg1 , mem_addr):
    print("00100" + registers.reg1 + mem_addr)

#for storing data from reg1 to mem_addr--
def store(reg1 , mem_addr):
    print("00101" + registers.reg1 + mem_addr)

#FOR ALL THE TYPE E INTRUCTIONS

#for jumping to a memory address
def UnconditionalJump(mem_addr):
    print("01111" + "000" + mem_addr)

#for jumping if greater than flag = 1
def JumpIfGreaterThan(mem_addr):
    print("10001" + "000" + mem_addr)

#for jumping if less than flag = 1
def JumpIfLessThan(mem_addr):
    print("10000" + "000" + mem_addr)

#for jumping if equal to  flag = 1
def JumpIfEqualTo(mem_addr):
    print("10010" + "000" + mem_addr)

def mov_imm(registor,val):
    s=""
    s+="00010"
    s+=Dict[registor]
   # if val>255 error
        
    bin_ans=format(val, '08b')
    s+=bin_ans
    print(s)
    
mov_imm(registor,val)

def right_shift(registor,val):
    s=""
    s+="01000"
    s+=Dict[registor]
    bin_ans=format(val, '08b')
    s+=bin_ans
    print(s)

def left_shift(registor,val):
    s=""
    s+="01000"
    s+=Dict[registor]
    bin_ans=format(val, '08b')
    s+=bin_ans
    print(s)    

