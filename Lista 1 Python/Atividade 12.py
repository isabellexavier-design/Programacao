#Ler salário e aumentar em 15%, depois descontar 8% de impostos e imprimir salário inicial, o salário com o aumento e o salário final.

salario = float (input("Insira o salario"))
x = salario * 0.15
aumento = salario + x
imposto = aumento * 0.08
salariofinal = aumento - imposto
print ("O salario sem aumento é: ",salario)
print ("O salário com aumento é: ",aumento)
print ("O salario final é: ",salariofinal)