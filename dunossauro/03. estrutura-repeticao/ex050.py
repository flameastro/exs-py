# ex050: Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
n = int(input("Quantidade de Termos: "))

h = 1
for i in range(2, n+1):
    print(h + (1 / i))
    h += (1 / i)

print(f"Valor de H = {h:.5f}")
