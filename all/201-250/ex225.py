# ex225: Elaborar um programa que leia dez valores numéricos reais e apresente no final o somatório e a média dos valores lidos.
soma = 0

for i in range(10):
    n = float(input("Digite um número real: "))
    soma += n

print(f"A soma dos números é {soma}")
print(f"A média dos números é {soma / 10}")
