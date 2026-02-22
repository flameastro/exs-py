# ex013: Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário ganhou ou perdeu o jogo.
import random

def carregar_palavras(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        palavras = [linha.strip().lower() for linha in arquivo if linha.strip()]
    return palavras

def embaralhar_palavra(palavra):
    letras = list(palavra)
    random.shuffle(letras)
    return ''.join(letras)

def jogo_palavra_embaralhada():
    palavras = carregar_palavras("palavras.txt")
    palavra = random.choice(palavras)
    embaralhada = embaralhar_palavra(palavra)

    print("=== JOGO DA PALAVRA EMBARALHADA ===")
    print("A palavra é:", embaralhada)
    tentativas = 6

    while tentativas > 0:
        resposta = input("Qual é a palavra? ").lower()
        if resposta == palavra:
            print("\nParabéns! Você acertou a palavra:", palavra.upper())
            break
        else:
            tentativas -= 1
            print(f"Errado! Restam {tentativas} tentativas.")
    else:
        print("\nVocê perdeu! A palavra era:", palavra.upper())

jogo_palavra_embaralhada()
