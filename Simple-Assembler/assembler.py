
reg={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110'}

def Addition(rega,regb,regc):
    s="0000000"
    s=s+reg[rega]+reg[regb]+reg[regc]
    return(s)

def Subtraction(rega,regb,regc):
    s="0000100"
    s=s+reg[rega]+reg[regb]+reg[regc]
    return(s)

def mov_imm(registor,val):
    s=""
    s+="00010"
    s+=reg[registor]
    bin_ans=format(val, '08b')
    s+=bin_ans
    return(s)

def moveRegister(reg1 , reg2):
    return("00011" + "00000" + reg[reg1] + reg[reg2])
    
def load(reg1 , mem_addr):
    return("00100" + reg[reg1]+ mem_addr)
    

def store(reg1 , mem_addr):
    return("00101" + reg[reg1] + mem_addr)


def Multiplication(rega,regb,regc):
    reg={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110'}
    s="0011000"
    s=s+reg[rega]+reg[regb]+reg[regc]
    return(s)

#for dividing the register values--
def divide(reg3,reg4):
    return("00111" + "00000" + reg[reg3] + reg[reg4])
    
def right_shift(registor,val):
    s=""
    s+="01000"
    s+=reg[registor]
    bin_ans=format(val, '08b')
    s+=bin_ans
    return(s)

def left_shift(registor,val):
    s=""
    s+="01000"
    s+=reg[registor]
    bin_ans=format(val, '08b')
    s+=bin_ans
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

#for bitwise NOT operation--
def invert(reg1 , reg2):
    return("01101" + "00000" + reg[reg1] + reg[reg2])

#for comparing the register values--
def compare(reg1 , reg2):
    return("01110" + "00000" + reg[reg1] + reg[reg2])

#for jumping to a memory address
def UnconditionalJump(mem_addr):
    return("01111" + "000" + mem_addr)

#for jumping if greater than flag = 1
def JumpIfGreaterThan(mem_addr):
    return("10001" + "000" + mem_addr)

#for jumping if less than flag = 1
def JumpIfLessThan(mem_addr):
    return("10000" + "000" + mem_addr)
    
#for jumping if equal to  flag = 1
def JumpIfEqualTo(mem_addr):
    return("10010" + "000" + mem_addr)

def Halt():
    s="1001100000000000"
    return(s)


x=input().split()
y=1
label_counter = 0
variable_counter = 0
label_dict = {} #this label is for storing the address of the labels
variable_dict = {} #this label is for storing the address of the variables
#instruction 
#register 
while(y<=256):

    while(x[0] == "var"):
        variable_dict[x[1]] = format(variable_counter, '08b')
        variable_counter+=1
    
    if(x[0][-1:]==":"):
        label_dict[x[0][:-1]] = format(label_counter, '08b')
        label_counter+=1
    
    else if(x[0] not in instructions):
        print("instruction not found")

    else if(x[0]=="add"):
        final=Addition(x[1],x[2],x[3])
        
    else if(x[0]=="sub"):
        final=Subtraction(x[1],x[2],x[3])
    
    else if(x[0]=="mov"):
        if(x[2][0:1]=="$"):
            final=mov_imm(x[1],int(x[2][1:]))
        else:
            final=moveRegister(x[1],x[2])
            
    else if(x[0]=="load"):
        final=load(x[1],x[2])
        
    else if(x[0]=="st"):
        final=store(x[1],x[2])
        
    else if(x[0]=="mul"):
        final=Multiplication(x[1],x[2],x[3])
        
    if(x[0]=="div"):
        final=divide(x[1],x[2])
        
    if(x[0]=="rs"):
        final=right_shift(x[1],int(x[2][1:]))
        
    if(x[0]=="ls"):
        final=left_shift(x[1],int(x[2][1:]))
        
    if(x[0]=="xor"):
        final=Exclusive_OR(x[1],x[2],x[3])
        
    if(x[0]=="or"):
        final=OR(x[1],x[2],x[3])
        
    if(x[0]=="and"):
        final=AND(x[1],x[2],x[3])
        
    if(x[0]=="not"):
        final=invert(x[1],x[2])
        
    if(x[0]=="cmp"):
        final=compare(x[1],x[2])
        
    if(x[0]=="jmp"):
        if(type(x[1]) == int):    
            final=UnconditionalJump(x[1])
        else if(type(x[1]) == str):
            parameter = label_dict[x[1]]
            final = UnconditionalJump(parameter)
        
    if(x[0]=="jlt"):
        if(type(x[1]) == int):    
            final = JumpIfLessThan(x[1])
        else if(type(x[1]) == str):
            parameter = label_dict[x[1]]
            final = JumpIfLessThan(parameter)
        
    if(x[0]=="jgt"):
        if(type(x[1]) == int):    
            final = JumpIfGreaterThan(x[1])
        else if(type(x[1]) == str):
            parameter = label_dict[x[1]]
            final = JumpIfGreaterThan(parameter)

        
    if(x[0]=="je"):
        if(type(x[1]) == int):    
            final = JumpIfEqualTo(x[1])
        else if(type(x[1]) == str):
            parameter = label_dict[x[1]]
            final = JumpIfEqualTo(parameter)

        
    if(x[0]=="hlt"):
        final=Halt()
        print(final)
        break
        
    print(final)
    x=input().split()
    y+=1

            