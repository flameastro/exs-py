# ex170: Crie uma função que recebe uma string com uma ou mais palavras como parâmetro e retorne a mesma string, mas caso a palavra tiver 5 ou mais caracteres, retorne a palavra ao contrário. Por exemplo: VSCode é um belo editor -> edoCSV é um belo rotide.
def inverte_parcialmente(string: str):
    resultado = []

    for palavra in string.split():
        if len(palavra) >= 5:
            resultado.append(palavra[::-1])
        else:
            resultado.append(palavra)

    return " ".join(resultado)


if __name__ == "__main__":
    print(inverte_parcialmente("VSCode é um belo editor"))  # edoCSV é um belo rotide
    print(inverte_parcialmente("A mente é um lugar curioso."))  # A etnem é um ragul .osoiruc
    print(inverte_parcialmente("Você voltaria para o passado ou avançaria para o futuro?"))  # Você airatlov para o odassap ou airaçnava para o ?orutuf
