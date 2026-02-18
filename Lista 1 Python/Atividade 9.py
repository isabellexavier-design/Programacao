#Fornecer quantidade de camisetas pequenas, médias e grandes da venda e informar quanto será o valor

camisap = float (input("Insira a quantidade de camisa p vendidas"))
camisam = float (input("Insira a quantidade de camisa m vendidas"))
camisag = float (input("Insira a quantidade de camisa g vendidas"))

total = camisap + camisam + camisag
total = (camisap *10) + (camisam*12) + (camisag*15)
print("O valor arrecadado com a venda das camisetas é: " ,total)

