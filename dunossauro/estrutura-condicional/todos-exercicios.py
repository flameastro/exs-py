# Estrutura Condicional
# ex001: Faça um programa que peça dois números e imprima o maior deles.
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

if n1 > n2:
    print(f"{n1} é maior que {n2}")
elif n2 > n1:
    print(f"{n2} é maior que {n1}")
else:
    print("Ambos são iguais...")


# ex002: Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print("POSITIVO")
elif numero < 0:
    print("NEGATIVO")
else:
    print("NULO (0)")


# ex003: Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino
# M - Masculino
# Sexo Inválido.
letra = input("Digite o seu gênero (M/F): ")

if letra == "M":
    print("Masculino")
elif letra == "F":
    print("Feminino")
else:
    print("Sexo inválido")


# ex004: Faça um programa que verifique se uma letra digitada é vogal ou consoante.
letra = input("Digite uma letra: ").lower()

if len(letra) == 1:
    VOGAIS = ["a", "e", "i", "o", "u"]
    CONSOANTES = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    if letra in VOGAIS:
        print("A letra digitada é uma VOGAL.")
    elif letra in CONSOANTES:
        print("A letra digitada é uma CONSOANTE.")
    else:
        print("Ooops, você não inseriu uma letra do alfabeto, certifique-se de inserir uma das 26 letras do alfabeto.")
else:
    print(f"Por favor, insira uma letra. Você inseriu uma palavra com {len(letra)} caracteres.")


# ex005: Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
nota1 = float(input("Digite a primeira nota: "))
while nota1 not in range(0, 11):
    print("Por favor, certifique-se de inserir uma nota válida.")
    nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))
while nota2 not in range(0, 11):
    print("Por favor, certifique-se de inserir uma nota válida.")
    nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com Distinção")
else:
    print("Oops, algo deu errado! Por favor, tente novamente.")


# ex006: Faça um programa que leia três números e mostre o maior deles.
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))

if n1 > n2 and n1 > n3:
    print(f"O maior número é o primeiro -> {n1}")
elif n2 > n1 and n2 > n3:
    print(f"O maior número é o segundo -> {n2}")
elif n3 > n1 and n3 > n2:
    print(f"O maior número é o terceiro -> {n3}")
else:
    if n1 == n2 and n1 == n3:
        print(f"Todos são iguais -> {n1}")
    elif n1 == n2:
        print(f"Ambos o primeiro e o segundo número são iguais -> {n1}")
    elif n2 == n3:
        print(f"Ambos o segundo e o terceiro número são iguais -> {n2}")
    elif n1 == n3:
        print(f"Ambos o primeiro e o terceiro números sao iguais -> {n1}")


# ex007: Faça um programa que leia três números e mostre o maior e o menor deles:
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))

if n1 < n2 and n1 < n3:
    print(f"O menor número é o primeiro -> {n1}")
elif n2 < n1 and n2 < n3:
    print(f"O menor número é o segundo -> {n2}")
elif n3 < n1 and n3 < n2:
    print(f"O menor número é o terceiro -> {n3}")
else:
    if n1 == n2 and n1 == n3:
        print(f"Todos são iguais -> {n1}")
    elif n1 == n2:
        print(f"Ambos o primeiro e o segundo número são iguais -> {n1}")
    elif n2 == n3:
        print(f"Ambos o segundo e o terceiro número são iguais -> {n2}")
    elif n1 == n3:
        print(f"Ambos o primeiro e o terceiro números sao iguais -> {n1}")


# ex008: Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:
produto1 = float(input("Informe o primeiro produto: "))
produto2 = float(input("Informe o segundo produto: "))
produto3 = float(input("Informe o terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print(f"Você deve comprar o primeiro produto -> {produto1}")
elif produto2 < produto1 and produto2 < produto3:
    print(f"Você deve comprar o segundo produto -> {produto2}")
elif produto3 < produto1 and produto3 < produto2:
    print(f"Você deve comprar o terceiro produto -> {produto3}")
else:
    if produto1 == produto2 and produto1 == produto3:
        print(f"Todos são iguais -> {produto1}")
    elif produto1 == produto2:
        print(f"Ambos o primeiro e o segundo produto são iguais -> {produto1}")
    elif produto2 == produto3:
        print(f"Ambos o segundo e o terceiro produto são iguais -> {produto2}")
    elif produto1 == produto3:
        print(f"Ambos o primeiro e o terceiro produto são iguais -> {produto1}")


# ex009: Faça um programa que leia três números e mostre-os em ordem decrescente
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

print(f"Os números em ordem decrescente são: {", ".join(sorted([str(numero) for numero in [n1, n2, n3]], reverse=True))}")


# ex010: Faça um programa que pergunte em que turno você estuda. Peça para digitar:
# M - Matutino
# V - Vespertino
# N - Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print("Selecione o seu turno correspondente.")
print("Digite M para Matutino")
print("Digite V para Vespertino")
print("Digite N para Noturno")

turno = input("Em que turno você estuda/trabalha? ").upper()

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")
