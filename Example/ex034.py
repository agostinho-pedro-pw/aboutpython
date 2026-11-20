#Desafio_ex034
#Escreva um programa que pergunte o salário
# de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1.250,00, calcule um aumento de 10%
#Para os inferiores ou iguais, o aumento é de 15%

from time import sleep

sal=float(input("Informe-nos o seu salário:R$"))
if sal >= 1.250:
    aum=sal + (sal*10/100)
    print(f"O seu aumento séra de {aum:.2f}R$")
else:
    aum=sal + (sal*15/100)
    print(f"O seu aumento séra de {aum:.2f}R$")

print("PROCESSANDO...")
sleep(2)