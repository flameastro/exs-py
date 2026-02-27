# ex310: Elaborar um programa que leia 15 elementos reais para uma matriz A de uma dimensão do tipo vetor. Construir uma matriz B de mesmos tipo e dimensão, observando a seguinte lei de formação: “todo elemento da matriz A que possuir índice par deve ter seu elemento dividido por 2; caso contrário, o elemento da matriz A deve ser multiplicado por 1.5”. Apresentar os elementos da matriz B.
matrizA = []
matrizB = []

for x in range(15):
    numero = float(input("Digite um número real: "))
    matrizA.append(numero)

for x in range(15):
    if x % 2 == 0:
        matrizB.append(matrizA[x] / 2)
    else:
        matrizB.append(matrizA[x] * 1.5)

print(matrizB)
