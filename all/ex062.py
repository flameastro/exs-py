# ex062: Crie um programa que leia o nome de várias pessoas e exiba a lista em ordem alfabética.
lista = []

while True:
    nome = input('Digite o nome da pessoa: ').strip().title()
    lista.append(nome)

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Digite corretamente [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue

print(f'A lista com os nomes em ordem alfabética é {sorted(lista)}')
