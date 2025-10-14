# ex281: Crie um programa que peça ao usuário números inteiros indefinidamente até que o usuário insira o valor "0". Ao final do programa, imprima os pares, a soma e a média dos números digitados.
numeros = []
while True:
    numero = int(input("Insira um número inteiro ou 0 para sair. "))

    if numero == 0:
        break

    numeros.append(numero)


if len(numeros) == 0:
    print(f"A lista não possui nenhum número, impossível realizar operações.")
else:
    soma = 0
    pares = []

    for numero in numeros:
        soma += numero

        if numero % 2 == 0:
            pares.append(str(numero))

    media = soma / len(numeros)

    print(f"Os números pares da lista são: {', '.join(pares) if pares else 'Nenhum número par'}")
    print(f"A soma dos números digitados é {soma}")
    print(f"A média dos números digitados é {media}")
