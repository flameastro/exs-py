# ex024: Faça um programa que calcule e mostre a média aritmética de N notas.
quantidade = 0
soma = 0

while True:
    nota = float(input("Insira uma nota: "))
    while nota not in range(0, 11):
        print("Considere digitar uma nota válida.")
        nota = float(input("Insira uma nota: "))

    soma += nota
    quantidade += 1

    continuar = input("Deseja continuar? [S/N]: ").upper().strip()
    while continuar not in ["S", "N"]:
        print("Por favor, insira S para SIM e N para NÃO")
        continuar = input("Deeseja continuar? [S/N]: ").upper().strip()

    if continuar == "N":
        break

media = soma / quantidade

print(f"A média das notas é de {media:.2f}")
