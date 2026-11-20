##Desafio_024
#024: Crie um programa que leia o nome de uma
# cidade diga se ela começa ou não com o nome "SANTO".
city=str(input("Digite o nome da sua cidade: ")).strip()
c=city.lower()
#print("santos" in c)
print(c[:6]=="santos")