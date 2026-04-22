#Calcular quantos litros de água e de suco são necessários para se fazer X litros de refresco (informados pelo usuário).
total_partes = 10
refrescos = float (input("litros de refrescos desejados: "))
agua = (refrescos*8) / total_partes
suco = (refrescos*2) / total_partes
print(f"agua:{agua}L | suco:{suco}L")