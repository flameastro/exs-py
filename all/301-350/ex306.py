# ex306: Elaborar um programa que leia uma matriz A do tipo vetor com dez elementos inteiros positivos. Construir uma matriz B de mesmos tipo e dimensão, em que cada elemento da matriz B deve ser o valor negativo do elemento correspondente da matriz A. Desta forma, se em A[1] estiver armazenado o elemento 8, deve estar em B[1] o valor –8 e assim por diante. Apresentar os elementos da matriz B.
matrizA = []
matrizB = []

for x in range(10):
    numero = int(input("Digite um número inteiro e positivo: "))
    matrizA.append(numero)

for x in range(10):
    matrizB.append(matrizA[x] * -1)

print(matrizB)
