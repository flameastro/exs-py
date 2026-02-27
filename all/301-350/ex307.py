# ex307: Elaborar um programa que leia 15 elementos inteiros de uma matriz A do tipo vetor. Construir uma matriz B de mesmo tipo, observando a seguinte lei de formação: “todo elemento da matriz B deve ser o quadrado do elemento da matriz A correspondente”. Apresentar os elementos das matrizes A e B.
matrizA = []
matrizB = []

for x in range(15):
    numero = int(input("Digite um número inteiro: "))
    matrizA.append(numero)

for x in range(15):
    matrizB.append(matrizA[x] ** 2)

print(matrizB)
