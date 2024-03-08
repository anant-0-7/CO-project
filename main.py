

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
   "s1": "01001",
   "a0": "01010",
   "a1": "01011",
   "a2": "01100",  
   "a3": "01100",
   "a4": "01100",
   "a5": "01100",
   "a6": "01100",
   "a7": "01100",
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

print(imm_to_bin(0, 10)) 

f = open("text.txt","r")
read = f.readlines()
for i in read:

    words = i.split()
    i_list = []
    for word in words:
        i_list.extend(word.split(","))

    #R Type instructions
    if i_list[0] in r_type:
        if i_list == "sub":
            binary = ""
            binary += "0100000" + register_dict[i_list[1]]+ register_dict[i_list[2]]+ r_type[i_list[0]] + register_dict[i_list[3]]+"0110011"

        else:
            binary = ""
            binary += "0000000" + register_dict[i_list[1]]+ register_dict[i_list[2]]+ r_type[i_list[0]] + register_dict[i_list[3]]+"0110011"

    elif i_list[0] in i_type:
        binary = imm_to_bin(int(i_list[3]),12)
        s = binary + register_dict[i_list[2]] + i_type[i_list[0]][1] + register_dict[i_list[1]] + i_type[i_list[0]][0]
    
    if (i_list == []):
        continue
    print(i_list)
f.close()
 
