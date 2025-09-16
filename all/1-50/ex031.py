# ex031: Faça um programa que leia 7 números inteiros e no final mostre o somatório entre eles.
soma = 0
for i in range(7):
    numero = int(input(f'Digite o número {i+1}: '))
    soma += numero

print(f'A soma dos números digitados foi {soma}')
