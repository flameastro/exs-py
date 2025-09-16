# ex224: Elaborar um programa que apresente o somatório dos valores pares existentes na faixa de 1 até 500.
soma = 0

for i in range(0, 501, 2):
    soma += i

print(f"A soma dos valores pares existentes na faixa de 1 até 500 é de {soma}")  # A soma dos valores pares existentes na faixa de 1 até 500 é de 62750
