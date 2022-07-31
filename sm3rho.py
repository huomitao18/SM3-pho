import random
from gmssl import sm3, func


def getrandinput(length):
    result = hex(random.randint(0,16**length)).replace('0x','')
    if(len(result)<length):
        result = '0'*(length-len(result))+result
    return result

def rho_birthday(n):
    length = n//4
    input = bytes(getrandinput(70),encoding='utf-8')
    Enc_inner = sm3.sm3_hash(func.bytes_to_list(input))
    Enc_outer = sm3.sm3_hash(func.bytes_to_list(bytes(Enc_inner,encoding='utf-8')))
    while True:
        Enc_inner=sm3.sm3_hash(func.bytes_to_list(bytes(Enc_inner,encoding='utf-8')))
        Enc_outer=sm3.sm3_hash(func.bytes_to_list(bytes(Enc_outer,encoding='utf-8')))
        Enc_outer=sm3.sm3_hash(func.bytes_to_list(bytes(Enc_outer,encoding='utf-8')))
        if sm3.sm3_hash(func.bytes_to_list(bytes(Enc_inner,encoding='utf-8')))[0:length] == sm3.sm3_hash(func.bytes_to_list(bytes(sm3.sm3_hash(func.bytes_to_list(bytes(Enc_outer,encoding='utf-8'))),encoding='utf-8')))[0:length]:
            break
    return Enc_inner,sm3.sm3_hash(func.bytes_to_list(bytes(Enc_outer,encoding='utf-8')))




if __name__=='__main__':
    lencoll=int(input("please enter the length collision:"))
    a1,a2=rho_birthday(lencoll)
    print(a1,a2,'\n',end=' ')

    enc_a1=bytes(a1,encoding='utf-8')
    enc_a1= sm3.sm3_hash(func.bytes_to_list(enc_a1))
    print(a1,':',enc_a1)

    enc_a2=bytes(a2,encoding='utf-8')
    enc_a2= sm3.sm3_hash(func.bytes_to_list(enc_a2))
    print(a2,':',enc_a2)