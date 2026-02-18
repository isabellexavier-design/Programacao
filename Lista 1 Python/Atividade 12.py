#Ler salário e aumentar em 15%, depois descontar 8% de impostos e imprimir salário inicial, o salário com o aumento e o salário final.

salario = float (input("Insira o salario"))
aumento = salario * 0.15
salario_aumento = salario + aumento
imposto = salario_aumento * 0.08
salario_final = salario_aumento - imposto
print ("O salario inicial é: ",salario)
print ("O salário aumentado é: ",salario_aumento)
print ("O salario descontado é: ",salario_final)