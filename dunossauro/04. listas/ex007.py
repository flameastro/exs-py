# ex007: Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
numeros = []
multiplicacao = 1
soma = 0
for x in range(5):
    numero = int(input("Digite um numero inteiro: "))

    numeros.append(str(numero))

    multiplicacao *= numero
    soma += numero


print(f"A soma dos números informados é de {soma}")
print(f"A multiplicação entre os números resulta em {multiplicacao}")
print(f"Os números informados são {", ".join(numeros)}")
