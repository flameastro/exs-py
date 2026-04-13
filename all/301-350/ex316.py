# ex316: Pedro tem 1,50 m e cresce 2 cm por ano, enquanto Lucas tem 1,10 m e cresce 3 cm por ano. Construa um algoritmo que calcule e imprima quantos anos serão necessários para que:
# a) Lucas e Pedro tenham o mesmo tamanho.
# b) Lucas seja maior que Pedro.
pedro = 150
lucas = 110
anos = 0

while lucas < pedro:
    # Aumentando a altura de pedro e lucas
    pedro += 2
    lucas += 3

    # Incrementando o ano para cada repetição
    anos += 1


print(f"a) Levaria {anos} anos para que Lucas e Pedro tivessem o mesmo tamanho")
print(f"b) Levaria {anos + 1} anos para que Lucas tivesse uma altura maior que Pedro")  # Adiciona-se +1 à variável anos porque pedro e lucas teriam 2.30m em 40 anos, e para Lucas ultrapassar Pedro, Lucas deveria ter 2.33m e Pedro 2.32m, resultando em +1 ano.
