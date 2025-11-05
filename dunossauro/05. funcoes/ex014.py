# ex014: Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

# 8  3  4
# 1  5  9
# 6  7  2
# Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica: produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar uma matriz 3x3.
import itertools

def quadrado_magico(numeros):
    m = [numeros[0:3], numeros[3:6], numeros[6:9]]
    linhas = [sum(linha) for linha in m]

    colunas = [sum([m[i][j] for i in range(3)]) for j in range(3)]

    diagonal1 = m[0][0] + m[1][1] + m[2][2]
    diagonal2 = m[0][2] + m[1][1] + m[2][0]

    todas_somas = linhas + colunas + [diagonal1, diagonal2]

    return all(s == todas_somas[0] for s in todas_somas)


def quadrados_magicos():
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    contador = 0

    for perm in itertools.permutations(numeros):
        if quadrado_magico(perm):
            contador += 1
            print(f"\nQuadrado mágico #{contador}:")
            print(f"{perm[0]} {perm[1]} {perm[2]}")
            print(f"{perm[3]} {perm[4]} {perm[5]}")
            print(f"{perm[6]} {perm[7]} {perm[8]}")

    print(f"\nForam encontrados {contador} quadrados mágicos.")


quadrados_magicos()
