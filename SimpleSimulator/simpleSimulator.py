input_list = list(map(str, sys.stdin.readlines()))
counter=len(input_list)
list_memory=input_list
reg={'000':'R0','001':'R1','010':'R2','011':'R3','100':'R4','101':'R5','110':'R6','111':'FLAGS'}
reg_value={'R0':0,'R1':0,'R2':0,'R3':0,'R4':0,'R5':0,'R6':0,'FLAGS':0}
var_dict = {}
var_count = 0
for i in range[counter,256]:
    list_memory.append("0000000000000000")
i=0
while(i<len(input_list))
    x=input_list[i]
    if(x[0:5]=="00000"):
        reg1=reg[x[7:10]]
        reg2=reg[x[10:13]]
        reg3=reg[x[13:]]
        reg_value[reg1]=reg_value[reg1]+reg_value[reg2]
    
    
        if(reg_value[reg1]>=256):
            reg_value["FLAGS"]=0
            reg_value["FLAGS"]+=8
        
   
    if(x[0:5]=="00001"):
        reg1=reg[x[7:10]]
        reg2=reg[x[10:13]]
        reg3=reg[x[13:]]
        reg_value[reg1]=reg_value[reg1]-reg_value[reg2]
        
        
        if(reg_value[reg1]<0):
            reg_value["FLAGS"]=0
            reg_value["FLAGS"]+=8
            reg_value[reg1]=0
            
    if(x[0:5]=="00110"):
        reg1=reg[x[7:10]]
        reg2=reg[x[10:13]]
        reg3=reg[x[13:]]
        reg_value[reg1]=reg_value[reg1]*reg_value[reg2]
        
        
        if(reg_value[reg1]<0 or reg_value[reg1]>256 ):
            reg_value["FLAGS"]=0
            reg_value["FLAGS"]+=8

    if(x[0:5]=="00010"):
        #imm
        reg1=reg[x[5:8]]
        imm=int(x[8:],2)
        reg_value[reg1]=imm
        
    if(x[0:5]=="01001"):
        #left_shift
        reg1=reg[x[5:8]]
        imm=int(x[8:],2)
        reg_value[reg1]= int(reg_value[reg1])<<imm

    if(x[0:5]=="01000"):
        #right_shift
        reg1=reg[x[5:8]]
        imm=int(x[8:],2)
        reg_value[reg1]= int(reg_value[reg1])>>imm
    if(x[0:5]=="00111"):           #divide
        
        reg1=reg[x[10:13]]
        reg2=reg[x[13:]]
        
        reg_value["R0"]=int(reg_value[reg1]/reg_value[reg2])
        reg_value["R1"]=reg_value[reg1]%reg_value[reg2]

    if(x[0:5]=="01110"):        #compare
        
        reg1=reg[x[10:13]]
        reg2=reg[x[13:]]
        
        if reg_value[reg1]>reg_value[reg2]:
            reg_value["FLAGS"]=0
            reg_value["FLAGS"]+=2
        elif reg_value[reg1]<reg_value[reg2]:
            reg_value["FLAGS"]=0
            reg_value["FLAGS"]+=4
        else:
            reg_value["FLAGS"]=0
            reg_value["FLAGS"]+=1
    
    if(x[0:5]=="01101"):           #invert
        
        reg1=reg[x[10:13]]
        reg2=reg[x[13:]]
        
        reg_value[reg1]= (~reg_value[reg2])

    if(x[0:5] == "00101"):         #stores data from reg to var      #make for, for storing variable value in list_memory
        reg1=reg[x[5:8]]
        val = reg_value[reg1] #val = 5
        var_dict[int(x[8:],2)-len(input_list)] = format(val, '016b')
        var_count+=1

    if(x[0:5] == "00100"):         #load data from reg to var
        reg1=reg[x[5:8]]
        val=var_dict[int(x[8:],2)-len(input_list)]
        reg_value[reg1]=val

    

    