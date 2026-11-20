##Desafio_022
#Crie um programa que leia o nome completo de uma pessoa e mostre:
#
#=>O nome com todas as letras maísculas
#=>O nome com todas minúsculas
#=>Quantas letras ao todo(Sem considerar espaços).
#=>Quantos letras tem o pirmeiro nome.

name=str(input("Digite o seu nome: ")).strip()
#Manipulating text!
ma=name.upper()
mi=name.lower()
print("O seu nome maísculo: \n==>{}".format(ma))
print("O seu nome minúsculo: \n==>{}".format(mi))
div=name.split()#==> usado para divir a string! ex: div=["..","..",".."]
#print("O primeiro nome tem: {} letras ".format(len(div[0])))
#counting with no space
print("Seu nome tem ao todo {} letras ".format(len(name) - name.count(" ")))
print("O seu primeiro nome de {} letras ".format(name.find(" ")))
print("O seu primeiro nome: {} ",format(len(div[0])))