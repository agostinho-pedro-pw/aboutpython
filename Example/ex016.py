#Desafio_015
#Crie um programa que leia um número real
# qualquer pelo teclado e mostre na tela a
#  sua porção inteira

#ex: Digite um número: 6.12321
#O número 6.12321 tem a sua parte 6.

num=float(input("Digite um número real :"))
'''from math import ceil #trunc
print("O número {} tem a sua parte inteira {}".format(num,ceil(num)))'''
print("O numero {} tem a sua parte inteira {}".format(num,int(num)))