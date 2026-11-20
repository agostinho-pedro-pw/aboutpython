##Desafio ex044
"""Elabore um programd«a que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
-> À vista dinheiro/cheque : 10% de desconto
--> À vosta no cartão: 5% de desconto
--> em até 2x no cartão: preço normal
--> 3x ou mais no cartão: 20% de juros"""
print("------------**------------")
print("~~>\033[1;31mSistema de Pagamento\033[m<~~")
print("------------**------------")
price=float(input("Informe-nos o valor da compra [Kz]: "))
print("------------**------------")
option=(int(input("Informe-nos também o metódo de pagamento: "
      "\n[1]--> Á Vista dinheiro/cheque"
      "\n[2]--> À vista no cartão"
      "\n[3]--> Em até 2x no cartão"
      "\n[4]--> 3x ou mais no cartáo"
                  "\nR : ")))
if option > 4:
    print("\033[1;31mOpção invalida!\033[m")
if option >= 1 and option <=4:
    print("{:~^35}".format(">RECIBO<"))
if option==1:
    desc = price-price*0.10
    print(f"Receberás 10% d'juros ficando {desc:.2f}kz")
elif option==2:
    desc= price-price*0.05
    print(f"Receberás 5% d'juros ficando {desc:.2f}kz")
elif option==3:
    print("Preço Normal do produto!")
elif option==4:
    desc= price+price*0.20
    total=int(input("Informe o total do produto: "))
    parcela= desc/total
    print(f"Receberás cerca de {parcela}kz em parcelas +20% d'juros ficando {desc:.2f}kz")

