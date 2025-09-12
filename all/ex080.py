# ex080: Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários. No final, mostre o total de salários pagos aos homens e o total pago às mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não sempre que ler os dados de um funcionário.

salarios_homens = []
salarios_mulheres = []
while True:
    salario = float(input('Digite o salário: '))
    sexo = input('Digite o sexo [M/F]: ').strip().upper()

    while sexo not in ['M', 'F']:
        sexo = input('Digite corretamente [M/F]: ').strip().upper()

    if sexo == 'M':
        salarios_homens.append(salario)
    elif sexo == 'F':
        salarios_mulheres.append(salario)

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Digite corretamente [S/N]: ').strip().upper()
    if continuar == 'N':
        break 
    elif continuar == 'S':
        continue

homens = sum(salarios_homens)
mulheres = sum(salarios_mulheres)

print(f'O salário total dos homens é {homens}')
print(f'Já o salário total das mulheres é {mulheres}')
