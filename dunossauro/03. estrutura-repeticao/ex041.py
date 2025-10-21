# ex041: Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

# Os juros e a quantidade de parcelas seguem a tabela abaixo:

# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25
# Exemplo de saída do programa:

# Valor da Dívida   Valor dos Juros     Quantidade de Parcelas      Valor da Parcela
# R$ 1.000,00       0                   1                           R$  1.000,00
# R$ 1.100,00       100                 3                           R$    366,00
# R$ 1.150,00       150                 6                           R$    191,67
divida = float(input("Valor da dívida: R$ "))

parcelas_juros = [
    (1, 0),
    (3, 10),
    (6, 15),
    (9, 20),
    (12, 25)
]

print("\nValor da Dívida\tValor dos Juros\tQuantidade de Parcelas\tValor da Parcela")

for qtd_parcelas, juros in parcelas_juros:
    valor_juros = divida * (juros / 100)
    valor_total = divida + valor_juros
    valor_parcela = valor_total / qtd_parcelas

    print(f"R$ {valor_total:10.2f}\tR$ {valor_juros:10.2f}\t{qtd_parcelas:>10}\t\tR$ {valor_parcela:10.2f}")
