# ex015: Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;
lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if (lado1 + lado2) > lado3:
    if lado1 == lado2 and lado1 == lado3:
        print("Triângulo Equilátero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Triângulo Isósceles")
    elif lado1 != lado2 and lado1 != lado3:
        print("Triângulo Escaleno")
else:
    print("Isso não é um triângulo.")
