#Converter tempo de trabalho sem acidentes pela quantidade de dias em anos, meses e dias

acidentes = int (input("Insira os dias dsem acidentes"))
mes = acidentes/30
ano = acidentes/365
print(f"Está a" ,acidentes, "dias", mes , "meses" , ano, "anos sem acidente")