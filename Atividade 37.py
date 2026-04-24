#Calcular e mostrar a tabuada de um número digitado pelo usuário.

numero = int(input("Tabuada: "))
i = 1
while i <= 10:
    print(f"{numero} x {i} = {numero * i}")
    i += 1