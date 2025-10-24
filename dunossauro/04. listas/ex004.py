# ex004: Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
consoantes = 0
for i in range(10):
    caractere = input("Digite um caractere: ").upper().strip()
    while not caractere.isalpha() or len(caractere) != 1:
        print("Certifique-se de inserir uma letra válida.")
        caractere = input("Digite um caractere: ").upper().strip()

    if caractere not in ["A", "E", "I", "O", "U"]:
        consoantes += 1

print(f"Foram inseridos ao todo {consoantes} consoantes.")
