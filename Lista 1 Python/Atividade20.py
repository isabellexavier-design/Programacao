#Calcular a quantidade de novelos de lã necessários para produzir cada blusa em uma confecção.

blusa = float(input("Digite quantas blusas devem ser confeccionadas: "))
novelo = 125
vblusa = 120
total = blusa * vblusa
quantidade = total / novelo
print("O total de novelos é: ",quantidade)