# ex051: Faça um programa que mostre os n termos da Série a seguir:
# S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
# Imprima no final a soma da série.

termos = int(input("Quantidade de termos: "))
s = 0
numerador = 1
denominador = 1

print("Série: ", end="")

for i in range(termos):
    if i < termos - 1:
        print(f"{numerador}/{denominador}", end=" + ")
    else:
        print(f"{numerador}/{denominador}")
    
    s += numerador / denominador
    numerador += 1
    denominador += 2

print(f"Soma da série: {s:.2f}")
