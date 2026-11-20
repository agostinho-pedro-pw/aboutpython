#Desafio
#Crie um programa que leia quanto
# dineiro uma pessoa tem na carteira
# e mostre quantos dolares ela pode comprar
#
#considere:
#US$1.0=1000kz

num=float(input("Insira o seu dinheiro:"))
calc=num/918
print("Com {}kz em dolares terás: {:.3f}$".format(num,calc))