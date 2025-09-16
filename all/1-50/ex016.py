# ex016: Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada.
dias = int(input('Quantos dias em um mês você trabalha? '))
horas = 8
lucro_hora = 25

salario = (lucro_hora * horas) * dias

print(f'O salário do funcionário é de {salario}')
