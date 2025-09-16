# ex227: Imagine uma máquina que possua somente as operações aritméticas de soma e subtração. Escreva um algoritmo para fazer uma multiplicação.

def multiplicacao(a, b):
    soma = 0

    for _ in range(b):
        soma += a

    return soma


if __name__ == "__main__":
    print(multiplicacao(15, 3))  # 45
    print(multiplicacao(12, 7))  # 84
    print(multiplicacao(28, 95))  # 2660
