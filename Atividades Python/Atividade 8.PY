#Inserir a altura de uma pessoa
#Inserir o sexo (M ou F)
#Para homens: (72.7*h) - 58 e para mulheres: (62.1*h) - 44.7
altura = float (input("Insira a sua altura:"))
sexo = (input("Insira o sexo (M ou F):"))
if sexo == "M":
    peso_ideal = (72.7*altura) - 58
    print ("Para homens o peso ideal é: ,peso_ideal")
elif sexo == "F": 
    peso_ideal = (62.1*altura) - 44.7
    print ("Para mulheres o peso ideal é: ,peso_ideal")
else:
    print ("Sexo inválido.Insira F ou M")
    





