# ex086: Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura “para”. No final, mostre na tela:
# a) Quantas mulheres foram cadastradas
# b) Quantos homens pesam mais de 100Kg
# c) A média de peso entre as mulheres
# d) O maior peso entre os homens

homem_peso100 = mulheres = 0
peso_homens = []
peso_mulheres = []
for i in range(8):
    sexo = input('Digite o sexo [M/F]: ').strip().upper()
    while sexo not in ['M', 'F']:
        sexo = input('Digite corretamente [M/F]: ').strip().upper()

    peso = float(input('Digite o peso: '))

    if sexo == 'F':
        peso_mulheres.append(peso)
        mulheres += 1
    if sexo == 'M':
        peso_homens.append(peso)
        if peso > 100:
            homem_peso100 += 1


maior = peso_homens.index(max(peso_homens))
media_mulheres = sum(peso_mulheres) / len(peso_mulheres)
print(f'Foram cadastradas {mulheres} {"mulher" if mulheres == 1 else "mulheres"}')
print(f'Há {homem_peso100} {"homem" if homem_peso100 == 1 else "homens"} com mais de 100Kg.')
print(f'A média de pesos entre as mulheres é de {media_mulheres}')
print(f'O maior peso entre os homens foi de {peso_homens[maior]}')
