# ex001: Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

# Compara duas strings
# String 1: Brasil Hexa 2006
# String 2: Brasil! Hexa 2006!
# Tamanho de "Brasil Hexa 2006": 16 caracteres
# Tamanho de "Brasil! Hexa 2006!": 18 caracteres
# As duas strings são de tamanhos diferentes.
# As duas strings possuem conteúdo diferente.
string1 = input("String 1: ")
string2 = input("String 2: ")

print("Compara duas strings")
print(f"String 1: {string1}")
print(f"String 2: {string2}")
print(f"Tamanho da String 1: {len(string1)}")
print(f"Tamanho da String 2: {len(string2)}")
if len(string1) == len(string2):
    print("As duas string são de tamanhos iguais.")
else:
    print("As duas string são de tamanhos diferentes.")
    print("As duas string possuem conteúdo diferente.")

if string1 == string2:
    print("As duas strings possuem conteúdo igual.")


# ex002: Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
nome = input("NOME: ").upper()

print(nome[::-1])


# ex003: Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.
# F
# U
# L
# A
# N
# O
nome = input("NOME: ")
for letra in nome:
    print(letra)


# ex004: Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.
# F
# FU
# FUL
# FULA
# FULAN
# FULANO
nome = input("NOME: ")
for x in range(1, len(nome)+1):
    print(nome[:x])


# ex005: Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.
# FULANO
# FULAN
# FULA
# FUL
# FU
# F
nome = input("NOME: ")
for x in range(0, len(nome)):
    print(nome[x:])


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


# ex007: Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.
string = input("STRING: ").lower()
VOGAIS = ["a", "e", "i", "o", "u"]

numero_vogais = 0
for vogal in VOGAIS:
    numero_vogais += string.count(vogal)

print(f"Aparecem {sum([string.count(x) for x in VOGAIS])} vogais na string.")
print(f"A string possui {string.count(" ")} espaços em branco.")


#ex008: Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
palavra = input("Palavra: ").replace(" ", "")

if palavra == palavra[::-1]:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
