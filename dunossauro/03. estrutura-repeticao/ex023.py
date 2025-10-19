# ex023: Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
import math

N = int(input("Digite um número inteiro: "))
total_divisoes = 0

print(f"Números primos entre 1 e {N}:")

for num in range(2, N + 1):
    primo = True

    for i in range(2, int(math.sqrt(num)) + 1):
        total_divisoes += 1
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num, end=' ')

print(f"\n\nTotal de divisões executadas: {total_divisoes}")
