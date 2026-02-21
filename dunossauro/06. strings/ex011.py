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
