# Aproveitando as soluções dos problemas anteriores, escreva um programa em que leia dois vetores de inteiros `v` e `w`, de dimensões `m` e `n` respectivamente, verifique se eles estão ordenados, ordene-os em caso contrário e, em seguida, imprima a intercalação dos dois.
# Exemplo de intercalação:
# `v: 1 4 6 9`  
# `w: 2 3 5 7`
# Saída:
# `1, 2, 3, 4, 5, 6, 7, 9.`

def ler_vetor(nome_vetor, col):
    print(nome_vetor)
    vetor = []

    for l in range(col):
        valor = int(input("Valor: "))
        vetor.append(valor)

    return vetor


def esta_ordenado(vetor):
    for i in range(len(vetor)-1):
        if vetor[i] > vetor[i+1]:
            return False

    return True


def intercalacao(vetor1, vetor2):
    vetor_intercalado = vetor1 + vetor2
    return vetor_intercalado


def ordenacao(vetor):
    for x in range(len(vetor)):
        for item in range(len(vetor) - 1):
            if vetor[item] > vetor[item + 1]:
                troca = vetor[item]
                vetor[item] = vetor[item + 1]
                vetor[item + 1] = troca

    return vetor




m = int(input("Tamanho: "))
v, w = ler_vetor("v", m), ler_vetor("w", m)

vetor_intercalado = intercalacao(v, w)

if not esta_ordenado(vetor_intercalado):
    vetor_intercalado = ordenacao(vetor_intercalado)

print(vetor_intercalado)
