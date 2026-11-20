#Desafio_012
#Faça um algoritmo que leia o preço
# de um produto e mostre seu novo
# preço, com 5% de desconto.
preco=float(input("Informe o preço do produto:kz"))
desc=preco-(preco*5/100)
print("O desconto séra de 5% ficando: {:.1f}kz".format(desc))