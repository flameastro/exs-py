# ex082: Crie um programa que leia o sexo e a idade de várias pessoas. O programa vai perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre:
# a) qual é a maior idade lida
# b) quantos homens foram cadastrados
# c) qual é a idade da mulher mais jovem
# d) qual é a média de idade entre os homens

idades = []
idades_homens = []
idades_mulheres = []
while True:
    idade = int(input('Digite a idade: '))

    sexo = input('Digite o sexo [M/F]: ').strip().upper()
    while sexo not in ['M', 'F']:
        sexo = input('Digite corretamente [M/F]: ').strip().upper()
    
    idades.append(idade)

    if sexo == 'M':
        idades_homens.append(idade)
    elif sexo == 'F':
        idades_mulheres.append(idade)


    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue


maior = max(idades)
homens = len(idades_homens)
mulher_jovem = min(idades_mulheres)
media = sum(idades_homens) / len(idades_homens)

print(f'A maior idade é {maior}')
print(f'Foram cadastrados {homens} {"homem" if homens == 1 else "homens"}')
print(f'A idade da mulher mais jovem é {mulher_jovem}')
print(f'A média da idade dos homens é de {media}')
