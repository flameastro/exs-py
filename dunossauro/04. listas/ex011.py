# ex011: Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
lista1 = []
lista2 = []
lista3 = []

for _ in range(5):
    valor = input("Insira qualquer valor (vetor 1): ")
    lista1.append(valor)

for _ in range(5):
    valor = input("Insira qualquer valor (vetor 2): ")
    lista2.append(valor)

for _ in range(5):
    valor = input("Insira qualquer valor (vetor 2): ")
    lista3.append(valor)

lista = []
for i in range(5):
    lista.append(lista1[i])
    lista.append(lista2[i])
    lista.append(lista3[i])

print(lista)
