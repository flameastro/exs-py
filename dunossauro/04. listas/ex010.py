# ex010: Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
lista1 = []
lista2 = []

for i in range(5):
    valor = input("Insira qualquer valor (vetor 1): ")
    lista1.append(valor)

for i in range(5):
    valor = input("Insira qualquer valor (vetor 2): ")
    lista2.append(valor)

lista = []
for i in range(5):
    lista.append(lista1[i])
    lista.append(lista2[i])

print(lista)
