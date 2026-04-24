#receber valor salário mínimo e valor salário de um funcionário, calcular e mostrar quantidade de salários mínimos que ganha o funcionário.

salario_minimo = float(input("Valor do salário mínimo: R$ "))
salario_func = float(input("Salário do funcionário: R$ "))

quantidade = salario_func / salario_minimo

print(f"O funcionário ganha o equivalente a {quantidade:.2f} salários mínimos.")
