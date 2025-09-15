# ex214: Efetuar a leitura de um valor numérico inteiro positivo ou negativo representado pela variável N e apresentar o valor lido como sendo positivo. Dica: se o valor lido for menor que zero, ele deve ser multiplicado por -1.
N = int(input("Digite um número inteiro: "))

if N >= 0:
    formula = N * 1
else:
    formula = N * -1

print(f"O valor de {N} absoluto é {formula}.")
