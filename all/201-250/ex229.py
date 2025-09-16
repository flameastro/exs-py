# ex229: Crie uma função que aceite uma lista de inteiros como parâmetro e retorne cada elemento da lista multiplicado por 3 apenas se este resultar em par.
def pares_triplicados(lista):
    return [x * 3 for x in lista if x * 3 % 2 == 0]


if __name__ == "__main__":
    print(pares_triplicados([12, 5, 2, 10]))  # [36, 6, 30]
    print(pares_triplicados([15, 64, 128, 512, 78]))  # [192, 384, 1536, 234]
    print(pares_triplicados([27, 39, 21, 15]))  # []