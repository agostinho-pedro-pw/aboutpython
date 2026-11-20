"""EScreva um programa que leia dois números inteiros
 e os compare-os mostrando na tela uma mensagem:

--> O primeiro valor é o maior
--> O segundo número é o maior
--> Não existe valor maior, os dois são iguais"""

num=int(input("Insira um número: "))
num2=int(input("Insira outro número: "))
if num>num2:
    print(f"{num} > {num2}")
elif num<num2:
    print(f"{num} < {num2}")
else:
    print(f"{num} == {num2}")