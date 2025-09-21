# ex239: Mês do Ano: Peça um número de 1 a 12 e imprima o mês do ano correspondente.
MESES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

mes = int(input("Digite um mês do ano no formato numérico [1-12]: "))
while mes not in range(1, 13):
    mes = int(input("Por favor, digite um número entre 1 a 12.\nDigite um mês do ano no formato numérico [1-12]: "))

print(f"Mês selecionado: {MESES[mes-1]}")
