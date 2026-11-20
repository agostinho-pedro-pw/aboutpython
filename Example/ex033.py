#Desafio_033
#Faça um programa que leia três
# números e mostre qual é o maior e qual é o menor
a=int(input("Digite o 1ª numero: "))
b=int(input("Digite o 2ª numero: "))
c=int(input("Digite o 3ª numero: "))

"""
max= max(a,b,c)
min= min(a,b,c)
print(f"O maior valor é {max}")
print(f"O menor valor é  {min} ")"""

if(a >= b) and a >= c:
    print(f"maior é {a}")
elif(b >= a) and b>= c:
    print(f"maior é {b}")
else:
    print(f"o maior é {c}")

if a <= b and a <= c:
    print(f"menor é {a}")
elif b <= a and b <= c:
    print(f"menor é {b}")
else:
    print(f"menor é {c}")