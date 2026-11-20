#Desafio_004: Faça um programa que leia algo pelo
# teclado e mostre na tela o sei tipo primitivo e
# todas as informações possíveis sobre ele!

text= input("Digite algo: ")
print("O tipo primitvo de :",type(text))
print("É um texto..? ",text.isalpha())
print("É um número..? ",text.isnumeric())
print("É um AlfaNumerico..? ",text.isalnum())
print("Contém espaço..?",text.isspace())
print("Está em maiúsculas?",text.isupper())
print("Está capitalizada?",text.istitle())
print("Está alguma coisa..?{}".format(text.isdecimal()))
