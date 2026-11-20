##Desafio ex041
"""A confideração nacional de Natação precisa
de um programa que leia o ano de nascimento ded um atleta
e mostre sua categoria de acordo com a idade:

--> até 9 anos : MIRM
--> até 14anos : INFANTIL
--> até 19anos: JUNIOR
--> até 20anos: Sênior
--> acima :MASTER"""
##obtendo os dados do usuário
age= int(input("\033[32mInsira o seu ano de nascimento:\033[m "))
from datetime import date
age = date.today().year - age
##usando condições aninhadas
if age <=9:
    print("Level: \033[1;31mMIRIM\033[m")
elif age <=14:
    print("Level: \033[1;31mINFANTIL\033[m")
elif age <=19:
    print("Level: \033[1;31mJUNIOR\033[m")
elif age <=20:
    print("Level: \033[1;31mSÊNIOR\033[m")
else:
    print("Level: \033[1;31mMASTER\033[m")
