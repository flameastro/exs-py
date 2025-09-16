# ex109: Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e mostre na tela:
# a) Quais foram os números sorteados
# b) Quantos números estão acima de 5
# c) Quantos números são divisíveis por 3
from random import randint

numeros = []
acima5 = div3 = 0

for i in range(20):
    numero = randint(0, 10)
    numeros.append(numero)

    if numero > 5:
        acima5 += 1

    if numero % 3 == 0:
        div3 += 1

print(f'Os números sorteados foram {numeros}')
print(f'São {acima5} números sorteados acima de 5')
print(f'São {div3} números sorteados que são divisíveis por 3')
