# ex347: Crie uma função em que receba um vetor de inteiros de tamanho n e devolva o valor True se o vetor estiver ordenado e False em caso contrário.
def esta_ordenado(v):
    va = v.copy()

    for x in range(len(v)):
        for item in range(len(v) - 1):
            if v[item] > v[item + 1]:
                troca = v[item]
                v[item] = v[item + 1]
                v[item + 1] = troca

    return v == va


print(esta_ordenado([1, 2, 3]))
print(esta_ordenado([5, 4, 1, 2, 7]))
print(esta_ordenado([1, 5, 4, 1, 2, 3]))
