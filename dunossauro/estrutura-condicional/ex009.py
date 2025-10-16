# ex009: Faça um programa que leia três números e mostre-os em ordem decrescente
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

print(f"Os números em ordem decrescente são: {", ".join(sorted([str(numero) for numero in [n1, n2, n3]], reverse=True))}")
