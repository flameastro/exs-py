# ex008: Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
ganho_hora = float(input("Quantos reais você ganha por hora? "))
horas_mes = int(input("Quantas horas você trabalha por mês? "))

salario = ganho_hora * horas_mes
print(f"Seu salário é de aproximadamente R${salario}.")
