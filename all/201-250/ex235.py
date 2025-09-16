# ex235: Média Simples: Peça ao usuário para digitar três notas e calcule a média aritmética.
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

media = sum([n1, n2, n3]) / 3
print(f"A sua média é {media}")
