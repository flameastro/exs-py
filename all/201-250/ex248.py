# ex248: Peça ao usuário 3 números inteiros e diga se eles são iguais ou não
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 == n2 and n1 == n3:
    print("Os números são iguais")
else:
    print("Os números são diferentes")
