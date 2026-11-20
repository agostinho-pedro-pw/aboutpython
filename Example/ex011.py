#Desafio_012
#Faça um programa que leia a largura e a altura
# de uma parede em metros, calcule a sua área
# e a quantidade de tinta necessária para pintá-la
# , sabendo que cada litro de tinta, pinta uma área de 2m^2.

alt=float(input("Digite a Altura:"))
lar=float(input("Digite a Largura"))
area=(alt*lar)
qtd=area*1/2
print("A area da parede {}x{} é: {}m".format(alt,lar,area))
print("A qtd de tintas necessária para pintar a parede séra de: {}l".format(qtd))