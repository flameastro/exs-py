# ex127: Crie uma função que remove itens duplicados de uma lista, sem usar set.
def remove_duplicate_items(any_list: list, ordered: bool = False):
    if len(any_list) < 1:
        return "Lista Inválida."

    new_list = []
    for element in any_list:
        if element not in new_list:
            new_list.append(element)

    if ordered:
        new_list.sort()

    return new_list


if __name__ == "__main__":
    list1 = ["Mario", "Maria", "Felipe", "Jorge", "Jorge", "Maria"]
    print(remove_duplicate_items(list1, False))  # ['Mario', 'Maria', 'Felipe', 'Jorge']

    list2 = []
    print(remove_duplicate_items(list2, False))  # Lista Inválida.

    list3 = [3, 9, 8, 3, 2, 0, 5, 2, 8, 1, 5, 3, 8, 4, 5, 2, 1, 0]
    print(remove_duplicate_items(list3, True))  # [0, 1, 2, 3, 4, 5, 8, 9]
