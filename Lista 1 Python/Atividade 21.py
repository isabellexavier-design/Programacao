#calcular quantos litros de refrigerante o cliente comprou.
lata= int(input("Insira a quantidade de latas compradas: "))
garrafa1= int(input("Insira a quantidade de garrafas 600ml compradas: "))
garrafa2= int(input("Insira a quantidade de garrafas 2l compradas: "))

total= (lata * 350) + (garrafa1 * 600) + (garrafa2 * 2000)
print ("O total de litros de refrigerantes em ML é de: ",total) 
