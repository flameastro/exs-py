# ex078: Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
# a) Quantos homens foram cadastrados
# b) Quantas mulheres foram cadastradas
# c) A média de idade do grupo
# d) A média de idade dos homens
# e) Quantas mulheres tem mais de 20 anos

idades = []
grupo_homens = []
homens = mulheres = mulher_maior20 = 0
for i in range(5):
    idade = int(input(f'Digite a idade da pessoa {i+1}: '))
    sexo = input(f'Digite o sexo da pessoa {i+1} [M/F]: ').strip().upper()

    while sexo not in ['M', 'F']:
        sexo = input(f'O sexo deve ser M ou F: ').strip().upper()

    idades.append(idade)
    
    if sexo == 'M':
        grupo_homens.append(idade)
        homens += 1
    elif sexo == 'F':
        mulheres += 1
        if idade > 20:
            mulher_maior20 += 1

media = sum(idades) / len(idades)
media_homens = sum(grupo_homens) / len(grupo_homens)

print(f'Foram cadastrados {homens} {"homem" if homens == 1 else "homens"}')
print(f'Foram cadastradas {mulheres} {"mulher" if mulheres == 1 else "mulheres"}')
print(f'A média das idades é {media}')
print(f'A média das idades dos homens é {media_homens}')
print(f'Há {mulher_maior20} {"mulher" if mulher_maior20 == 1 else "mulheres"} com mais de 20 anos')
