# ex308: Elaborar um programa que leia 10 elementos do tipo real em uma matriz A unidimensional e construir uma matriz B de mesma dimensão com os mesmos elementos armazenados na matriz A, porém de forma invertida. Ou seja, o primeiro elemento da matriz A passa a ser o último da matriz B, o segundo elemento da matriz A passa a ser o penúltimo da matriz B, e assim por diante. Apresentar os elementos das matrizes A e B.
matrizA = []
matrizB = []

for x in range(10):
    numero = int(input("Digite um número inteiro: "))
    matrizA.append(numero)

for x in range(9, -1, -1):
    matrizB.append(matrizA[x])

print(matrizB)
