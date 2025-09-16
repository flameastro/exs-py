# ex073: Crie uma função que recebe uma lista e um elemento, e verifique se aquele elemento está ou não presente na lista
def verifica_elemento_na_lista(lista: list, elemento):
    if elemento in lista:
        indice_elemento = lista.index(elemento)
        return f"O elemento está na lista, no índice {indice_elemento}"

    return f"O elemento ({elemento}) não está presente na lista ({lista})"


if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5]
    print(verifica_elemento_na_lista(lista1, 2))  # O elemento está na lista, no índice 1

    lista2 = ["A", "B", "C", "D", "E"]
    print(verifica_elemento_na_lista(lista2, "Z"))  # O elemento (Z) não está presente na lista (['A', 'B', 'C', 'D', 'E'])

    lista3 = []
    print(verifica_elemento_na_lista(lista3, "A"))  # O elemento (A) não está presente na lista ([])
