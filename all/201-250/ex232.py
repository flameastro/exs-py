# ex232: Leia dois nomes de pessoas e os imprima em ordem alfabética.
nome1 = input("Digite o nome da primeira pessoa: ")
nome2 = input("Digite o nome da segunda pessoa: ")

print(", ".join(sorted([nome1, nome2])))
