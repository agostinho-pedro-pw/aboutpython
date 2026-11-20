##Desafio ex052
"""Faça um programa queleia um número inteiro e diga se ele é ou não um número primo"""
print("{:=^50}".format("|>\033[1;31mDETECTOR DE NUMEROS PRIMOS\033[m<|"));print("")
num=int(input("Insira o número: "));print("")
"""if 1<=num<=500:
    if num%2!=0:
        print("~~>É um \033[1;32mNUMERO PRIMO!👌\033[m")
else:
    print("O número é muito grande!"
          "Tens que me pagar \033[1;40m 200kz \033[m😒🚫")"""
tot=0
if 1<=num<=50:
    for i in range(1,num+1):
        if num % i ==0:
            tot += 1
            print("\033[34m", end=" ")
        else:
            print("\033[31m",end=" ")
        print(f"{i}\033[m",end=" ")
    if num % 2!=0:
        print(f"\nO nº {num} foi dividido apenas {tot}vezes, portanto ele é \033[40mPRIMO!\033[m")
    else:
        print(f"\nPortanto, o número {num} ñ é \033[40mPRIMO!\033[m")
else:
    print("Número muito \033[1;31mGRANDE..\033[m",end="");print("Tens que me pagar \033[40m 200kz🚫😒\033[m")
