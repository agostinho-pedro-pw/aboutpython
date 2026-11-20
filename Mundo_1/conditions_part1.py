#Estudo de estrutura de condição simples!
#if & else
#sintaxe:
"""
if<condition>:
[true]
else:
[false]
"""
"""
n= str(input("Digite o seu nome: "))
if n =="Agostinho":
    print("Que nome lindo você tem, caba!")
else:
    print("O seu nome é tão normal!😂")
print("Bom dia, {}!".format(n))"""
n1= float(input("Digite a sua 1ª nota: "))
n2=float(input("Digite a sua 2ª nota: "))
m=(n1+n2)/2
##Blocos de comando:
if m>= 6:
    print("A sua média é otíma!👌")
else:
    print("A sua média foi péssima😶")