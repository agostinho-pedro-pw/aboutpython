#Desafio_008
#Escreva um programa quel leia
# um valor em metros e o exiba
# convertido em contrimétros e
# milimentros.

num=float(input("Digite o valor:"))
km=num/1000
hm=num/100
dam=num/10
dm=num*10
cm=num*100
mm=num*1000

print("==>km={}\n==>hm={}\n==>dam={}\n==>dm={}\n==>cm={}\n==>mm={}".format(km,hm,dam,dm,cm,mm))