import sys
reg={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110','FLAGS':'111'}

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
    
    #load stores all the values if the mem_addr in the reg1
def load(reg1 , variable): #change load store and all the immediate value checkers also check the variable counter
    return("00100" + reg[reg1]+variable_dict[variable])
    

def store(reg1 , variable):
    return("00101" + reg[reg1] + variable_dict[variable])


def Multiplication(rega,regb,regc):
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
    s="0101000"
    s=s+reg[rega]+reg[regb]+reg[regc]
    return(s)

def OR(rega,regb,regc):
    s="0101100"
    s=s+reg[rega]+reg[regb]+reg[regc]
    return(s)

def AND(rega,regb,regc):
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
def UnconditionalJump(label): ##
    return("01111" + "000" + label_dict[label])

#for jumping if greater than flag = 1
def JumpIfGreaterThan(label): ##
    return("10001" + "000" + label_dict[label])

#for jumping if less than flag = 1
def JumpIfLessThan(label): ##
    return("10000" + "000" + label_dict[label])
    
#for jumping if equal to  flag = 1
def JumpIfEqualTo(label): ##
    return("10010" + "000" + label_dict[label])

def Halt():
    s="1001100000000000"
    return(s)


#input_list = list(map(str, sys.stdin.readlines())) #l=[intructions as strings]
path='c:\Users\Veneet Gandhi\Desktop\kwalitywalls\Simple-Assembler\assembler.py'
code=[i.strip().split() for i in open(path).readlines()]
input_list=code
variable_dict = {}
var_count=0
output_list=[]

for i in range(len(input_list)):
    x=input_list[i]
    x=x.split()
    input_list[i]=x

for x in input_list:       # count number of variables
    if(x[0] != "var"):
        break
    else:
        var_count+=1

temp=var_count

for x in input_list:     #assign memory location to variables
    if(x[0] != "var"):
        break
    else:
        idx=len(input_list)-temp
        variable_dict[x[1]] = format(idx, '08b')
        temp-=1

for i in range(var_count ,len(input_list)):
    if(x[0] == "var"):
        output_list.append("variables not in beginning")

if ["hlt"] not in input_list:
    output_list.append("halt instruction missing")

elif(input_list[-1]!="hlt"):
    output_list.append("instructions after halt")

label_counter = 0
label_dict = {} #this label is for storing the address of the labels

instructions=["add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt"]
register=["R0","R1","R2","R3","R4","R5","R6","FLAGS"]
for i in range(var_count ,len(input_list)):
    if(input_list[i][0][-1:]==":"): 
        label_dict[input_list[i][0][:-1]] = format(label_counter, '08b')
        label_counter+=1
        input_list[i] = input_list[i][1:]
 
for i in range(var_count,len(input_list)):
    x=input_list[i]
    
    if x[0] not in instructions:
        output_list.append("instruction not found")
        break

    elif(x[0]=="add"):
        if(len(x)!=4):
            output_list.append("Wrong type")
            break

        elif(x[1] not in register or x[2] not in register  or x[3] not in register):
            output_list.append("Register not found")
            break
        else:
            output_list.append(Addition(x[1],x[2],x[3]))
        
    elif(x[0]=="sub"):
        if(len(x)!=4):
            output_list.append("Wrong type")
            break
        elif(x[1] not in register or x[2] not in register  or x[3] not in register):
            output_list.append("Register not found")
            break
        else:
            output_list.append(Subtraction(x[1],x[2],x[3]))
    
    elif(x[0]=="mov"):
        if(len(x)!=3):
            output_list.append("Wrong type")
            break

        elif(x[2][0:1]=="$"):
            if(int(x[2][1:])>255 or int(x[2][1:])<0):
                output_list.append("Illegal Immediate value")
            elif(x[1] not in register):
                output_list.append("Register not found")
            else:
                output_list.append(mov_imm(x[1],int(x[2][1:])))
        else:
            if (x[1] not in register or x[2] not in register):
                output_list.append("Register not found")
            else:
                output_list.append(moveRegister(x[1],x[2]))
            
    elif(x[0]=="ld"):
        if(len(x)!=3):
            output_list.append("Wrong type")
            break

        elif(x[1] not in register or x[2] not in variable_dict.keys()):
            output_list.append("Use of undefined variables")  
            break
        elif(x[2] in label_dict):
            output_list.append("Misuse of variables as labels") 
            break
        else:
            if(type(x[2]) == str):
                output_list.append(load(x[1],x[2]))

            else:
                output_list.append(load(x[1],x[2]))

    elif(x[0]=="st"):
        if(len(x)!=3):
            output_list.append("Wrong type")
            break
        elif(x[1] not in register or x[2] not in variable_dict.keys()):
            output_list.append("Use of undefined variables")  
            break
        elif(x[2] in label_dict):
            output_list.append("Misuse of variables as labels") 
            break
        else:
            if(type(x[2]) == str):
                output_list.append(store(x[1],x[2]))

            else:
                output_list.append(store(x[1],x[2]))
        
    elif(x[0]=="mul"):
        if(len(x)!=4):
            output_list.append("Wrong type")
            break
        elif(x[1] not in register or x[2] not in register  or x[3] not in register):
            output_list.append ("Register not found")
            break
        else:
            output_list.append(Multiplication(x[1],x[2],x[3]))
        
    elif(x[0]=="div"):
        if(len(x)!=3):
            output_list.append("Wrong type")
            break
        elif(x[1] not in register or x[2] not in register):
            output_list.append("Register not found")
            break
        else:
            output_list.append(divide(x[1],x[2]))
        
    elif(x[0]=="rs"):
        if(len(x)!=3):
            output_list.append("Wrong type")
            break

        
        elif(int(x[2][1:])>255 or int(x[2][1:])<0):
            output_list.append("Illegal Immediate value")
        elif(x[1] not in register):
            output_list.append ("Register not found")
     
        else:
            output_list.append(right_shift(x[1],int(x[2][1:])))
        
    elif(x[0]=="ls"):
        if(len(x)!=3):
            output_list.append("Wrong type")
            break

        
        elif(int(x[2][1:])>255 or int(x[2][1:])<0):
                output_list.append("Illegal Immediate value")
        elif(x[1] not in register):
                output_list.append ("Register not found")
     
        else:
            output_list.append(left_shift(x[1],int(x[2][1:])))
        
    elif(x[0]=="xor"):
        if(len(x)!=4):
            output_list.append("Wrong type")
            break

        elif(x[1] not in register or x[2] not in register  or x[3] not in register):
            output_list.append ("Register not found")
            break
        else:
            output_list.append(Exclusive_OR(x[1],x[2],x[3]))
        
    elif(x[0]=="or"):
        if(len(x)!=4):
            output_list.append("Wrong type")
            break

        elif(x[1] not in register or x[2] not in register  or x[3] not in register):
            output_list.append("Register not found")
            break
        else:
            output_list.append(OR(x[1],x[2],x[3]))
        
    elif(x[0]=="and"):
        if(len(x)!=4):
            output_list.append("Wrong type")
            break

        elif(x[1] not in register or x[2] not in register  or x[3] not in register):
            output_list.append("Register not found")
            break
        else:
            output_list.append(AND(x[1],x[2],x[3]))
        
    elif(x[0]=="not"):
        if(len(x)!=3):
            print("Wrong type")
            break

        elif(x[1] not in register or x[2] not in register):
            output_list.append("Register not found")
            break
        else:
            output_list.append(invert(x[1],x[2]))
        
    elif(x[0]=="cmp"):
        if(len(x)!=3):
            output_list.append("Wrong type")
            break

        elif(x[1] not in register or x[2] not in register):
            output_list.append("Register not found")
            break
        else:
            output_list.append(compare(x[1],x[2]))
        
    elif(x[0]=="jmp"):
        if(len(x)!=2):
            output_list.append("Wrong type")
            break

        elif(x[1] not in label_dict.keys()):
            output_list.append("Use of undefined label")  
            break

        elif(x[2] in variable_dict.keys()):
            output_list.append("Misuse of labels as variable") 
            break
        else:
            output_list.append(UnconditionalJump(x[1]))

        
    elif(x[0]=="jlt"):
        if(len(x)!=2):
            output_list.append("Wrong type")
            break

        elif(x[1] not in label_dict.keys()):
            output_list.append("Use of undefined label")  
            break

        elif(x[2] in variable_dict.keys()):
            output_list.append("Misuse of labels as variable") 
            break
        else:
            output_list.append(JumpIfLessThan(x[1]))
        
    elif(x[0]=="jgt"):
        if(len(x)!=2):
            output_list.append("Wrong type")
            break

        elif(x[1] not in label_dict.keys()):
            output_list.append("Use of undefined label")  
            break

        elif(x[2] in variable_dict.keys()):
            output_list.append("Misuse of labels as variable") 
            break
        else:
            output_list.append(JumpIfGreaterThan(x[1]))
        
    elif(x[0]=="je"):
        if(len(x)!=2):
            output_list.append("Wrong type")
            break

        elif(x[1] not in label_dict.keys()):
            output_list.append("Use of undefined label")  
            break

        elif(x[2] in variable_dict.keys()):
            output_list.append("Misuse of labels as variable") 
            break
        else:
            output_list.append(JumpIfEqualTo(x[1]))
        
    elif(x[0]=="hlt"):
        output_list.append(Halt())
        break

for x in output_list:
    print(x)
        