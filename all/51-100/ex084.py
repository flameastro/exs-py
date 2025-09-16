# ex084: Faça um programa usando a estrutura “faça enquanto” que leia a idade de várias pessoas. A cada laço, você deverá perguntar para o usuário se ele quer ou não continuar a digitar dados. No final, quando o usuário decidir parar, mostre na tela:
# a) Quantas idades foram digitadas
# b) Qual é a média entre as idades digitadas
# c) Quantas pessoas tem 21 anos ou mais.

idades = []
idade21 = 0
while True:
    idade = int(input('Digite a idade: '))

    idades.append(idade)

    if idade > 21:
        idade21 += 1

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue

media = sum(idades) / len(idades)
print(f'Há {len(idades)} idades cadastradas')
print(f'A média das idades é de {round(media, 2)}')
print(f'Há {idade21} {"pessoa" if len(idades) == 1 else "pessoas"} com mais de 21 anos.')
