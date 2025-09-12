# ex041: Uma empresa precisa reajustar o salário dos seus funcionários, dando um aumento de acordo com alguns fatores. Faça um programa que leia o salário atual, o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa. No final, mostre o seu novo salário, baseado na tabela a seguir:
# - Mulheres
# - menos de 15 anos de empresa: +5%
# - de 15 até 20 anos de empresa: +12%
# - mais de 20 anos de empresa: +23%
# - Homens
# - menos de 20 anos de empresa: +3%
# - de 20 até 30 anos de empresa: +13%
# - mais de 30 anos de empresa: +25%

salario = float(input('Digite o salário: '))
genero = input('Digite o gênero [M/F]: ').strip().upper()

while genero not in ['M', 'F']:
    genero = input('Digite corretamente [M/F]: ').strip().upper()

anos = int(input('Quantos anos trabalha na empresa? '))

if genero == 'F':
    if anos < 15:
        aumento = salario * 0.05
    elif anos >= 15 and anos < 20:
        aumento = salario * 0.12
    elif anos >= 20:
        aumento = salario * 0.23
elif genero == 'M':
    if anos < 20:
        aumento = salario * 0.03
    elif anos >= 20 and anos < 30:
        aumento = salario * 0.13
    elif anos >= 30:
        aumento = salario * 0.25
salario += aumento

print(f'Seu novo salário reajustado é de R${salario} reais')
