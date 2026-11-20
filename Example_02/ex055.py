##Desafio ex055
"""Faça um programa que leia o peso de cinco pessoas. No final, mostre:
qual foi o maior e o menor peso lido."""
from idlelib.colorizer import prog_group_name_to_tag

##Instanciando a var idade
idade=0
menor=0
maior=0
for i in range (1,6):
    ##Obtendo as informações do usuário:
    peso=(float(input(f"\033[1;31m{i}ª\033[m insira o seu peso:[Kg] ")))
    if i==1:
        maior=peso
        menor=peso
    if i>1:
        if peso>maior:
            maior=peso
        if peso<menor:
            menor=peso

print(f"O maior peso lido foi de {maior}kg")
print(f"O menor peso lido foi de {maior}kg")