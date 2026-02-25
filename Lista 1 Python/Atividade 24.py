#Calcular quantos litros de água e de suco são necessários para se fazer X litros de refresco (informados pelo usuário).
tonelagua=float (input("Insira a quantidade de água:"))
tonelsuco=float (input("Insira a quantidade de suco:"))
litros= (input("Insira a quantidade de litros de refresco:"))
total= (tonelagua*8) + (tonelsuco*2)
print ("A quantidade de refresco necessária é de: " ,total)