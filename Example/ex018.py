#Desafio_018
#Faça um programa que leia um ângulo
# qualquer e mostre na tela o valor
# do seno cosseno tangente desse angulo.

print("==>**🐍**<==")
a=float(input("Digite o valor do ângulo: "))
import math
s=math.sin(math.radians(a))
c=math.cos(math.radians(a))
t=math.tan(math.radians(a))
print("Portanto, o valor {} tem os seguintes ângulos :".format(a))
print("==> Seno: {:.2f}".format(s))
print("==> Cosseno:  {:.2f}".format(c))
print("==> Tangente: {:.2f}".format(t))