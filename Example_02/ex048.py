##Desafio ex048
"""
    Faça um programa que calcule a soma entre todos os números ímpares
    que são múltiplos de três e que se encontram no intervalo de 1 até 500.
"""
#Qdo é que um número é ímpar..?
"""R: Um número é impar qdo o resto da divisão por dois é diferente de zero!
ex. n%2!=0: IMPAR"""
print("{:~^35}".format("|>\033[1;31mSOMADOR IMPAR\033[m<|"));print("")
sum=0
i=int(input("~~>INICIO: "))
f=int(input("~~>FIM: "));print("")
for c in range(i,f+1,1):
    if c%2!=0 and c%3==0:
        sum+=c

print(f"Portanto, a \033[1;32mSOMA\033[m de todos os nºs \033[1;31mÍMPARES\033[m multiplos de 3 séra de \033[1;40m {sum} \033[m")
