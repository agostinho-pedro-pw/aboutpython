##Desafio ex054
"""Crie um progrmaa que leia o ano de nascimento de sete pessoas.
No final, mostre: quantas pessoas ainda não atingiuram a maoridade e quntas já são maiores
"""
##Obtendo as informações dos usuários
print("{:~^50}".format("|>\033[1;31mREGISTRO DE IDADE\033[m<|"))
menor=0
maior=0
tot=0
from datetime import date
from time import sleep
for i in range (1,3):
    idade=int(input(f" {i}º seu ano de nascimento: "))
    ##sleep(0.35)
    idade=date.today().year-idade
   ## print("\033[32m>-\033[m"*2)
    if idade>=21:
         maior+=1
    elif idade<21:
        menor+=1
if maior==0:
    print("Não existe \033[31mMAIORES\033[m de idade no sistema🔞 ")
if menor==0:
    print("Não existe \033[31mMENORES\033[m de idade no sistema🔞 ")
if maior>0:
    print(f"Existem cerca de {maior}ª usuário(s) \033[31mMAIORES\033[m de idade no sistema🥲")
if menor>0:
    print(f"Existem cerca de {menor}ª usuário(s) \033[31mMENORES\033[m de idade no sistema😒")
