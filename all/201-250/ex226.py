# ex226: Elaborar um programa que leia oito elementos inteiros em uma matriz A do tipo vetor. Construir uma matriz 8 de mesma dimensão com os elementos da matriz A multiplicados por 3. O elemento 8[1] deve ser implicado pelo elemento A[1] * 3, o elemento 8[2] implicado pelo elemento A[2] * 3 e assim por diante, até 8. Apresentar a matriz 8.
lista_A = []

for i in range(8):
    lista_A.append(int(input("Digite um número inteiro: ")))

lista_B = lambda lista: [lista[i] * 3 for i in range(8)]
print(lista_B(lista_A))
