# ex043: Crie um programa que leia 6 números inteiros e no final mostre quantos deles são pares e quantos são ímpares.
pares = 0
impares = 0

for i in range(6):
    numero = int(input(f'Digite o número {i+1}: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Foram {pares} pares digitados e {impares} ímpares digitados.')
