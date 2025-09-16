# ex083: Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas. O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
# a) O nome da pessoa mais velha
# b) O nome da mulher mais jovem
# c) A média de idade do grupo
# d) Quantos homens tem mais de 30 anos
# e) Quantas mulheres tem menos de 18 anos

nomes = []
idades = []
homens30 = mulheres18 = 0
while True:
    nome = input('Digite o nome: ').strip().title()
    idade = int(input('Digite a idade: '))

    sexo = input('Digite o sexo [M/F]: ').strip().upper()
    while sexo not in ['M', 'F']:
        sexo = input('Digite corretamente [M/F]: ').strip().upper()

    if sexo == 'M':
        if idade > 30:
            homens30 += 1
    elif sexo == 'F':
        if idade < 18:
            mulheres18 += 1
    nomes.append(nome)
    idades.append(idade)

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue

velho = idades.index(max(idades))
jovem = idades.index(min(idades))
media = sum(idades) / len(idades)
print(f'O nome da pessoa mais velha é {nomes[velho]}, e tem {idades[velho]} anos')
print(f'A pessoa mais jovem é {nomes[jovem]}, e tem {idades[jovem]} anos')
print(f'A média das idades é de {media}')
print(f'Há {homens30} {"homem" if homens30 == 1 else "homens"} com mais de 30 anos')
print(f'Há {mulheres18} {"mulher" if mulheres18 == 1 else "mulheres"} com menos de 18 anos')
