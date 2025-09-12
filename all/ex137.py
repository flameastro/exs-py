# ex137: Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.
vendedor = input("Digite o nome do vendedor:\n>>> ")
salario = float(input(f"Digite o salário fixo de {vendedor}:\n>>> "))
vendas = float(input(f"Qual foi o total de venda que {vendedor} fez?\n>>> "))

total = (vendas * 0.15) + salario

print(f"TOTAL = R$ {total:.2f}")
