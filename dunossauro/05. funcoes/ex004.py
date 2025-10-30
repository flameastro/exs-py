# ex004: Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere P, se seu argumento for positivo, e N, se seu argumento for zero ou negativo.
def retorna_caractere(numero: int):
    return "P" if numero >= 1 else "N"


if __name__ == "__main__":
    print(retorna_caractere(13))  # P
    print(retorna_caractere(0))  # N
    print(retorna_caractere(-5))  # N
