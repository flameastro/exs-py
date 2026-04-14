# ex320: Dada uma matriz de 6 linhas e 2 colunas de inteiros, calcular e exibir a média geométrica dos valores de cada uma das linhas. A média geométrica é calculada pela seguinte expressão: SQRT (X1 * X2), que representa a raiz quadrada do resultado da multiplicação dos elementos da coluna 1 (X1) pelos elementos da coluna 2 (X2).
from math import sqrt
matriz = []
X1 = 0
X2 = 0

for i in range(6):
    linha = []
    for j in range(2):
        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
        if j == 0:
            X1 += valor

        if j == 1:
            X2 += valor

        linha.append(valor)
    matriz.append(linha)

media_geometrica = sqrt(X1 * X2)
print(f"Média geométrica: {media_geometrica}")
