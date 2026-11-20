##Estrutras de repetição
"""
    sintaxe:
    for c in range(1,5):
        passo
    pega
"""
"""
n=int(input("Digite um número: "))
for c in range(0,n+1):
    print(c)
print("FIM")"""
i=int(input("Inicio:"))
f=int(input("Fim:"))
p=int(input("Salto:"))

for c in range(i,f+1,p):
    print(c)
s=0
for c in range(0,3):
    n=int(input("Digite um numero: "))
    s+=n
print(f"O Somaotorio foi de {s}")

