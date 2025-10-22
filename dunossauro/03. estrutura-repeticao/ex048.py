# ex048: Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
# Exemplo:
#   12376489 => 98467321
numero = str(int(input("Digite um número inteiro: ")))
print(f"{numero} => {numero[::-1]}")
