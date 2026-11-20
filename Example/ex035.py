#Desafio_035
#Desenvolva um programa que leia o
# comprimento de três retas e diga
# ao usuário, se elas podem ou não formar um triângulo

print("\033[1;35m-=-"*20)
print("Analisador de Triângulos")
print("-=-"*20,"\033[m")
#solicitando os dados no usuário:
r_1=int(input("\033[1;34mA 1ª recta: "))
r_2=int(input("A 2ª recta: "))
r_3=int(input("A 3ª recta: \033[m"))

#Principio DESIGUALDADE DE TRIÂNGULOS
"""
if r_1 + r_2 > r_3 and r_2+ r_3 > r_1 and r_3 + r_1 > r_2:
    print("Esses lados podem formar um triângulo.")
else:
    print("Não pode formar um triângulo.")"""

maior=max(r_1,r_2,r_3)

if maior < ((r_1 +r_2+r_3) - maior) :
    print("Eles \033[1;31mPODEM FORMAR\033[m um triângulo")
else:
    print("Eles \033[1;37;40mNÃO PODEM FORMAR\033[m um triângulo")