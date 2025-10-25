# ex013: Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, ...).
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []
for i in range(12):
    temperatura = float(input(f"Temperatura do mês {meses[i]}: "))
    temperaturas.append(temperatura)

media = sum(temperaturas) / 12
print(f"A média das temperaturas é de {media:.2f}")

i = 0
while i < 12:
    if temperaturas[i] > media:
        print(meses[i])

    i += 1


# ex014: Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
pontos = 0
for x in range(5):
    print(perguntas[x])
    resposta = input("Responda: ").upper().strip()

    while resposta not in ["S", "N"]:
        print("Insira S para SIM e N para NÃO")
        resposta = input("Responda: ").upper().strip()

    if resposta == "S":
        pontos += 1

if pontos == 5:
    classificacao = "Assasino"
elif pontos >= 3:
    classificacao = "Cúmplice"
elif pontos > 1:
    classificacao = "Suspeita"
else:
    classificacao = "Inocente"

print(f"A pessoa possui {pontos} pontos.")
print(f"Classificação: {classificacao}")
