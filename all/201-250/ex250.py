# ex250: Crie uma função que receba x e y como valores inteiros e retorne uma lista de pares e uma lista de ímpares desses ranges.
def pares_impares(x, y):
    pares = [str(n) for n in range(x, y+1) if n % 2 == 0]
    impares = [str(n) for n in range(x, y+1) if n % 2 == 1]

    return (
        f"Ímpares: {", ".join(impares)}\n"
        f"Pares: {", ".join(pares)}"
    )


if __name__ == "__main__":
    print(pares_impares(15, 29))  # Ímpares: 15, 17, 19, 21, 23, 25, 27, 29; Pares: 16, 18, 20, 22, 24, 26, 28
    print(pares_impares(1, 10))  # Ímpares: 1, 3, 5, 7, 9; Pares: 2, 4, 6, 8, 10
    print(pares_impares(25, 50))  # Ímpares: 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49;Pares: 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50
