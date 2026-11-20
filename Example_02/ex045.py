##Desafio ex045
#ex:
"""
itens = ('PEDRA','PAPEL','TESOURA')
from random import randint
rad= randint(0,2)
print(f"A escolha foi de {itens[rad]}")"""
"""Crie um programa que faça o computador jogar Jokenpô com você"""
print("\n")
print("------------**-----------")
print("-----\033[32mJogo de Jokênpo\033[m-----")
print("------------**-----------");print("\n")
opt=int(input("Informe-nos : "
      "\n[1]--> Pedra"
      "\n[2]--> Papel"
      "\n[3]--> Tesoura"
      "\nR: "))

from random import randint
num=randint(1,3)

if opt >= 4:
    print("\033[1;31mOpcao invalida!\033[m")
from time import sleep
"""if opt < 4:
    print("PROCESSANDO...")
    sleep(1.5)"""
print("JO")
sleep(0.3)
print("KEN")
sleep(0.3)
print("PO!!!")
sleep(0.3);print("-="*15)
if num ==1:
    if opt == 1:
        print("COMPUTADOR: PEDRA")
        print("USUARIO: PEDRA")
        print("~>EMPATE")
    if opt ==2:
        print("COMPUTADOR: PEDRA")
        print("USUARIO: PAPEL")
        print("~>GANHOU")
    if opt ==3:
        print("COMPUTADOR: PEDRA")
        print("USUARIO: TESOURA")
        print("~>PERDEU")
elif num==2:
    if opt==1:
        print("COMPUTADOR: PAPEL")
        print("USUARIO: PEDRA")
        print("~>PERDEU")
    if opt ==2:
        print("COMPUTADOR: PAPEL")
        print("USUARIO: PAPEL")
        print("~>EMPATE")
    if opt ==3:
        print("COMPUTADOR: PAPEL")
        print("USUARIO: TESOURA")
elif num==3:
    if opt==1:
        print("COMPUTADOR: TESOURA")
        print("USUARIO: PEDRA")
        print("~>GANHOU")
    if opt ==2:
        print("COMPUTADOR: TESOURA")
        print("USUARIO: PAPEL")
        print("~>PERDEU")
    if opt ==3:
        print("COMPUTADOR: TESOURA")
        print("USUARIO: TESOURA")
        print("~>EMPATE")
print("-="*15)
"""
if opt==1 and num==1:
    print("COMPUTADOR: PEDRA")
    print("USUÁRIO: PEDRA")
    print("Empate 'Pedra vs Pedra'")
elif opt==2 and num==2:
    print("COMPUTADOR: PAPEL")
    print("USUÁRIO: PAPEL")
    print("Empate 'Papel vs Papel'")
elif opt==3 and num==3:
    print("Empate 'Tesoura vs Tesoura'")
elif opt==1 and num==2:
    print("Perdeu 'Papel mata Pedra'")
elif opt==1 and num==3:
    print("Ganhou 'Pedra mata Tesoura'")
elif opt==2 and num==1:
    print("Ganhou 'Papel mata Pedra'")
elif opt==2 and num==3:
    print("Perdeu 'Tesoura mata Papel'")
elif opt==3 and num==1:
    print("Perdeu 'Pedra mata Tesoura'")
elif opt==3 and num==2:
    print("Ganhou 'Tesoura mata Papel'")
"""
