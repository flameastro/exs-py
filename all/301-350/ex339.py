# ex339: Elabore um programa que represente o algoritmo para calcular a soma dos primeiros N termos da sequência definida a seguir, com N fornecido via teclado:
# (1 / 2) + (1 / 4) + (1 / 6) + (1 / 8) + (1 / 10)
n = int(input("Digite a quantidade de termos: "))
soma = 0

denominador = 2

for x in range(n):
    soma += 1 / denominador
    denominador += 2

print(f"A soma dos {n} termos é: {soma}")
