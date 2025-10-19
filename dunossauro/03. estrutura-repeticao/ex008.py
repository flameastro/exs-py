# ex008: Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
for i in range(5):
    numero = float(input(f"Digite o {i+1}o número: "))
    soma += numero

media = soma / 5
print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")
