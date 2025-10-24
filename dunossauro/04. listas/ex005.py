# ex005: Faça um programa que leia 10 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
par = []
impar = []
numeros = []

for i in range(10):
    numero = int(input("Insira um número: "))

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

    numeros.append(numero)


print(f"Números inseridos: {numeros}")
print(f"Números PARES: {par}")
print(f"Números ÍMPARES: {impar}")
