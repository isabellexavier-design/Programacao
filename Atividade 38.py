#Receber o ano de nascimento de uma pessoa e o ano atual, calcular e mostrar:
#a idade dessa pessoa em anos;
#a idade dessa pessoa em meses;
#a idade dessa pessoa em dias;
#a idade dessa pessoa em semanas.

ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = int(input("Ano atual: "))

anos = ano_atual - ano_nascimento
meses = anos * 12
semanas = anos * 52
dias = anos * 365

print(f"A idade em anos é:" ,anos)
print(f"A idade em meses é:" ,meses)
print(f"A idade em semanas é:" ,semanas)
print(f"A idade em dias é" ,dias)

