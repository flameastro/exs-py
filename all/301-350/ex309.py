# ex309: Construir um programa que calcule a tabuada de um valor qualquer de 1 até 10 e armazene os resultados em uma matriz A de uma dimensão. Apresentar os elementos da matriz A.
numero = int(input("Digite um valor de 1 a 10: "))
matriz = []

for x in range(1, 11):
    matriz.append(numero * x)

print(matriz)
