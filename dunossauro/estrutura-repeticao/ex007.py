# ex007: Faça um programa que leia 5 números e informe o maior número.
numeros = []

for i in range(5):
    numero = int(input(f"Insira o {i+1}o número inteiro: "))
    numeros.append(numero)

print(f"O maior número inserido foi {sorted(numeros)[-1]}")
