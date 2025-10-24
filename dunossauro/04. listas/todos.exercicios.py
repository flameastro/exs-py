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


# ex006: Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
medias = []

for aluno in range(10):
    notas = []

    for n in range(4):
        nota = float(input(f"Digite a nota do aluno {aluno+1}: "))
        while nota < 0 or nota > 10:
            print("Por favor, considere inserir uma nota válida.")
            nota = float(input(f"Digite a nota do aluno {aluno+1}: "))

        notas.append(nota)

    media = sum(notas) / 4
    medias.append(str(media))

aprovados = len([x for x in medias if float(x) >= 7])
print(f"O número de alunos com média superior a 7 é {aprovados}.")


# ex007: Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
numeros = []
multiplicacao = 1
soma = 0
for x in range(5):
    numero = int(input("Digite um numero inteiro: "))

    numeros.append(str(numero))

    multiplicacao *= numero
    soma += numero


print(f"A soma dos números informados é de {soma}")
print(f"A multiplicação entre os números resulta em {multiplicacao}")
print(f"Os números informados são {", ".join(numeros)}")


# ex008: Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
idades = []
alturas = []

for x in range(5):
    idade = int(input("Idade: "))
    while idade not in range(0, 121):
        print("Por favor, insira um valor adequado.")
        idade = int(input("Idade: "))

    altura = float(input("Altura: "))
    while altura < 0 or altura > 3:
        print("Por favor, digite um valor para a altura que seja válido.")
        altura = float(input("Altura: "))

    idades.append(idade)
    alturas.append(altura)


print(idades[::-1])
print(alturas[::-1])


# ex009: Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
lista = []
for i in range(10):
    numero = int(input("Insira um número inteiro: "))
    lista.append(str(numero ** 2))

print(f"Lista com o cálculo dos quadrados dos elementos: {", ".join(lista)}")


# ex010: Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
lista1 = []
lista2 = []

for i in range(5):
    valor = input("Insira qualquer valor (vetor 1): ")
    lista1.append(valor)

for i in range(5):
    valor = input("Insira qualquer valor (vetor 2): ")
    lista2.append(valor)

lista = []
for i in range(5):
    lista.append(lista1[i])
    lista.append(lista2[i])

print(lista)
