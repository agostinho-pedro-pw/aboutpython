##Desafio ex036
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos ano ele vai
#pagr.
"""
Calcule o valor da prestaçao mensal, sabendo que ela não pode execeder 30% ou entt o empréstimo séra negado!
"""

##obtendo os dados do usuário
casa = float(input("Digite a valor da casa [Kz]: "))
salario= float(input("Informe-me nos o seu salário [Kz]: "))
anos= int(input("Quantos anos de fincanciamento? "))
prestacao= casa / (anos*12)
if prestacao <= salario*0.30:
    print(f"Para pagar uma casa de {casa} em {anos} anos"
      f"A prestação será de {prestacao:.2f} Kwanzas!")
else:
    print("Não é possível fazer esse empréstimo")
