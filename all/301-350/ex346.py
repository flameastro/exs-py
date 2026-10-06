# ex346: Faça um programa que leia e armazene em um vetor
# uma sequência de inteiros. Em seguida o programa deve ler
# uma sequência de inteiros informados pelo usuário e, para cada um
# deles, dizer se ele pertence ou não ao vetor armazenado previamente.
vetor = []

print("Inserindo elementos no vetor")
for i in range(10):
    valor = int(input("Valor: "))
    vetor.append(valor)

print("Verificando elementos")
for i in range(10):
    valor = int(input("Valor: "))
    pertence = False

    for j in range(len(vetor)):
        if valor == vetor[j]:
            pertence = True
            pos = j
            break

    if pertence:
        print(f"{valor} pertence ao vetor na posição {pos} (primeira ocorrência)")
    else:
        print(f"{valor} não pertence ao vetor")
