# ex015: Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.
ganho_hora = float(input("Insira a quantidade de reais que você ganha por hora: "))
horas_mes = int(input("Digite a quantidade de horas trabalhadas num mês: "))

salario_bruto = ganho_hora * horas_mes
IMPOSTO_RENDA = (salario_bruto * 11) / 100
INSS = (salario_bruto * 8) / 100
SINDICATO = (salario_bruto * 5) / 100

salario_liquido = salario_bruto - (IMPOSTO_RENDA + INSS + SINDICATO)

print(" Detalhes do Salário ".center(50, "-"))
print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"Salário líquido: R${salario_liquido:.2f}")
print(f"Imposto de Renda: R${IMPOSTO_RENDA:.2f}")
print(f"INSS: R${INSS:.2f}")
print(f"Sindicato: R${SINDICATO:.2f}")
