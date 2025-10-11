# ex274: Escreva um programa que salve em cada linha de um arquivo a conversão de temperaturas Fahrenheit para Celsius de 0 a 300.
arquivo = "Conversao-Fahrenheit-para-Celsius.txt"

with open(arquivo, "w") as f:
    for fahrenheit in range(0, 301):
        celsius = (fahrenheit - 32) / 1.8

        f.write(f"{fahrenheit} Graus Fahrenheit equivale a {celsius:.2f} Graus Celsius\n")
