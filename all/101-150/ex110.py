# ex110: Crie uma função que recebe uma lista como parâmetro e retorne quais elementos NÃO são repetidos
def verifica_nao_repetidos(lista: list):
    if len(lista) < 1:
        return "A lista deve possuir ao menos 1 elemento."

    nao_repetidos = []
    for elemento in lista:
        if lista.count(elemento) == 1:
            nao_repetidos.append(elemento)

    if len(nao_repetidos) > 0:
        return f"Os elementos não repetidos são: {nao_repetidos}"

    return "Todos os itens se repetem."


if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Os elementos não repetidos são: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(verifica_nao_repetidos(lista1))

    lista2 = ["a", "b", "a", "c"]
    print(verifica_nao_repetidos(lista2))  # Os elementos não repetidos são: ['b', 'c']

    lista3 = []
    print(verifica_nao_repetidos(lista3))  # A lista deve possuir ao menos 1 elemento.

    lista4 = ["a"]
    print(verifica_nao_repetidos(lista4))  # Os elementos não repetidos são: ['a']

    lista5 = ["a", "a", "a"]
    print(verifica_nao_repetidos(lista5))  # Todos os itens se repetem.
