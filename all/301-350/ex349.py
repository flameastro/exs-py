# ex349: Faça um programa que leia duas sequências de inteiros, não necessariamente contendo a mesma quantidade de números. Seu programa deverá:
# - Dizer se a segunda sequência está contida na primeira.  
#   Exemplo:  
#   `v1: 7 3 2 3 2 6 4 7`  
#   `v2: 3 2 6`  
#   Saída: sim
# - Construir um terceiro vetor, sem destruir os originais, que é a concatenação do primeiro com o segundo.  
#   Exemplo:  
#   `v1: 7 3 2 6`  
#   `v2: 5 1 8 4 9`  
#   Saída: 7 3 2 6 5 1 8 4 9
# - Ordenar os elementos do terceiro vetor e, em seguida, imprimir todos os números em ordem crescente.  
#   Exemplo:  
#   `v1: 7 3 2 6`  
#   `v2: 5 1 8 4 9`  
#   Saída: 1 2 3 4 5 6 7 8 9
v = []
w = []

print("--- Vetor v ---")
while True:
    valor = int(input("Valor: "))

    if valor == 0:
        break

    v.append(valor)

print("--- Vetor w ---")
while True:
    valor = int(input("Valor: "))

    if valor == 0:
        break

    w.append(valor)


# 1 - Dizer se a segunda sequência está contida na primeira
def versao1():
    contido = True

    for i in range(len(w)):
        if not w[i] in v and w.count(i) > v.count(i):
            contido = False

    if contido:
        print("O vetor w está contido no vetor v")
    else:
        print("O vetor w não está contido no vetor v")

# 2 - Construir um terceiro vetor, sem destruir os originais, que é a concatenação do primeiro com o segundo
def versao2():
    k = []

    for x in v:
        k.append(x)

    for x in w:
        k.append(x)

    print(k)

# 3 - Ordenar os elementos do terceiro vetor e, em seguida, imprimir todos os números em ordem crescente
def versao3():
    k = []

    for x in v:
        k.append(x)

    for x in w:
        k.append(x)

    for x in range(len(k)):
        for item in range(len(k) - 1):
            if k[item] > k[item + 1]:
                troca = k[item]
                k[item] = k[item + 1]
                k[item + 1] = troca

    print(k)
