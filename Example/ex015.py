#Desafio_015
#EScreva um programa que pergunte a quantidade
# de km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado.Calcule o preço a pagar
#, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado!

km=float(input("Insira a quantidade de km rodados: "))
qtd=int(input("Insira os dias ultilizados: "))
res=((qtd*60)+(km*0.15))
print("Portanto, o Carro foi alugado para {}dia(s) e percorreu cerca de {}Km \nO valor a pago séra de: {}R$".format(qtd,km,res))