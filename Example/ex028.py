##Desafio_028
#Escreva um progrrama que faça o computador
# "pensar!" em um número inteiro entre 0 e 5
# e peça para o usúario tentar descobrir
# qual foi o número escolhido pelo computador!

#O programa deverá escrever na tela se o usúario venceu ou perdeu

#importando a biblioteca time.
import time
from time import sleep ##modulo time//muito bom!
import random
num=random.randint(0,5)#modulo random.

print("\033[1;32m==>**🐍**<==\033[m")
print("=="*10)
n=int(input("Advinhe o número entre [0,5]: "))
print("=="*10)
print("\033[1;35mProcessando...\033[m")
sleep(2)
if n == num :
    print(f"Safado! você acertou! \nfoi examente {num}")
else:
    print(f"\033[1;34mERROU!😂 o número escolhido foi {num} tente novamente!\033[m")
print("\033[1;35m=="*10)