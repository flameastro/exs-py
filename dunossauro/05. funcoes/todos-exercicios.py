# ex001: Faça um programa para imprimir:

# 1
# 2   2
# 3   3   3
# .....
# n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
def imprime_linhas(n: int):
    for x in range(1, n+1):
        yield f'{str(x)}   ' * x


if __name__ == "__main__":
    for l in imprime_linhas(4):
        print(l)
    """
    1   
    2   2   
    3   3   3
    4   4   4   4
    """

    for l in imprime_linhas(6):
        print(l)
    """
    1
    2   2
    3   3   3
    4   4   4   4
    5   5   5   5   5
    6   6   6   6   6   6
    """


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


# ex003: Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
def soma(x: float, y:float , z:float):
    return sum([x, y, z])


if __name__ == "__main__":
    print(soma(3, 5, 4))  # 12
    print(soma(25, 25, 50))  # 100
    print(soma(56, 7, 1))  # 64


# ex004: Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere P, se seu argumento for positivo, e N, se seu argumento for zero ou negativo.
def retorna_caractere(numero: int):
    return "P" if numero >= 1 else "N"


if __name__ == "__main__":
    print(retorna_caractere(13))  # P
    print(retorna_caractere(0))  # N
    print(retorna_caractere(-5))  # N


# ex005: Faça um programa com uma função chamada soma_imposto. A função possui dois parâmetros formais: taxa_imposto, que é a quantia de imposto sobre vendas expressas em porcentagem, e custo, que é o custo de um item antes do imposto. A função "altera" o valor de custo para incluir o imposto sobre vendas.
def soma_imposto(custo: float, taxa_imposto: float):
    return custo - (custo * taxa_imposto)


if __name__ == "__main__":
    print(soma_imposto(1250.99, 0.4))  # 750.594
    print(soma_imposto(25350, 0.15))  # 21547.5
    print(soma_imposto(785.8, 0.45))  # 432.18999999999994
