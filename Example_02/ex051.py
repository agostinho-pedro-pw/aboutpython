##Desafio ex051
"""
Desenvolva um programa queleia o primeiro termo e a razão de uma PA.
No final, mostre: os 10 primeiros termos dessa progressão.
"""
from idlelib.colorizer import prog_group_name_to_tag

## termo Geral: u= u1 + (d-1)*r

print("{:~^45}".format("|>\033[1;31mPROGRESSÃO ARIIMETRICA\033[m<|"));print(".")
p=int(input("Insira o Primeiro termo: "))
r=int(input("Insira a razão: "))
term=0
print("{:~^40}".format("\033[1;31mOS TERMOS DE UMA PA\033[m"))
for c in range(1,11):
    term= p +(c-1)*r
    print(f"({c}ª)~>{term}")

"""
sum = 0
for c in range(2,21,2):
    sum+=c
    print(c)
print(sum)"""

