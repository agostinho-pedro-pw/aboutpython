#Desafio_017
#Faça um progrma que leia
# o comprimento do cateto e adjacnte
# de um triângulo retângulo, calcule
# e mostre o comprimento da hipotenusa
print("\033[1;33m==>****🐍****<==\033[m")
o=float(input("\033[1;34mDigte o valor do cateto oposto: "))
a=float(input("Digite o valor do cateto adjacente: \033[m"))
'''sum=(o**2 + a**2)
from math import sqrt

hip= sqrt(sum)'''
print("\033[1;35mCateto Oposto ==> {} ".format(o))
print("Cateto Adjacente ==> {}\033[m".format(a))
#print("Portanto, A hepotenusa {:.2f}".format(hip))
from math import hypot
n="hipotenusa"
print("\033[1;37;40mO valor da {}{} séra: {:.2f}\033[m".format("\033[1;33;40m",n,hypot(a,o)))