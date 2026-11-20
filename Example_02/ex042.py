##Desafio ex042
"""REfaça o desafio 035 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo
séra formado:
--> Equilátero : todos os lados iguais
--> Isóscelee: dois lados iguais
--> Escaleno: todos os lados diferentes"""
##Obtendo os valorees do triangulo
a= int(input("~~>Recta 1º: "))
b= int(input("~~>Recta 2º: "))
c= int(input("~~>Recta 3º: "))

sum = max(a,b,c)#modulo math
##Estrutura de condições aninhadas
if sum < (a + b + c)- sum and a != b and a!=c and b!=c:
    print("Eles podem formar um TRIANGULO, \033[1;35mESCALENO\033[m")
elif sum < (a + b + c) -sum and a == b and a==c:
    print("Podem sim formar um TRIANGULO, \033[1;32mEQUILÁTERO\033[m")
elif sum < (a + b + c) - sum and a == b or a==c or b==c:
    print("Eles podem formar um TRIANGULO \033[1;31mESÓSCILES\033[m")
else:
    print("Não podem formar um TRIANGULO")
