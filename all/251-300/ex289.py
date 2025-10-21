# ex289: Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.
# Data de Nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
nascimento = input("Digite a sua data de nascimento no formato dd/mm/aaaa: ")
nascimento = nascimento.split("/")

print(f"Você nasceu em {nascimento[0]} de {meses[int(nascimento[1])-1]} de {nascimento[2]}.")
