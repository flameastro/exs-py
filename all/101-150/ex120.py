# ex120: Crie uma função que receba uma lista de números como parâmetro e retorne a média de números daquela lista.
def retorna_media(lista: int):
    if len(lista) < 2:
        return "A lista deve ter ao menos 2 elementos."

    try:
        soma = sum(lista)
        media = soma / len(lista)

        return f"A média de números da lista é de: {media}"
    except TypeError as type_e:
        return f"A lista deve conter apenas números. Erro: {type_e}"
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    print(retorna_media([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # A média de números da lista é de: 5.0
    print(retorna_media(["a", "b", "c"]))  # A lista deve conter apenas números. Erro: unsupported operand type(s) for +: 'int' and 'str'
    print(retorna_media([]))  # A lista deve ter ao menos 2 elementos.
