# ex223: Construir um programa que apresente a soma dos cem primeiros números naturais (1+2+3+ ... +98+99+100).
soma = 0

for i in range(1, 101):
    soma += i

print(f"A soma dos cem primeiros números naturais é de {soma}")  # A soma dos cem primeiros números naturais é de 5050
