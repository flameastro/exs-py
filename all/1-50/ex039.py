# ex039: Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.
pares = 0
for i in range(5):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        pares += 1

print(f'Ao total são {pares} números pares')
