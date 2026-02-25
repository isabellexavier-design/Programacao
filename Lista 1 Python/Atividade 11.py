#Converter tempo de trabalho sem acidentes pela quantidade de dias em anos, meses e dias

dias_trabalhados = int (input("digite o número de dias trabalhados sem acidente: "))

anos = dias_trabalhados // 365
meses= (dias_trabalhados % 365 ) // 30
dias = (dias_trabalhados % 365) %30

print(f"{dias_trabalhados} dias equivalentes a {anos} anos, {meses} meses e {dias} dias")