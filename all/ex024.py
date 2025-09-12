# ex024: Desenvolva um programa que leia o nome de um funcionário, seu salário, quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de acordo com a tabela a seguir:
# - Até 3 anos de empresa: aumento de 3%
# - entre 3 e 10 anos: aumento de 12.5%
# - 10 anos ou mais: aumento de 20%
funcionario = input('Digite o nome do funcionário: ')
salario = int(input('Digite o salário do funcionário: '))
anos = int(input('Quantos anos trabalha na empresa? '))


if anos < 3:
    aumento = salario * 0.03
elif anos > 3 and anos < 10:
    aumento = salario * 12.5
elif anos >= 10:
    aumento = salario * 0.20
print(f'O novo salário de {funcionario} agora é de {salario + aumento}')
