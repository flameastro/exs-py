# ex247: Dado listas dentro de uma outra lista pai, crie uma função que retorne apenas UMA lista com seus respectivos elementos. Exemplo: [["Python"], ["JavaScript"], [5], [True]] -> ["Python", "JavaScript", 5, True]
def lista_unica(lista: list):
    return [element[0] for element in lista]


if __name__ == "__main__":
    lista1 = [["Python"], ["JavaScript"], [5], [True]]
    print(lista_unica(lista1))  # ['Python', 'JavaScript', 5, True]

    lista2 = [[False], ["Linux"], ["GitHub"], [6.78]]
    print(lista_unica(lista2))  # [False, 'Linux', 'GitHub', 6.78]
