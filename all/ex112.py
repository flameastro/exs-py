# ex112: Crie um programa que verifica em que posições há disjuntores ligados e desligados
def verifica_posicoes_disjuntores(disjuntores: list):
    lista_pos = []

    if isinstance(disjuntores, list):
        for pos, disjuntor in enumerate(disjuntores):
            if isinstance(disjuntor, bool) and disjuntor:
                lista_pos.append(pos)

    if len(lista_pos) == 0:
        return "Nenhuma posição."

    return f"Lista de posições: {lista_pos}"


if __name__ == "__main__":
    lista1 = [True, True, False, False, True, False, False, False, True]
    print(verifica_posicoes_disjuntores(lista1))  # Lista de posições: [0, 1, 4, 8]

    lista2 = [False, True, False, False, False, True, True]
    print(verifica_posicoes_disjuntores(lista2))  # Lista de posições: [1, 5, 6]

    lista3 = [True, False, False, True, True, False, False]
    print(verifica_posicoes_disjuntores(lista3))  # Lista de posições: [0, 3, 4]

    lista4 = [1, 4, 6, 7, "Python"]
    print(verifica_posicoes_disjuntores(lista4))  # Nenhuma posição.
