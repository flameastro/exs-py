# ex221: Ler um número inteiro qualquer e multiplicá-lo por dois. Apresentar o resultado da multiplicação somente se o resultado for maior que 30.
n = int(input("Digite um número inteiro qualquer: "))
resultado = n * 2

if resultado > 30:
    print(f"O resultado é {resultado}")
