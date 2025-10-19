# ex025: Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
print("Responda \"s\" para SIM e \"n\" para NÃO...")
pontos = 0

telefonou = input("Telefonou para a vítima? ").lower()
while telefonou not in ["s", "n"]:
    print("Por favor, digite \"s\" para SIM e \"n\" para NÃO.")
    telefonou = input("Telefonou para a vítima? ").lower()

if telefonou == "s":
    pontos += 1


local = input("Esteve no local do crime? ").lower()
while local not in ["s", "n"]:
    print("Por favor, digite \"s\" para SIM e \"n\" para NÃO.")
    local = input("Esteve no local do crime? ").lower()

if local == "s":
    pontos += 1


mora_perto = input("Mora perto da vítima? ").lower()
while mora_perto not in ["s", "n"]:
    print("Por favor, digite \"s\" para SIM e \"n\" para NÃO.")
    mora_perto = input("Mora perto da vítima? ").lower()

if mora_perto == "s":
    pontos += 1


devia = input("Devia para a vítima? ").lower()
while devia not in ["s", "n"]:
    print("Por favor, digite \"s\" para SIM e \"n\" para NÃO.")
    devia = input("Devia para a vítima? ").lower()

if devia == "s":
    pontos += 1


trabahou = input("Já trabalhou com a vítima? ").lower()
while trabahou not in ["s", "n"]:
    print("Por favor, digite \"s\" para SIM e \"n\" para NÃO.")
    trabahou = input("Já trabalhou com a vítima? ").lower()

if trabahou == "s":
    pontos += 1


if pontos == 5:
    classificacao = "Assasino"
elif pontos >= 3:
    classificacao = "Cúmplice"
elif pontos == 2:
    classificacao = "Suspeito"
elif pontos <= 1:
    classificacao = "Inocente"

print(f"A classificação do participante foi: {classificacao}")
