# ex002: Faça um programa para imprimir:
# 1
# 1   2
# 1   2   3
# .....
# 1   2   3   ...  n
# Para um n informado pelo usuário. Use uma função que receba um valor n inteiro, imprima até a n-ésima linha.
def imprime_linhas_numeradas(n: int):
    for x in range(1, n+1):
        yield "   ".join([str(x) for x in range(1, x+1)])


if __name__ == "__main__":
    for item in imprime_linhas_numeradas(3):
        print(item)
    """
    1
    1   2
    1   2   3
    """

    for item in imprime_linhas_numeradas(12):
        print(item)
    """
    1
    1   2
    1   2   3
    1   2   3   4
    1   2   3   4   5
    1   2   3   4   5   6
    1   2   3   4   5   6   7
    1   2   3   4   5   6   7   8
    1   2   3   4   5   6   7   8   9
    1   2   3   4   5   6   7   8   9   10
    1   2   3   4   5   6   7   8   9   10   11
    1   2   3   4   5   6   7   8   9   10   11   12
    """
