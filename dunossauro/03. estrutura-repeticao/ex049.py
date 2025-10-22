# ex049: Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.
n = int(input("Quantos termos da série deseja mostrar? "))

soma = 0
den = 1

print("Série: ", end="")

for num in range(1, n + 1):
    termo = num / den
    print(f"{num}/{den}", end="")

    if num < n:
        print(" + ", end="")

    soma += termo
    den += 2

print(f"\n\nSoma da série = {soma:.2f}")
