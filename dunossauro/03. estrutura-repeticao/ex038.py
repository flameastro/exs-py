# ex038: Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
# v1
from datetime import date

salario = 1000
aumento = 0.015  # 1,5%
ano_inicial = 1995
ano_atual = date.today().year

for ano in range(1996, ano_atual + 1):
    salario += salario * aumento
    aumento *= 2

print(f"Salário atual em {ano_atual}: R$ {salario:.2f}")


# v2
from datetime import date

salario = float(input("Digite o salário inicial do funcionário: R$ "))
aumento = 0.015
ano_inicial = 1995
ano_atual = date.today().year

for ano in range(1996, ano_atual + 1):
    salario += salario * aumento
    aumento *= 2

print(f"Salário atual em {ano_atual}: R$ {salario:.2f}")
