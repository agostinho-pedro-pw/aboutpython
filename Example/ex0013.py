#Desafio_013
#Faça um algoritmo que leia o salário
# de um funcionário e mosntre seu novo
# salário com 15% de aumento.
sal=float(input("Insira o seu salário: Kz"))
aum=sal+(sal*15/100)
print("Portanto,você receberá um aumento de 15% ficando: {:.2f}kz".format(aum))