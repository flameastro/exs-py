# ex006: Faça um programa que peça o raio de um círculo, calcule e mostre sua área:
from math import pi
raio = float(input("Digite o raio do círculo: "))
area = pi * raio ** 2

print(f"A área do círculo é de aproximadamente {area}")
