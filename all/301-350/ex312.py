# ex312: Construir um programa que leia uma matriz A de uma dimensão do tipo vetor com 20 elementos do tipo inteiro. Ao final do programa, apresentar a quantidade de valores pares e ímpares existentes na referida matriz.
matrizA = []
pares = 0
impares = 0

for x in range(20):
    valor = int(input("Digite um valor inteiro qualquer: "))
    matrizA.append(valor)

for l in matrizA:
    if l % 2 == 0:
        pares += 1
    else:
        impares += 1


print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
