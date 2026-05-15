# ex343: Crie uma função que tenha um número como parâmetro e retorne uma lista com cada número desse número em uma lista ordenada por ordem crescente
def orderna_numeros(n):
    narr = []

    for x in str(n):
        narr.append(int(x))

    return list(sorted(narr))


if __name__ == "__main__":
    print(orderna_numeros(753))  # [3, 5, 7]
    print(orderna_numeros(312313))  # [1, 1, 2, 3, 3, 3]
    print(orderna_numeros(4763))  # [3, 4, 6, 7]
