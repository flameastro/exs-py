# ex093: Crie uma função que retorne o primeiro elemento de uma lista
def retorna_primeiro_elemento(lista: list):
    if len(lista) > 0:
        return f"O primeiro elemento da lista é {lista[0]}"

    return "A lista deve possuir ao menos um elemento."

if __name__ == "__main__":
    lista1 = ["Maçã", "Banana", "Laranja", "Abacaxi"]
    print(retorna_primeiro_elemento(lista1))  # O primeiro elemento da lista é Maçã

    lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # O primeiro elemento da lista é 1
    print(retorna_primeiro_elemento(lista2))

    lista3 = []
    print(retorna_primeiro_elemento(lista3))  # A lista deve possuir ao menos um elemento.
