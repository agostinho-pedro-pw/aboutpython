#Defasio_ex031
#Desanvolva um programa que pergunte a distância
# de uma viagem em km. Calcule o preço da passagem,
#cobrando R$0,50 por Km para viangens de até 200km e
#R$ 0,45 para viagens mais longas!

dist=float(input("\033[1;47;40mQual foi a distância da viagem:\033[m "))

'''
if dist<=200:
    print(f"Você pretende fazer uma viagem de {dist}km,", end="")
    print(f"a sua viajem custará cerca de: {dist*0.50:.2f}R$")
else:
    print(f"o Custo da viajem será de: {dist*0.45:.2f}R$")'''
preco= dist* 0.50 if dist <= 200 else dist* 0.45 ## no python não temos
#operadores ternários
print(f"\033[1;35mO preço da viajem séra de : {preco:.2f}R$")