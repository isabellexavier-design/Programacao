#Dia e o mês de uma data e informar quantos dias se passaram desde o início do ano

dia = float(input("Insira o dia"))
mes = float(input("Insira o mes"))

dia =(mes-1) *30 +dia
print(f"Se passaram {dia} dias desde o inicio do ano")

