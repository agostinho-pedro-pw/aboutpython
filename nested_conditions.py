


##Estudo das Condições aninhadas

nome= str(input("Qual o seu nome? "))
##Introdução das estruturas de condição aninhas com o *elif*
if nome.lower() == "agostinho":
    print("Que nome bonito você tem!")
elif nome == "Pedro" or nome=="Antonio" or nome =="Maria" or nome=="Joana":
    print("O seu nome é bem popular aqui em \033[1;31mAngola\033[m")
elif nome in "Claudia Ana Meury Dina":
    print("Que belo nome femenino")
else:
    print("Aí como o teu nome é normal!")
print(f"Tenha um bom dia \033[1;35m{nome.capitalize()}\033[m!")
