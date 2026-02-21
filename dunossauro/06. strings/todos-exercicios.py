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


# ex009: Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através dos caracteres de formatação.
CPF = input("Insira um CPF no formato xxx.xxx.xxx-xx: ")

if CPF.count("-") != 1 or len(CPF) != 14:
    print("❌ CPF Inválido.")
else:
    CPF = CPF.split(".")
    CPF = CPF + CPF[2].split("-")
    del CPF[2]

    inicio = CPF[0]
    primeiro_meio = CPF[1]
    segundo_meio = CPF[2]
    fim = CPF[3]

    if len(inicio) == 3 and len(primeiro_meio) == 3 and len(segundo_meio) == 3 and len(fim) == 2:
        print("✅ CPF válido.")
    else:
        print("❌ CPF Inválido.")


# ex010: Número por extenso. Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela por extenso.
def numero_por_extenso(numero):
    unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dez_a_dezenove = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

    if numero < 10:
        return unidades[numero]
    elif numero < 20:
        return dez_a_dezenove[numero - 10]
    else:
        dezena = numero // 10
        unidade = numero % 10

        if unidade == 0:
            return dezenas[dezena]
        else:
            return f"{dezenas[dezena]} e {unidades[unidade]}"


numero = int(input("Digite um número entre 0 e 99: "))

if 0 <= numero <= 99:
    print(f"{numero} por extenso é: {numero_por_extenso(numero)}")
else:
    print("Número fora do intervalo permitido (0 a 99).")


# ex011: Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

# Digite uma letra: A
# -> Você errou pela 1ª vez. Tente de novo!

# Digite uma letra: O
# A palavra é: _ _ _ _ O

# Digite uma letra: E
# A palavra é: _ E _ _ O

# Digite uma letra: S
# -> Você errou pela 2ª vez. Tente de novo!
import random

def carregar_palavras(nome_arquivo):
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            palavras = [linha.strip().lower() for linha in arquivo if linha.strip()]
        return palavras
    except FileNotFoundError:
        return "Não foi possível encontrar o arquivo"
    except:
        return "Um erro inesperado aconteceu. Verifique se o arquivo realmente exite e se possui as devidar palavras"

def escolher_palavra(palavras):
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_acertadas):
    exibicao = ""
    for letra in palavra:
        if letra in letras_acertadas:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    return exibicao.strip()

def jogo_forca():
    palavras = carregar_palavras("palavra.txt")
    palavra = escolher_palavra(palavras)
    letras_acertadas = []
    letras_erradas = []
    tentativas = 6

    print("=== JOGO DA FORCA ===")
    print("A palavra tem", len(palavra), "letras.")
    print("_ " * len(palavra))

    while tentativas > 0:
        letra = input("\nDigite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas UMA letra.")
            continue

        if letra in letras_acertadas or letra in letras_erradas:
            print("Você já tentou essa letra. Escolha outra.")
            continue

        if letra in palavra:
            letras_acertadas.append(letra)
            print("\nA palavra é:", mostrar_palavra(palavra, letras_acertadas))
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print(f"-> Você errou pela {len(letras_erradas)}ª vez. Tente de novo!")
            print(f"Restam {tentativas} tentativas.")

        if all(letra in letras_acertadas for letra in palavra):
            print("\n🎉 Parabéns! Você acertou a palavra:", palavra.upper())
            break
    else:
        print("\n💀 Você foi enforcado! A palavra era:", palavra.upper())

jogo_forca()
