# ex292: Leia uma matriz 3 x 3 de inteiros. Ao fim, exiba a matriz em formato tabular e também o elemento do centro. Ex.:
# 1   2   3
# 4   5   6
# 7   8   9
# Elemento do centro: 5
matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        numero = int(input(f"Digite o número [{i}][{j}]: "))
        linha.append(numero)
    matriz.append(linha)


for linha in matriz:
    print(linha)

print(f"Elemento do centro: {matriz[1][1]}")
