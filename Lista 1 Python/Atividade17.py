#Ler uma temperatura Celsius e imprimi-Ia em Fahrenheit 
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(f"{celsius}°C é equivalente a {fahrenheit:.2f}°F.")