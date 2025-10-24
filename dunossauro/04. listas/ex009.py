# ex009: Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
lista = []
for i in range(10):
    numero = int(input("Insira um número inteiro: "))
    lista.append(str(numero ** 2))

print(f"Lista com o cálculo dos quadrados dos elementos: {", ".join(lista)}")
