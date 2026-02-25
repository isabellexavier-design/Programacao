#Ler um número inteiro até três dígitos e imprimir a saída: CENTENA = x DEZENA = x  e UNIDADE = x

numero =(input("Insira um numero inteiro de no máximo 3 dígitos"))
print (f'centena:{numero[:1]}')
print (f'dezena:{numero[1:2]}')
print (f'unidade:{numero[2:]}')



