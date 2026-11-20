#Desafio_019
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo nome deles e escrevendo o nome do escolhido.
import random
from random import randint
sort=random.randint(1,10)
print("\033[1;38m")
print("----------**---------")
print("Tendo a seguinte lista:")
print("\n----------**---------")
print("==> 1.Agostinho Pedro")
print("==> 2.Acácio Manuel")
print("==> 3.Manuel Domingos")
print("==> 4.Inácio Jacinto")
print("==> 5.Miguel Salazar")
print("==> 6.Minga João")
print("==> 7.Jacinto TChipa")
print("==> 8.Victor Hugo Mendes")
print("==> 9.Mário de Oliveira")
print("==> 10.Miguel Maya\033[m")

print("\n----------**---------")
print("O aluno sorteado é o [ {} ] Parabens!😂".format(sort))