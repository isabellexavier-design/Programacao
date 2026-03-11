#Imprimir salário bruto e salário líquido. Considere que o salário líquido é igual ao salário bruto descontando-se 10% de impostos.

h =float(input("Insira a quantidade de horas normais: "))
he = float(input("Insira a quantidade de horas extras trabalhadas: "))

salario_bruto= (h * 10) + (he * 15)

salario_líquido = salario_bruto - (salario_bruto * 0.10)

print ("Seu salário bruto é: ",salario_bruto)
print ("Seu salário líquido é: ",salario_líquido)
