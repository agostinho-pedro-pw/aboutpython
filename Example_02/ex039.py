import datetime
from datetime import date
"""Faça um programa que leia o ano de nasciemento de um
 jovem e informe de acordo com sua idade:

  --> se ele ainda vai se alistar ao serviço militar
  --> se é a hora de se alistar
  --> se já passou do tempo de alistamento
  Seu programa tbm deverá mostrar o tempo que falta ou que passou do prazo.
  """

ano= int(input("Digite o seu ano de nascimento: "))
"""
if ano >= 18 and ano <= 24:
    ano = 24 - ano
    print(f" tens  cerca de {ano} anos, para se alistar no serviço militar")
elif ano >=24:
    ano = ano - 24
    print(f"Já se passaram cerca de {ano} anos, desde o seu alistamento militar")
elif ano < 18:
    ano = 18 - ano
    print(f"Faltam cerca de {ano} anos, para o teu alistamento militar")"""
idade= date.today().year-ano
if idade == 18:
    print("Você tem que se alistar IMEDIATAMENTE!")
elif idade < 18:
    saldo= 18 - idade
    sd= date.today().year+saldo
    print(f"Você ainda não pode se alistar, faltam {saldo} ano(s).no caso séra em {sd}")
elif idade > 18:
    saldo = ano - 18
    sd= date.today().year-saldo
    print(f"Você já deveria ter se alistado há {saldo} ano(s), em {sd} ")
elif idade >= 24:
    saldo= idade-24
    sp= date.today().year-saldo
    print(f"O seu alistamento já passou do prazo. Foi há {saldo} ano(s) em {sp}")