# ex085: Crie um programa usando a estrutura “faça enquanto” que leia vários números. A cada laço, pergunte se o usuário quer continuar ou não. No final, mostre na tela:
# a) O somatório entre todos os valores
# b) Qual foi o menor valor digitado
# c) A média entre todos os valores
# d) Quantos valores são pares

numeros = []
pares = 0
while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)

    pares += 1

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue

media = sum(numeros) / len(numeros)
menor = numeros.index(min(numeros))

print(f'A soma de todos os valores é de {sum(numeros)}')
print(f'O menor número digitado foi {numeros[menor]}, e aparece na {numeros.index(numeros[menor])+1}ª posição')
print(f'A média dos números é de {round(media, 2)}')
print(f'Há {pares} números {"par" if pares == 1 else "pares"}')
