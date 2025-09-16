# ex071: Crie uma função que recebe um número e faz uma contagem regressiva desse número
def contagem_regressiva(contagem: int):
    for numero in range(contagem, 0, -1):
        print(numero)


if __name__ == "__main__":
    contagem_regressiva(15)
    contagem_regressiva(5)
    contagem_regressiva(23)
