# Estrutura Sequencial
# ex001: Faça um programa que mostre a mensagem "Alo mundo" na tela:
print("Hello, World!")


# ex002: Faça um programa que peça um número e então mostre a mensagem "O número informado foi [número]":
numero = int(input("Digite um número inteiro: "))
print(f"O número informado foi: {numero}")


# ex003: Faça um programa que peça dois números e imprima a soma:
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))

soma = n1 + n2
print(f"A soma entre {n1} e {n2} é {soma}")


# ex004: Faça um programa que peça as 4 notas bimestrais e mostre a média.
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média das notas é {media}")


# ex005: Faça um programa que converta metros para centímetros:
metros = float(input("Digite a quantidade de metros: "))
centimetros = metros * 100

print(f"{metros} metros são aproximadamente {centimetros} centímetros")


# ex006: Faça um programa que peça o raio de um círculo, calcule e mostre sua área:
from math import pi
raio = float(input("Digite o raio do círculo"))
area = 3.14 * pi ** 2

print(f"A área do círculo é de aproximadamente {area}")


# ex007: Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado = float(input("Digite o valor do lado do quadrado: "))
area = lado ** 2
dobro_area = area * 2

print(f"A área do quadrado é {area}, e o dobro da área é {dobro_area}")

