##Desafio exx046
"""
    Faça um programa que mostre na tela uma contagem regressiva para o astouro de fogos de artificio
    indo de 10 até 0, com uma pausa ded 1 segundo entre eles!
"""

from time import sleep
print("{:~^40}".format(">\033[1;31mCONTADOR REGRESSIVO\033[m<"))
for c in range(10,0,-1):
    print(f"~~> {c}")
    sleep(0.7)
print("BUM!🤯")
print("~~"*10)
