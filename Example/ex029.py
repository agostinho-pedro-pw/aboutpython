#Desafio_ex029
#EScreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo
# "Você foi multado seu safado!"
#A vai custar 1,200kz por cada km acima do limite..
v=float(input("Qual foi a sua velocidade: "))
if v>80:
    m=(v-80)*1200
    print("Meu CABA, você foi multado! \n"
          f"A sua multa será de 1,200kz por cada [km] acima do limite ficando : {m}kz")
else:
    print("Bem, você esteve abaixo do LIMITE de velocidade!👍")
    print("Muito bem, CABA!")
