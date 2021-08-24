import sys
import matplotlib.pyplot as plt
input_list = list(map(str, sys.stdin.readlines()))
# f = open('sys.txt', mode='r+')
# input_list = f.readlines()
counter=len(input_list)
list_memory=input_list
reg={'000':'R0','001':'R1','010':'R2','011':'R3','100':'R4','101':'R5','110':'R6','111':'FLAGS'}
reg_value={'R0':0,'R1':0,'R2':0,'R3':0,'R4':0,'R5':0,'R6':0,'FLAGS':0}
output_list=[]
var_dict = {}
var_count = 0
cycle_x = []
cycle_y = []
cycle_ldst = []
cycle_counter = 0


PC=0
while(PC<len(input_list)):
    jump_flag=False
    cycle_x.append(cycle_counter)
    cycle_counter += 1
    cycle_ldst.append(-1)
    x=input_list[PC]
    PC_and_regvals=[]
    flag_val=reg_value["FLAGS"]
    reg_value["FLAGS"]=0
    if(x[0:5]=="00000"):
        #add
        reg1=reg[x[7:10]]
        reg2=reg[x[10:13]]
        reg3=reg[x[13:16]]
        reg_value[reg1]=reg_value[reg2]+reg_value[reg3]
    
    
        if(reg_value[reg1]>=65536):
            reg_value["FLAGS"]+=8
            reg_value[reg1]= reg_value[reg1]%65536
   
    if(x[0:5]=="00001"):
        #subtract
        reg1=reg[x[7:10]]
        reg2=reg[x[10:13]]
        reg3=reg[x[13:16]]
        reg_value[reg1]=reg_value[reg2]-reg_value[reg3]
        
        
        if(reg_value[reg1]<0):
            reg_value["FLAGS"]+=8
            reg_value[reg1]=0
            
    if(x[0:5]=="00110"):
        #multiply
        reg1=reg[x[7:10]]
        reg2=reg[x[10:13]]
        reg3=reg[x[13:16]]
        reg_value[reg1]=reg_value[reg2]*reg_value[reg3]
        
        
        if(reg_value[reg1]>=65536 ):
            reg_value["FLAGS"]+=8
            reg_value[reg1]= reg_value[reg1]%65536

    if(x[0:5]=="01010"):
        #xor
        reg1=reg[x[7:10]]
        reg2=reg[x[10:13]]
        reg3=reg[x[13:16]]
        reg_value[reg1]=reg_value[reg2]^reg_value[reg3]
    
    if(x[0:5]=="01011"):
        #or
        reg1=reg[x[7:10]]
        reg2=reg[x[10:13]]
        reg3=reg[x[13:16]]
        reg_value[reg1]=reg_value[reg2]|reg_value[reg3]
    
    if(x[0:5]=="01100"):
        #and
        reg1=reg[x[7:10]]
        reg2=reg[x[10:13]]
        reg3=reg[x[13:16]]
        reg_value[reg1]=reg_value[reg2] & reg_value[reg3]

    if(x[0:5]=="00010"):
        #mov_imm
        reg1=reg[x[5:8]]
        imm=int(x[8:16],2)
        reg_value[reg1]=imm

    if(x[0:5]=="00011"):
        #mov_reg
        reg1=reg[x[10:13]]
        reg2=reg[x[13:16]]
        if(reg2=="FLAGS"):
            reg_value[reg1]=flag_val
        else:
            reg_value[reg1]=reg_value[reg2]
        
    if(x[0:5]=="01001"):
        #left_shift
        reg1=reg[x[5:8]]
        imm=int(x[8:16],2)
        reg_value[reg1]= int(reg_value[reg1])<<imm
        if(reg_value[reg1]>=65536):
            reg_value["FLAGS"]+=8
            reg_value[reg1]= reg_value[reg1]%65536
            
    if(x[0:5]=="01000"):
        #right_shift
        reg1=reg[x[5:8]]
        imm=int(x[8:16],2)
        reg_value[reg1]= int(reg_value[reg1])>>imm
        
    if(x[0:5]=="00111"):           #divide
        reg1=reg[x[10:13]]
        reg2=reg[x[13:16]]
        reg_value["R0"]=int(reg_value[reg1]/reg_value[reg2])
        reg_value["R1"]=reg_value[reg1]%reg_value[reg2]

    if(x[0:5]=="01110"):        #compare
        
        reg1=reg[x[10:13]]
        reg2=reg[x[13:16]]
        if reg_value[reg1]>reg_value[reg2]:
            reg_value["FLAGS"]+=2
        elif reg_value[reg1]<reg_value[reg2]:
            reg_value["FLAGS"]+=4
        else:
            reg_value["FLAGS"]+=1
    
    if(x[0:5]=="01101"):           #invert
        reg1=reg[x[10:13]]
        reg2=reg[x[13:16]]
        val=format(reg_value[reg2], '016b')
        val_invert=""
        for i in val:
            if(i=="0"):
                i=1
            else:
                i=0
            val_invert+=str(i)
        reg_value[reg1]=int(val_invert,2)

    if(x[0:5] == "00101"):         #stores data from reg to var      #make for, for storing variable value in list_memory
        reg1=reg[x[5:8]]
        val = reg_value[reg1] #val = 5
        cycle_ldst.pop()
        cycle_ldst.append(int(x[8:16],2))
        var_dict[int(x[8:16],2)-len(input_list)] = format(val, '016b')
        var_count+=1

    if(x[0:5] == "00100"):         #load data from reg to var
        reg1=reg[x[5:8]]
        val=int(var_dict[int(x[8:16],2)-len(input_list)],2)
        cycle_ldst.pop()
        cycle_ldst.append(int(x[8:16],2))
        reg_value[reg1]=val

    if(x[0:5] == "01111"):
        #cycle_y[cycle_counter] = PC
        cycle_y.append(PC)
        jump_flag=True

    if(x[0:5] == "10000"):
        if(flag_val==4):
            cycle_y.append(PC)
            jump_flag=True
            

    if(x[0:5] == "10001"):
        if(flag_val==2):
            cycle_y.append(PC)
            jump_flag=True
    

    if(x[0:5] == "10010"):
        if(flag_val==1):
            cycle_y.append(PC)
            jump_flag=True

    PC_bin=format(PC, '08b')
    PC_and_regvals.append(PC_bin)
    PC_and_regvals.append(format(reg_value["R0"], '016b'))
    PC_and_regvals.append(format(reg_value["R1"], '016b'))
    PC_and_regvals.append(format(reg_value["R2"], '016b'))
    PC_and_regvals.append(format(reg_value["R3"], '016b'))
    PC_and_regvals.append(format(reg_value["R4"], '016b'))
    PC_and_regvals.append(format(reg_value["R5"], '016b'))
    PC_and_regvals.append(format(reg_value["R6"], '016b'))
    PC_and_regvals.append(format(reg_value["FLAGS"], '016b'))
    output_list.append(PC_and_regvals)
    if(jump_flag==False):
        cycle_y.append(PC)
    if(jump_flag):
        PC=int(x[8:16],2)
        continue
    PC=PC+1

for x in output_list:
    print(" ".join(list(map(str,x))))
    #print( " ".join(list(map(str,x))), file=sys.stderr)
for i in range(0 , var_count):
    list_memory.append(var_dict[i])
    
counter+=var_count
    
#for completing the output_list
for i in range(counter,256):
    list_memory.append("0000000000000000")  
    

for x in list_memory:
    x = x.strip('\n')
    print(x)
    #print(x , file=sys.stderr)

plt.scatter(cycle_x , cycle_y, c ="blue")
for i in range(0,len(cycle_ldst)):
    if cycle_ldst[i] != -1:
        plt.plot(i,cycle_ldst[i],'ro')

plt.show()
    
#first make a list for all the x- co ordinates of the graph , in that graph whenever an instruction is being executed
#the cycle_counter increases by 1

#for the y axis make another list in which you store the program counter
#make another list for handling ld and st functions