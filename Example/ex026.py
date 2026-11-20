##Desafio_026
#026: Faça um programa que leia uma frase pelo teclado
# e mostre quantas vezes aparece a letra "A", em que posição
# ela aparece a primeira vez e em que posição ela aparece a última vez.
t=str(input("Digite uma frase: ")).lower().strip()
print("A letra 'A' aparece ",t.count("a")," vezes!")
print(" A primeira letra apareceu na posição {}".format(t.find("a") + 1))
print("A ultima letra apareceu na posição {}".format(t.rfind("a") +1))
