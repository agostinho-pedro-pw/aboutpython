#Desafio_019_remaked
#Um professor quer sortear um dos
# seus quatro alunos para apagar o
# quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome do escolhido

a1=input("\033[1;32mDigite o nome do 1º aluno: ")
a2=input("Digite o nome do 2º aluno: ")
a3=input("Digite o nome do 3º aluno: ")
a4=input("Digite o nome do 4º aluno: \033[m")
lista=[a1,a2,a3,a4]
from random import choice
from time import sleep
print("\033[1;36mPROCESSANDO..\033[m")
sleep(2)
esc=choice(lista)
print("\n\033[1;35mO aluno escolhido foi \033[1;37;40m {} \033[m".format(esc))