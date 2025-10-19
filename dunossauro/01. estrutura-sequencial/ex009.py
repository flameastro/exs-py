# ex009: Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# Formula
# C = 5 * ((F-32) / 9).
fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)

print(f"{fahrenheit} Graus em Fahrenheit equivale a {celsius} Graus Celsius.")
