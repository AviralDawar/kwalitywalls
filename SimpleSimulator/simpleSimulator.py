x=input() #00000_00_3bits_3bits_3bits
reg={'000':'R0','001':'R1','010':'R2','011':'R3','100':'R4','101':'R5','110':'R6','111':'FLAGS'}
reg_value={'R0':0,'R1':0,'R2':0,'R3':0,'R4':0,'R5':0,'R6':0,'FLAGS':0}

#FLAG=000000000000 VLGE

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
