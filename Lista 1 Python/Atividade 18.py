#Imprimir salário bruto e salário líquido. Considere que o salário líquido é igual ao salário bruto descontando-se 10% de impostos.

h = int(input("Insira a quantidade de horas trabalhadas: "))
he = int(input("Insira a quantidade de horas extras trabalhadas: "))
salario2 = h*10 + he*15

desconto = salario2*0.10
salariol = salario2 - desconto

print (f"Seu salário bruto é: ",salario2,"e seu salário líquido é: ",salariol)