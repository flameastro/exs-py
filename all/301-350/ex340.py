# ex340: Elabore um programa que represente o algoritmo para calcular a soma dos primeiros 40 termos da sequência definida a seguir, com o valor de A fornecido via teclado:
# ((7 * A) / 3) + ((7 * A ) / 6) + ((7 * A ) / 12) + ((7 * A ) / 24) + ((7 * A ) / 48)
A = int(input("Insira o valor de A: "))

soma = 0
denominador = 3

for x in range(40):
    termo = (7 * A) / denominador
    soma += termo
    denominador *= 2


print(f"A soma dos primeiros 40 termos com o A = {A} é: {soma}")
