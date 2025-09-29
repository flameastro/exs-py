# ex255: Crie uma função que receba um texto como parâmetro e retorne o texto embaralhado, sem nenhuma ordem.
from random import randint

def embaralha_texto(texto):
    letra = ""
    lista = []
    tamanho = len(texto)
    numero = randint(0, tamanho-1)

    while len(lista) != tamanho:
        while numero in lista:
            numero = randint(0, tamanho-1)

        letra += texto[numero]
        lista.append(numero)

    return letra


if __name__ == "__main__":
    print(embaralha_texto("Flame"))  # maleF;  Fmael
    print(embaralha_texto("Ghost Fly"))  #  loGthysF;  Gtshy oFl
    print(embaralha_texto("Astronomia"))  # nsAmairoto;  onstoiramA
