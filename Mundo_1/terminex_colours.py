##Curso de python
#Cores no Terminal

##print("\033[1;35 mOlá, Mundo!\033[m")
a= 20
b=30
c= 80
d= 10
name="Agostinho"
##print(f"Os valores são \033[1;34m{a}\033[m e \033[1;31m{b}\033[m e \033[1;35m{c}\033[m e \033[1;37m{d}\033[m estudando o ANSI" )
name="Agositinho"
print(f"Olá Mundo \033[1;31m{name}\033[m !!")
print("Olá, Mundo {}{}{} !!".format("\033[1;36m",name,"\033[m"))
print("Olá, Mundo {}{}{} !!".format("\033[1;35m",name,"\033[m"))
print("Olá, Mundo {}{}{} !!".format("\033[1;35;40m",name,"\033[m"))

colours= {"clean":"\033[m",
	"purple":"\033[1;35;40m",
    "blue_":"\033[1:36m",      }
print("   {}{}{}".format(colours["purple"],name,colours["clean"]))