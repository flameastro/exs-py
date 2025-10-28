# ex017: Em uma competição de salto em distância, cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m
while True:
    saltos = []
    atleta = input("Atleta: ")
    if atleta == "":
        break

    for x in range(5):
        salto = float(input(f"{["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"][x]} Salto: "))
        while salto < 0 or salto > 50:
            print("Por favor, insira um valor correto.")
            salto = float(input(f"{["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"][x]} Salto: "))

        saltos.append(salto)

    media = sum(saltos) / 5

    print(" RESULTADO FINAL ".center(50, "-"))
    print(f"Atleta: {atleta.title()}")
    print(f"Saltos: {" - ".join(str(x) for x in saltos)}")
    print(f"Média dos saltos: {media:.2f}")
    print("-" * 50)
