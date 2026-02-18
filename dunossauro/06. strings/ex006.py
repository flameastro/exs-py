# ex006: Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso.

# Data de Nascimento: 29/10/1973
# Você nasceu em  29 de Outubro de 1973.
data = input("Digite a data no formato dd/mm/aaaa: ")
if data.count("/") != 2:
    print("❌ Data inválida.")
else:
    data = data.split("/")
    for elemento in data:
        if not elemento.isnumeric():
            print("❌ Data inválida.")
            exit()

    else:
        if (len(data[0]) != 2 or int(data[0]) < 1 or int(data[0]) > 33) or (len(data[1]) != 2 or int(data[1]) < 1 or int(data[1]) > 12):
            print("❌ Data inválida.")

        else:
            dia = data[0]
            mes = data[1]
            ano = data[2]
            MESES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

            print(f"Você nasceu em {dia} de {MESES[int(mes)-1]} de {ano}.")
