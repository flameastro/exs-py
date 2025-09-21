# ex246: Remover Elementos Falsy: Dada uma lista, remova todos os elementos que são considerados "falsy" (0, None, False, [], "").
def remove_falsy(lista):
    return [l for l in lista if l is False][0]


if __name__ == "__main__":
    print(remove_falsy([0, None, False, [], ""]))  # False
