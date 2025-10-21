# ex044: Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

# 1 , 2, 3, 4  - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:

# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
print(" INFORMAÇÕES SOBRE A ELEIÇÃO ".center(50, "-"))
print("1 - João Matheus Araújo")
print("2 - Felipe Gonçalves")
print("3 - Matheus Cândido ")
print("4 - Lucas Rafael dos Santos")
print("5 - Voto Nulo")
print("6 - Voto em Branco")

votos = []

while True:
    codigo = int(input("Digite o código de acordo com o candidato desejado: "))
    if codigo == 0:
        break

    while codigo not in range(1, 7):
        print("Certifique-se de inserir um código válido: ")
        codigo = int(input("Digite o código de acordo com o candidato desejado: "))

    votos.append(codigo)

print(f" RESULTADOS DA ELEIÇÃO ".center(50, "-"))
print(f"Total de votos: {len(votos)}") # EXTRA
print(f"Total de votos para o candidato 1 (João Matheus Araújo): {votos.count(1)}")
print(f"Total de votos para o candidato 2 (Felipe Gonçalves): {votos.count(2)}")
print(f"Total de votos para o candidato 3 (Matheus Cândido): {votos.count(3)}")
print(f"Total de votos para o candidato 4 (Lucas Rafael dos Santos): {votos.count(4)}")
print(f"Total de votos nulos: {votos.count(5)}")
print(f"Total de votos em branco: {votos.count(6)}")
print(f"Porcentagem de votos nulos sobre o total de votos: {((votos.count(5) / len(votos)) * 100):.2f}%")
print(f"Porcentagem de votos em branco sobre o total de votos: {((votos.count(6) / len(votos)) * 100):.2f}%")
