##Desafio ex053
"""Crie um programa que leia um frase qualquer e diga se ela é um polídromo,
desconsiderando os espaços!"""
from idlelib.colorizer import prog_group_name_to_tag

print("{:=^40}".format("|>\033[1;31mDETECTOR DE POLÍNDROMO\033[m<|"))
word=str(input("Insira uma palavra: ")).strip().upper()
div=word.split()
junto="".join(div)##Junção, usando para juntar/concatenar a palavra fatiada
inverso=""
print(junto)
inverso=junto[::-1]##Reponsavel por armazenar o inverso da palavra
print(junto[::-1])
"""for i in range (len(junto)-1,-1,-1):
    inverso+=junto[i]"""
if inverso==junto:
    print(f"A frase digitada é um PALINDROMO! \033[1;31m{inverso}\033[m", end="")
else:
    print(f"A frase \033[40m{word}\033[m não é um PALINDROMO! \033[1;31m{inverso}\033[m")
