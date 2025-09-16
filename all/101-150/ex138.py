# ex138: Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
codigo1 = int(input("Digite o código da peça 1:\n>>> "))
numero1 = int(input("Digite quantas peças são:\n>>> "))
valor1 = float(input("Digite o valor unitário de cada peça 1:\n>>> "))
calculo1 = numero1 * valor1

codigo2 = int(input("Digite o código da peça 2:\n>>> "))
numero2 = int(input("Digite quantas peças são:\n>>> "))
valor2 = float(input("Digite o valor unitário de cada peça 2:\n>>> "))
calculo2 = numero2 * valor2

valor = calculo1 + calculo2

print(f"VALOR A PAGAR: R$ {valor:.2f}")
