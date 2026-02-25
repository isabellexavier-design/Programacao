#Ler quantidade de cada moeda e imprimir o valor total economizado, existem moedas de 1,5,10,25 e 50 centavos, e de 1 real.

c1= int(input("Insira a quantidade de moedas de 1 centavo: "))
c5= int(input("Insira a quantidade de moedas de 5 centavos: "))
c10= int(input("Insira a quantidade de moedas de 10 centavos: "))
c25= int(input("Insira a quantidade de moedas de 25 centavos: "))
c50= int(input("Insira a quantidade de moedas de 50 centavos: "))
r1= int(input("Insira a quantidade de moedas de 1 real: "))

c1 * 0.01
c5 * 0.05
c10 * 0.10
c25 * 0.25
c50 * 0.50
r1* 1

valor = c1 * 0.01 + c5 * 0.05 + c10 * 0.10 + c25 * 0.25 + c50 * 0.50 + r1 * 1
print ("O valor total é: " ,valor)
