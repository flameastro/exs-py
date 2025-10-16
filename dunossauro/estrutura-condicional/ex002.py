# ex002: Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print("POSITIVO")
elif numero < 0:
    print("NEGATIVO")
else:
    print("NULO (0)")
