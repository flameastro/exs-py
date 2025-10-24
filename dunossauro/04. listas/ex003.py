# ex003: Faça um programa que leia 4 notas, mostre as notas e a média na tela.
soma = 0
for n in range(4):
    nota = int(input(f"Digite a {["primeira", "segunda", "terceira", "quarta"][n]} nota: "))
    while nota not in range(0, 11):
        print("Insira uma nota válida.")
        nota = int(input(f"Digite a {["primeira", "segunda", "terceira", "quarta"][n]} nota: "))

    soma += nota

media = soma / 4

print(f"Média: {media:.2f}")
