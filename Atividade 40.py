#Receber o valor dos catetos de um triângulo, calcular e mostrar o valor da hipotenusa.

cateto1 = float(input("Digite o valor do cateto 1: "))
cateto2 = float(input("Digite o valor do cateto 2: "))

# Teorema de Pitágoras: a² + b² = c²
hipotenusa = (cateto1**2 + cateto2**2) ** 0.5

print(f"O valor da hipotenusa é: {hipotenusa:.2f}")