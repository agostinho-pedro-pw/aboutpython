##Desafio ex040
"""Crie um programa que leia duas notas de um aluno
e calcule sua me´dia mostrando uma mensagem no final, de acordo
com a média atingida:
--> méia abaixo de 5.0: REPROVADO
--> média entre 5.0 e 6.9 : RECUPER(AÇÃO
--> méddia 7.0 ou superior : APROVADO"""

nota1=float(input("Insira a primeira nota: "))
nota2=float(input("Insira a segunda nota: "))
media = (nota2 +nota1)/2
##Usando condições aninhadas com python
if media < 5.0:
    print(f"REPROCADO, com uma média de {media:.2f}v")
elif media >= 5.0 and media <= 6.9:
    print(f"RECUPERAÇÃO, com uma média de {media:.2f}v")
elif media >=7 and media <=10:
    print(f"APROVADO, com uma média de {media:.2f}v")
else:
    print("IMPOSSÍVEL, parente!😒")
