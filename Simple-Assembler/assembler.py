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
    
    #load stores all the values if the mem_addr in the reg1
def load(reg1 , variable): #change load store and all the immediate value checkers also check the variable counter
    return("00100" + reg[reg1]+variable_dict[variable])
    

def store(reg1 , variable):
    return("00101" + reg[reg1] + variable_dict[variable])


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

f = open('Readme.txt', mode='r+')
input_l = f.readlines()    #l=[intructions as strings]
variable_dict = {}
var_count=0

for x in input_l:       # count number of variables
    x=x.split()
    
    if(x[0] != "var"):
        break
    else:
        var_count+=1
        
temp=var_count

for x in input_l:     #assign memory location to variables
   
    
    if(x[0] != "var"):
        break
    else:
        idx=len(input_l)-temp
        variable_dict.add(x[1],format(idx, '08b'))
        temp-=1

x=input().split()
y=1
label_counter = 0
variable_counter = 0
label_dict = {} #this label is for storing the address of the labels

instructions=["add","sub","mov","ld","st","mul","div","rs","ls","xor","or","and","not","cmp","jmp","jlt","jgt","je","hlt"]
register=["R0","R1","R2","R3","R4","R5","R6"]
 
while(y<=256):
    
    if(x[0][-1:]==":"):
        label_dict[x[0][:-1]] = format(label_counter, '08b')
        label_counter+=1
        y=y-1
    
    elif(x[0] not in instructions):
        print("instruction not found")
        break

    elif(x[0]=="add"):
        if(len(x)!=4):
            print("Wrong type")
            break

        elif(x[1] not in register or x[2] not in register  or x[3] not in register):
            print ("Register not found")
            break
        else:
            final=Addition(x[1],x[2],x[3])
        
    elif(x[0]=="sub"):
        if(len(x)!=4):
            print("Wrong type")
            break
        elif(x[1] not in register or x[2] not in register  or x[3] not in register):
            print ("Register not found")
            break
        else:
            final=Subtraction(x[1],x[2],x[3])
    
    elif(x[0]=="mov"):
        if(len(x)!=3):
             print("Wrong type")
             break

        elif(x[2][0:1]=="$"):
            if(int(x[2][1:])>255 or int(x[2][1:])<0):
                print("Illegal Immediate value")
            elif(x[1] not in register):
                print ("Register not found")
            else:
                final=mov_imm(x[1],int(x[2][1:]))
        else:
            if (x[1] not in register or x[2] not in register):
                print ("Register not found")
            else:
                final=moveRegister(x[1],x[2])
            
    elif(x[0]=="ld"):
        if(len(x)!=3):
             print("Wrong type")
             break

        elif(x[1] not in register or x[2] not in variable_dict.keys()):
            print("Use of undefined variables")  
            break
        elif(x[2] in label_dict):
            print("Misuse of variables as labels") 
            break
        else:
            if(type(x[2]) == str):
                final=load(x[1],variable_dict[x[2]])

            else:
                final=load(x[1],x[2])

    elif(x[0]=="st"):
        if(len(x)!=3):
             print("Wrong type")
             break
        elif(x[1] not in register or x[2] not in variable_dict.keys()):
            print("Use of undefined variables")  
            break
        elif(x[2] in label_dict):
            print("Misuse of variables as labels") 
            break
        else:
            if(type(x[2]) == str):
                final=store(x[1],variable_dict[x[2]])

            else:
                final=store(x[1],x[2])
        
    elif(x[0]=="mul"):
        if(len(x)!=4):
             print("Wrong type")
             break
        elif(x[1] not in register or x[2] not in register  or x[3] not in register):
            print ("Register not found")
            break
        else:
            final=Multiplication(x[1],x[2],x[3])
        
    elif(x[0]=="div"):
        if(len(x)!=3):
             print("Wrong type")
             break
        elif(x[1] not in register or x[2] not in register):
            print ("Register not found")
            break
        else:
            final=divide(x[1],x[2])
        
    elif(x[0]=="rs"):
        if(len(x)!=3):
             print("Wrong type")
             break

        
        elif(int(x[2][1:])>255 or int(x[2][1:])<0):
            print("Illegal Immediate value")
        elif(x[1] not in register):
            print ("Register not found")
     
        else:
            final=right_shift(x[1],int(x[2][1:]))
        
    elif(x[0]=="ls"):
        if(len(x)!=3):
             print("Wrong type")
             break

        
        elif(int(x[2][1:])>255 or int(x[2][1:])<0):
                print("Illegal Immediate value")
        elif(x[1] not in register):
                print ("Register not found")
     
        else:
            final=left_shift(x[1],int(x[2][1:]))
        
    elif(x[0]=="xor"):
        if(len(x)!=4):
            print("Wrong type")
            break

        elif(x[1] not in register or x[2] not in register  or x[3] not in register):
            print ("Register not found")
            break
        else:
            final=Exclusive_OR(x[1],x[2],x[3])
        
    elif(x[0]=="or"):
        if(len(x)!=4):
            print("Wrong type")
            break

        elif(x[1] not in register or x[2] not in register  or x[3] not in register):
            print ("Register not found")
            break
        else:
            final=OR(x[1],x[2],x[3])
        
    elif(x[0]=="and"):
        if(len(x)!=4):
            print("Wrong type")
            break

        elif(x[1] not in register or x[2] not in register  or x[3] not in register):
            print ("Register not found")
            break
        else:
            final=AND(x[1],x[2],x[3])
        
    elif(x[0]=="not"):
        if(len(x)!=3):
            print("Wrong type")
            break

        elif(x[1] not in register or x[2] not in register):
            print ("Register not found")
            break
        else:
            final=invert(x[1],x[2])
        
    elif(x[0]=="cmp"):
        if(len(x)!=3):
            print("Wrong type")
            break

        elif(x[1] not in register or x[2] not in register):
            print ("Register not found")
            break
        else:
            final=compare(x[1],x[2])
        
    elif(x[0]=="jmp"):
        if(len(x)!=2):
            print("Wrong type")
            break

        elif(x[1] not in label_dict.keys()):
            print("Use of undefined label")  
            break

        elif(x[2] in variable_dict.keys()):
            print("Misuse of labels as variable") 
            break
        else:
            final=UnconditionalJump(x[1])

        
    elif(x[0]=="jlt"):
        if(len(x)!=2):
            print("Wrong type")
            break

        elif(x[1] not in label_dict.keys()):
            print("Use of undefined label")  
            break

        elif(x[2] in variable_dict.keys()):
            print("Misuse of labels as variable") 
            break
        else:
            final=JumpIfLessThan(x[1])
        
    elif(x[0]=="jgt"):
        if(len(x)!=2):
            print("Wrong type")
            break

        elif(x[1] not in label_dict.keys()):
            print("Use of undefined label")  
            break

        elif(x[2] in variable_dict.keys()):
            print("Misuse of labels as variable") 
            break
        else:
            final=JumpIfGreaterThan(x[1])
        
    elif(x[0]=="je"):
        if(len(x)!=2):
            print("Wrong type")
            break

        elif(x[1] not in label_dict.keys()):
            print("Use of undefined label")  
            break

        elif(x[2] in variable_dict.keys()):
            print("Misuse of labels as variable") 
            break
        else:
            final=JumpIfEqualTo(x[1])
        
    elif(x[0]=="hlt"):
        final=Halt()
        print(final)
        break
        
    print(final)
    x=input().split()
    y+=1