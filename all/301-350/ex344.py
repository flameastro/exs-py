# ex344: Crie uma função que tenha range1 e range2 como parâmetros e retorne todos os números pares desde o range1 até o range2.
def pares_range(range1, range2):
    return [x for x in range(range1, range2+1) if x % 2 == 0]

if __name__ == "__main__":
    print(pares_range(1, 10))  # [2, 4, 6, 8, 10]
    print(pares_range(9, 24))  # [10, 12, 14, 16, 18, 20, 22, 24]
    print(pares_range(0, -9))  # []

