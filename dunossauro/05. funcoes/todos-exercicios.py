# ex001: Faça um programa para imprimir:

# 1
# 2   2
# 3   3   3
# .....
# n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
def imprime_n_linhas(n: int):
    for x in range(1, n+1):
        yield f'{str(x)}   ' * x


if __name__ == "__main__":
    for l in imprime_n_linhas(4):
        print(l)
    """
    1   
    2   2   
    3   3   3
    4   4   4   4
    """

    for l in imprime_n_linhas(6):
        print(l)
    """
    1
    2   2
    3   3   3
    4   4   4   4
    5   5   5   5   5
    6   6   6   6   6   6
    """
