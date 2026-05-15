# ex342: Crie uma função que aceite como parâmetro dois arrays com tamanho iguais, e retorne outra função que tem a soma das funções, de cada posição do array 1 e array 2.
# Também retorne um aviso caso tenha como argumento funções de tamanho diferente.
def soma_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return "As funções não podem ter tamanho diferentes"

    sarr = []

    for i in range(len(arr1)):
        sarr.append(arr1[i] + arr2[i])

    return sarr

if __name__ == "__main__":
    print(soma_arrays([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]))  # [2, 4, 6, 8, 10]
    print(soma_arrays([2, 5, 4], [3, 2, 2]))  # [5, 7, 6]
    print(soma_arrays([5, 4, 7, 8, 9], [2, -1, 0]))  # As funções não podem ter tamanho diferentes
