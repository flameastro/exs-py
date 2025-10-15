# ex010: Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# Formula
# F = (C * 9/5) + 32
celsius = float(input("Digite a temperatura em Graus Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius} Graus em Celsius equivale a {fahrenheit} Graus Fahrenheit.")
