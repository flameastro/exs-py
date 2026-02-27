# ex311: Elaborar um programa que leia seis elementos (valores inteiros) para as matrizes A e B de uma dimensão do tipo vetor. Construir as matrizes C e D de mesmo tipo e dimensão. A matriz C deve ser formada pelos elementos de índice ímpar das matrizes A e B e a matriz D deve ser formada pelos elementos de índice par das matrizes A e B. Apresentar os elementos das matrizes C e D.
matrizA = []
matrizB = []
matrizC = []
matrizD = []

for x in range(6):
    valor = int(input(f"Digite o valor {x+1} da matriz A: "))
    matrizA.append(valor)

for x in range(6):
    valor = int(input(f"Digite o valor {x+1} da matriz B: "))
    matrizB.append(valor)


for x in range(6):
    if x % 2 != 0:
        matrizC.append(matrizA[x])
        matrizC.append(matrizB[x])
    else:
        matrizD.append(matrizA[x])
        matrizD.append(matrizB[x])

print(f"Matriz C: {matrizC}")
print(f"Matriz D: {matrizD}")
