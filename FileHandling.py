reg_codes={"zero":"00000", "ra":"00001", "sp":"00010", "gp":"00011", "tp":"00100",
   "t0":"00101", "t1":"00110", "t2":"00111", "s0":"01000", "fp":"01000",
   "s1":"01001", "a0":"01010", "a1":"01011", "a2":"01100", "a3":"01101",
   "a4":"01110", "a5":"01111", "a6":"10000", "a7":"10001", "s2":"10010",
   "s3":"10011", "s4":"10100", "s5":"10101", "s6":"10110", "s7":"10111",
   "s8":"11000", "s9":"11001", "s10":"11010", "s11":"11011", "t3":"11100",
   "t4":"11101", "t5":"11110", "t6":"11111"}


r_codes = {'add':"000", 'sub':"000", 'sll':"001",'slt':"010", 'sltu':"011", 'xor':"100", 'srl':"101", 'or':"110", 'and':"111"}
r_codes_keys = r_codes.keys()

i_codes = {"lw": ["0000011","010"], "addi": ["010011","000"], "sltiu": ["010011","011"], "jalr":["110011","000"]}
i_codes_keys = i_codes.keys()

s_codes = {"sw": ["0100011", "010"]}
s_codes_keys = s_codes.keys()

b_codes = {"beq": "000", "bne": "001", "blt": "100", "bge":"101", "bltu": "110", "bgeu": "111"}
b_codes_keys = b_codes.keys()

u_codes = {"lui":"0110111", "auipc":"0010111"}
u_codes_keys = u_codes.keys()

j_codes = {"jal": "1101111"}
j_codes_keys = j_codes.keys()

f = open("text.txt","r")
read = f.readlines()
for i in read:
    i_list = i.split()
    if i_list == []:
        continue
    elif i_list[0] in r_codes_keys or i_list[0] in i_codes_keys or i_list[0] in s_codes_keys or i_list[0] in b_codes_keys or i_list[0] in u_codes_keys or i_list[0] in j_codes_keys:
        print(i_list)
    else:
        print("Syntax Error")
    

f.close()