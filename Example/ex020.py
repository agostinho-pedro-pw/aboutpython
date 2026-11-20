#Desafio_020
#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos
# ..Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

a1=input("Insira o 1º nome: ")
a2=input("Insira o 2º nome: ")
a3=input("Insira o 3º nome: ")
a4=input("Insira o 4º nome: ")
from random import shuffle
lista = [a1,a2,a3,a4]
shuffle(lista)
print("A ordedm de apresentação séra: ")
print(lista)
