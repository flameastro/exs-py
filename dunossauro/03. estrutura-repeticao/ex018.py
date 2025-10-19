# ex018: Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
conjunto = []
while True:
    numero = int(input("Digite um número ou -1 para sair: "))

    if numero == -1:
        break

    conjunto.append(numero)

conjunto = sorted(conjunto)

maior = conjunto[-1]
menor = conjunto[0]

soma = 0
for numero in conjunto:
    soma += numero

print(f"O maior número do conjunto é: {maior}.")
print(f"O menor número do conjunto é: {menor}.")
print(f"A soma dos números do conjunto é: {soma}.")
