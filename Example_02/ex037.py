##Desafio_037
"""Escreva um programa que leia um número inteiro
qualquer e peça para o usuário escolher qual será´a base de conversão

ex:. 1 para binário
ex. 2 para octal
ex. 3 para hexadecimal"""

print("--------------------**----------------------")
num = int(input("Digite um número inteiro: "))
print(" :. 1 para binário")
print(" :. 2 para octal")
print(" :. 3 para hexadecimal")
opcao=int(input("Digite uma opção: "))
import math
if opcao ==1:
    print(f" O número {num} para binario é {bin(num)[2:]}")
elif opcao== 2:
    print(f" O número {num} em octal é {oct(num)[2:]}")
elif opcao==3 :
    print(f" O número {num} em hexadecimal é {hex(num)[2:]}")
else:
    print("Opção invalida!")