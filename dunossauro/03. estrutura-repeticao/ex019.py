# ex019: Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
conjunto = []
while True:
    numero = int(input("Digite um número entre 0 a 1000 ou 0 para sair: "))
    while numero not in range(0, 1001):
        print("Por favor, insira um número entre 0 a 1001.")
        numero = int(input("Digite um número entre 0 a 1000 ou 0 para sair: "))


    if numero == 0:
        break

    conjunto.append(numero)

conjunto = sorted(conjunto)

maior = conjunto[-1]
menor = conjunto[0]

soma = 0
for numero in conjunto:
    soma += numero

print(f"O maior número do conjunto é: {maior}.")
print(f"O menor número do conjunto é: {menor}.")
print(f"A soma dos números do conjunto é: {soma}.")
