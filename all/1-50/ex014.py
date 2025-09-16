# ex014: Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.
salario = float(input('Digite o seu salário: '))
aumento = salario * 0.15
salario += aumento

print(f'O seu novo salário com 15% de aumento é {salario}')
