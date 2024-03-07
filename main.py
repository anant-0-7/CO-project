#Random lines of code




print('Hello world')

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
