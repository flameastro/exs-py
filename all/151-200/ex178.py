# ex178: Crie uma função que recebe qualquer valor como parâmetro e retorne o tupo de dado deste valor
def tipo_de_dado(valor):
    return f"Este valor tem o tipo de dado {type(valor).__name__}"


if __name__ == "__main__":
    print(tipo_de_dado("Guido criou o que chamamos de python!"))  # Este valor tem o tipo de dado str
    print(tipo_de_dado(2 < 4))  # Este valor tem o tipo de dado bool
    print(tipo_de_dado(12 + 5))  # Este valor tem o tipo de dado int
    print(tipo_de_dado([1, 2, 3, 4, 5]))  # Este valor tem o tipo de dado list
