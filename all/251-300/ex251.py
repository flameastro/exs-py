# ex251: Crie uma função que receba uma matriz (Array/Lista bidimensional) com outras sublistas dentro da matriz com números inteiros dentro das sublistas e retorne cada sublista da matriz ordenada com 4 elementos.
# Regras: O argumento da função deve conter uma quantidade indeterminada de sublistas, mas a contagem de cada número deve ser 4. Exemplo: [[2, 1, 1, 1], [2, 2, 1, 2]] -> Explicação: 2 e 1 aparecem 4 vezes na matriz, mas em sublistas diferentes.
# Exemplo: [[2, 1, 1, 1], [2, 2, 1, 2]] -> Deve retornar: [[1, 1, 1, 1], [2, 2, 2, 2]]
# Exemplo: [[4, 3, 2, 1], [1, 1, 3, 1], [2, 4, 3, 2], [4, 4, 3, 2]] -> Deve retornar: [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
# Exemplo: [[7, 3, 4, 4], [4, 3, 7, 3], [4, 7, 7, 3]] -> Deve retornar: [[3, 3, 3, 3], [4, 4, 4, 4], [7, 7, 7, 7]]
def matriz_ordenada(matriz):
    return [sorted([n for l in matriz for n in l])[i-4:i] for i in range(0, len(matriz*4)+1, 4)][1:]


if __name__ == "__main__":
    print(matriz_ordenada([[2, 1, 1, 1], [2, 2, 1, 2]]))  # [[1, 1, 1, 1], [2, 2, 2, 2]]
    print(matriz_ordenada([[4, 3, 2, 1], [1, 1, 3, 1], [2, 4, 3, 2], [4, 4, 3, 2]]))  # [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    print(matriz_ordenada([[7, 3, 4, 4], [4, 3, 7, 3], [4, 7, 7, 3]]))  # [[3, 3, 3, 3], [4, 4, 4, 4], [7, 7, 7, 7]]
