##Desafio ex056
"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.No final do programa, mostre:
--> A média de idade do grupo;
--> Qual é o nome do homem mais velho
--> Quantas mulheres têm menos de 20 anos"""

##Instanciando as variaveis:
sm=0
maioridadehomem=0
menoridadehomem=0
nomevelho=""
for i in range (1,3):
    print("{:-^25}".format(f"{i}ª PESSOA"))
    name=str(input(f"{i}ª informe-nos o seu nome: ")).capitalize()
    age=int(input(f"A sua Idade: "))
    sex=str(input(f"E o seu SEXO:[M/F] ")).upper().strip()
    sm+=age
    if i==1 and sex in "Mm":
        maioridadehomem=age
        nomevelho=name
    else:
        if sex in "Mm" and age>maioridadehomem:
            maioridadehomem=age
            nomevelho=name
        if sex in "Ff" and age<20:
            menoridadehomem+=1
media=sm/3
print(f"~~>A MÉDIA das idade doo grupo é {media}")
print(f"O homem mais velho do grupo tem {maioridadehomem} anos e o seu nome é {nomevelho}")
if menoridadehomem>0:
    print(f"Existem cerca de {menoridadehomem} que são menores de idade")