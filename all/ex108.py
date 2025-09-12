# ex108: Crie uma função que receba um texto como parâmetro e retorne a quantidade de palavras no texto.
def retorna_quantidade_palavras(texto: str):
    try:
        palavras = texto.split()
        quantidade_palavras = len(palavras)

        return f"A quantidade de palavras é de {quantidade_palavras}"
    except TypeError as type_e:
        return f"A função aceita apenas strings. Erro: {type_e}"


if __name__ == "__main__":
    print(retorna_quantidade_palavras("Python foi criado por Guido van Rossum"))  # A quantidade de palavras é de 7
    print(retorna_quantidade_palavras("Lorem, ipsum dolor sit amet consectetur adipisicing elit. Placeat illo aut eius totam quaerat ad expedita ducimus explicabo, asperiores eaque, doloremque labore fugiat consequuntur, voluptatum nobis veniam quae animi hic!"))  # A quantidade de palavras é de 30
