#Desaio_032
#faça um programa que leia
# um ano qualquer e mostre
# se ele é "BISSEXTO".

from datetime import datetime
print("==>",datetime.now(),"<==");print("\n")
ano= int(input("\033[1;47;40mInforme o ano:\033[m "))
if ano == 0:
    ano= datetime.now().year
#condição de um ano Bissexto:
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0) :
    print(f"\033[1;35mO ano {ano} é \033[0;0;40mbissexto!\033[m")
else:
   print(f"\033[1;35mO ano {ano} \033[0;0;31mnão é bissexto\033[m")

'''
date= datetime.now()
print(f" A sua data é {date.day} / {date.month} / {date.year} ")'''