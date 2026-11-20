##Desafio ex047
"""Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50"""

##n=int(input("Digite um número:"))
"""
if n % 2 == 0:
    print("PAR")
else:
    print("IMPAR")"""
"""
print("{:~^15}".format(">\033[1;31mPAR\033[m<"))
for i in range (1,50):
    if i%2==0:
        print("~~>PAR: ",i)
    elif i%2!=0:
        print(f"~~>IMPAR: {i}")
"""
print("{:~^20}".format(">\033[1;31mPAR\033[m<"))
i=int(input("INICIO: "))
f=int(input("FIM: "));print("")
for c in range(i,f+1,1):
    if c%2==0:
        print(f"~~>PAR: {c}")



