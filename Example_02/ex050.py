##Desafio ex050
"""Desenvolva um programaque leia seis numéros inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor for impar o desconsidere!"""
from inspect import cleandoc

from django.contrib.sessions.management.commands import clearsessions

##Obtendo os números do usuário
i=int(input("Qtd de números a ler: "))
soma=0
cont=0
if 1<=i<=12:
    print("{:~^45}".format("|>\033[1;31mSOMA DOS NÚMEROS PARES\033[m<|"))
if 1<=i<=12:
    for c in range(1,i+1,1):
        num= int(input(f"Digite o {c}º \033[1;40mnúmero:\033[m "))
        if num%2==0:
            soma+=num
            cont+=1
if 1<=i<=12:
    print(f"Foi encontrado {cont} numeros pares,soma dos \033[1;32mPARES\033[m séra: {soma}")
else:
    print("\033[1;31mSOMA\033[m mto grande,"
    "Tens que pagar \033[1;40m 200kz🚫😒 \033[m")
