# ex001: Faça um programa que leia um vetor de 5 números inteiros e mostre-os.
vetor = []
for x in range(5):
    vetor.append(int(input("Insira um número: ")))

print(vetor)


# ex002: Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
vetor = []
for x in range(10):
    vetor.append(int(input("Insira um número: ")))

print(list(reversed(vetor)))


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


# ex005: Faça um programa que leia 10 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
par = []
impar = []
numeros = []

for i in range(10):
    numero = int(input("Insira um número: "))

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

    numeros.append(numero)


print(f"Números inseridos: {numeros}")
print(f"Números PARES: {par}")
print(f"Números ÍMPARES: {impar}")
