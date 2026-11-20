##Desafio ex043
"""Desenvolva uma lógica que leia o peso e a altura
de um pesso, calcule o seu IMC e mostre sei status, de acorso com a tabela abaixo:
--> Abaixo de 18.5: Abaixo do Peso
--> Entre 18.5 e 25: Peso ideal
--> 25 até 30: Sobrepeso
--> 30 até 40 : Obesidade
--> Acima de 40: Obesidade mórbida"""

##IMC~~> Indíce de Massa corporia

print("----------**-----------")
print("------->\033[1;31mStatus\033[m<--------")
print("----------**-----------");print("")
peso=float(input("Informe-nos o seu peso [Kg]: "))
altura=float(input("Informe-nos o seu altura [m]: "));print("")
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f"\033[1;31m~~>Abaixo do peso\033[m ~~> IMC ={imc:.2f}")
elif 18.5 <= imc < 25:
    print(f"\033[1;32m~~>Peso ideal\033[m ~~> IMC ={imc:.2f}")
elif 25 <= imc < 30:
    print(f"\033[1;33m~~>Sobrepeso\033[m ~~> IMC ={imc:.2f}")
elif 30 <= imc < 40:
    print(f"\033[1;33m~~>Obesidade\033[m ~~> IMC ={imc:.2f}")
elif imc > 40:
    print(f"\033[1;31m~~>Obesidade mórbida\033[m ~~> IMC ={imc:.2f}")
else:
    print(f"Impossível😒🚫")
