

register_dict = {
   "zero": "00000",
   "ra": "00001",
   "sp": "00010",
   "gp": "00011",
   "tp": "00100",
   "t0": "00101",
    "t1": "00110",
    "t2": "00111",
    "s0": "01000",
    "s1": "01001",
   "a0": "01010",
   "a1": "01011",
   "a2": "01100",  
   "a3": "01101",
   "a4": "01110",
   "a5": "01111",
   "a6": "10000",
   "a7": "10001",
   "s2": "10010",  
   "s3": "10011",
   "s4": "10100",
   "s5": "10101",
   "s6": "10110",
   "s7": "10111",
   "s8": "11000",
   "s9": "11001",
   "s10": "11010",
   "s11": "11011",
   "t3": "11100",  
   "t4": "11101",
   "t5": "11110",
   "t6": "11111",
}

r_type = {'add':"000", 'sub':"000", 'sll':"001",'slt':"010", 'sltu':"011", 'xor':"100", 'srl':"101", 'or':"110", 'and':"111"}
#Funct7 is all zero except in sub which is 0100000
#Opcode is 0110011

i_type = {"lw": ["0000011","010"], 
          "addi": ["010011","000"], 
          "sltiu": ["010011","011"], 
          "jalr":["110011","000"]}

s_type = {"sw": ["0100011", "010"]}

b_type = {"beq": "000", "bne": "001", "blt": "100", "bge":"101", "bltu": "110", "bgeu": "111"}
#opcode for all is 110001

u_type = {"lui":"0110111", "auipc":"0010111"}
#No funct3 required

j_type = {"jal": "1101111"}
#no funct3




def tows_complement(binary):
    ones_complement = ''
    for i in binary:
        if i=='1':
            ones_complement += '0'
        else:
            ones_complement += '1'

    result = ''
    carry = True
    for i in ones_complement[::-1]:
        if i == '0' and carry:
            result = '1' + result
            carry = False
        elif i == '1' and carry:
            result = '0' + result
        else:
            result = i + result

    return result


def imm_to_bin(a, no_of_bits):
    n = abs(int(a))
    binary = ''
    while n:
        binary = str(n % 2) + binary
        n //= 2
        
    length = no_of_bits - len(binary)
    final = length * '0'
    binary1 = final + binary

    if int(a) < 0:
        binary1= tows_complement(binary1)
        
    return binary1


f = open("text.txt","r")
read = f.readlines()
count = 1
labels=[]
for i in read:
  s = ""
  j = 0
  while j < len(i):
      if i[j] == ":":
          labels.append(s)
          s = ""
          break
      s += i[j]
      j += 1


for i in read:

    words = i.split()
    i_list = []
    for word in words:
        i_list.extend(word.split(","))
    if(len(i_list) != 0):   #check whether the line is not empty
        if '(' in i_list[-1]:
            inst = i_list[-1].split("(")
            i_list[2] = inst[1][0:-1]
            i_list[3] = inst[0]
    else:   #if line is empty then continue
        continue
    if ":" in i:
        print("There is a label here.")
        continue

    #R Type instructions
    if i_list[0] in r_type:
        if i_list == "sub":
            binary = ""
            binary += "0100000" + register_dict[i_list[3]]+ register_dict[i_list[2]]+ r_type[i_list[0]] + register_dict[i_list[1]]+"0110011"

        else:
            binary = ""
            binary += "0000000" + register_dict[i_list[3]]+ register_dict[i_list[2]]+ r_type[i_list[0]] + register_dict[i_list[1]]+"0110011"

    
    #I Type
    elif i_list[0] in i_type:
        binary = imm_to_bin(int(i_list[2]),12)
        binary+=register_dict[i_list[3]] + i_type[i_list[0]][1] + register_dict[i_list[1]] + i_type[i_list[0]][0]
    
    #S Type
    elif i_list[0] in s_type:
        binary=imm_to_bin(int(i_list[2],12))
        binary+=binary[0:7]+register_dict[i_list[3]]+register_dict[i_list[1]]+"010"+binary[7:12]+s_type[i_list[0]][0]
    
    #B Type
    elif i_list[0] in b_type:
        binary=imm_to_bin(int(i_list[3]),13)
        binary+=binary[12]+binary[5:11]+register_dict[i_list[1]]+register_dict[i_list[2]]+binary[1:5]+binary[11]+b_type[i_list[0]]

    #U TYPE
    elif i_list[0] in u_type:
        given_value=int(i_list[2])
        if(given_value<-2**31 or given_value> 2**31-1):
            print(f"ERROR on line {count+1}:the immediate value is out of bounds")
            break
        
        imm=imm_to_bin(int(i_list[2]),32)
        binary=imm[1:21]+register_dict[i_list[1]]+u_type[i_list[0]]

    # J TYPE
    elif i_list[0] in j_type:
        given_value=int(i_list[2])
        if(given_value<-2**20 or given_value> 2**20-1):
            print(f"ERROR on line {count+1}:the immediate value is out of bounds")
            break


        imm=imm_to_bin(int(i_list[2]),21)
        binary=imm[1]+imm[10:20]+imm[10]+imm[2:10]+register_dict[i_list[1]]+"1101111"

    else:
        print("ERROR: Invalid Instruction")
    if (i_list == []):
        continue
    print(binary)
    binary = ""
    
f.close()