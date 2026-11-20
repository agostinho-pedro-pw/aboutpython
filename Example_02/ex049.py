##Desafio ex049
"""Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher,
    só que agora ultilizando um laço de repetição"""
print("{:~^35}".format("~~|>\33[1;31mTABUADA\033[m<|~~"))
n=int(input("Insira um número 😒: "))
if 1<=n<=12:
    for i in range(1,12+1):
        print("-"*12)
        print(f"{n} X {i} = {n*i}")
else:
    print("Tens que pagar \033[1;40m200kz\033[m🚫")
print("{:~^28}".format("|>\033[1;31mFIM\033[m<|"))
