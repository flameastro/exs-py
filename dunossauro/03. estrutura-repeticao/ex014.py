# ex014: Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
pares = 0
impares = 0
for i in range(10):
    numero = int(input(f"Insira o {i+1}o numero inteiro: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"A quantidade de números pares é de {pares}")
print(f"A quantidade de números impares é de {impares}")
