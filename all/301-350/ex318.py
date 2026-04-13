# ex318: A partir de um conjunto de números inteiros sequenciais, obtidos com base em dados fornecidos pelo usuário (número inicial e final), identifique e apresente:
# a) A quantidade de números  positivos.
# b) A quantidade de números pares.
# c) A quantidade de números ímpares.
# d) A quantidade de números ímpares e divisíveis por 3 e 7.
# e) A respectiva média para cada um dos itens.
# Obs: Valide se o número inicial é maior que o número final
inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))

# Variáveis necessárias
positivos = 0
pares = 0
impares = 0
impares_divisiveis = 0
numeros = 0
soma = 0
media = 0

if inicio < fim:
    for i in range(inicio, fim+1):
        if i > 0:
            positivos += 1

        if i % 2 == 0:
            pares += 1
        else:
            impares += 1

        if (i % 2 != 1) and (i % 3 == 0) and (i % 7 == 0):
            impares_divisiveis += 1

        soma += i
        numeros += 1

    media = soma / numeros
    print(f"Quantidade de números positivos: {positivos}")
    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números impares: {impares}")
    print(f"Quantidade de números impares divisíveis por 3 e 7: {impares_divisiveis}")
    print(f"Média de todos os números: {media}")
else:
    print("Certifique-se de inserir um valor inicial menor que o valor final")
