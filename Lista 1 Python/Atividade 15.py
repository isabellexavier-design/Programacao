# Ler o valor total da conta e imprimir quanto cada um deve pagar, mas Carlos e André não podem pagar centavos.]

total = float (input("Insira o valor total da conta: "))
valor_por_pessoa = total / 3

#valor_por_pessoa vai virar um inteiro e remover virgula ( ex: 10,58-> 10)
carlos = int(valor_por_pessoa)
andre = int(valor_por_pessoa)

felipe = total - (carlos + andre)
print("Carlos deve pagar R$ {:.2F}" . format (carlos))
print("André deve pagar R$ {:.2F}" .format (andre))
print("Felipe deve pagar R$ {:.2F}" .format (felipe))






