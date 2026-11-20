##Desafio_027
#027: Faça um programa que leia o nome completo
# de uma pessoa, mostrando em seguida o primeiro
# e o último nome separadamente.
n=str(input("Digite o seu nome completo: ")).strip()
c=n.capitalize().split()
#<DEV/Thunder!>
#Caso batido com só um pouqinho de lógica e mais  nada!
#print("Seja bem-vindo sr(a),{} {}".format(c[0],c[-1].title()))
print("Seja bem-vindo sr(a) ,{} {}".format(c[0],c[len(c)-1]))