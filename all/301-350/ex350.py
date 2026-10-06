# ex350: Faça um programa em que leia dois vetores de números inteiros e descubra se um
# deles é permutação do outro, isto é, se eles tem os mesmos elementos, ainda
# que em ordem diferente. A quantidade de elementos lidos em cada vetor é no
# máximo 100, e cada sequ^encia termina quando o valor 0 é digitado. Por exemplo:
# [2; 2; 0; 3; 4] e [2; 2; 0; 3; 4]: sim.
# [2; 2; 0; 3; 4] e [4; 3; 2; 0; 2]: sim.
# [2; 2; 0; 3; 4] e [4; 3; 4; 0; 2]: não.
# [3; 0; 5] e [3; 0; 5; 3]: n~ao.
# Implemente duas versões deste problema:
# Ordenando os vetores para em seguida compará-los;
# Sem ordenar os vetores;
v = []
w = []

n = 0
print("Vetor v")
for i in range(101):
    valor = int(input("Valor: "))

    if valor == 0:
        break

    v.append(valor)
    n += 1

print("Vetor w")
for i in range(n):
    valor = int(input("Valor: "))

    if valor == 0:
        break

    w.append(valor)


# Versão 1 - Ordenando os vetores para em seguida compará-los
def versao1():
    # Ordena v
    for _ in range(len(v)):
        for item in range(len(v) - 1):
            if v[item] > v[item + 1]:
                troca = v[item]
                v[item] = v[item + 1]
                v[item + 1] = troca


    # Ordena w
    for _ in range(len(w)):
        for item in range(len(w) - 1):
            if w[item] > w[item + 1]:
                troca = w[item]
                w[item] = w[item + 1]
                w[item + 1] = troca


    # Verificando vetores
    identicos = True

    for i in range(len(v)):
        if v[i] != w[i]:
            identicos = False

    if identicos:
        print("São idênticos")
    else:
        print("São diferentes")

# Versão 2 - Sem ordenar os vetores
def versao2():
    d = {}

    for i in range(len(v)):
        if d.get(v[i]):
            d[v[i]] += 1
        else:
            d[v[i]] = 1

        if d.get(w[i]):
            d[w[i]] += 1
        else:
            d[w[i]] = 1


    # Percorre e verifica se existe uma contagem para determinado elemento que seja ímpar. Se tiver -> Quer dizer que existe apenas um elemento entre v e w, atuomaticamente ambos são diferentes
    identicos = True
    for value in d.values():
        if value % 2 == 1:
            identicos = False

    if identicos:
        print("São identicos")
    else:
        print("São diferentes")
