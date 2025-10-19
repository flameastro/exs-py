# ex010: Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
n1 = int(input("Insira o primeiro número inteiro: "))
n2 = int(input("Insira o segundo número inteiro: "))

if n1 > n2:
    for numero in range(n1, n2-1, -1):
        print(numero)
else:
    for numero in range(n1, n2+1):
        print(numero)
