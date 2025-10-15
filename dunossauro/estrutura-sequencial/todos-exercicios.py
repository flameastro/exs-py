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


# ex008: Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
ganho_hora = float(input("Quantos reais você ganha por hora? "))
horas_mes = int(input("Quantas horas você trabalha por mês? "))

salario = ganho_hora * horas_mes
print(f"Seu salário é de aproximadamente R${salario}.")


# ex009: Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# Formula
# C = 5 * ((F-32) / 9).
fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
celsius = 5 * ((fahrenheit - 32) / 9)

print(f"{fahrenheit} Graus em Fahrenheit equivale a {celsius} Graus Celsius.")


# ex010: Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# Formula
# F = (C * 9/5) + 32
celsius = float(input("Digite a temperatura em Graus Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius} Graus em Celsius equivale a {fahrenheit} Graus Fahrenheit.")


# ex011: Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:
# O produto do dobro do primeiro com metade do segundo .
# A soma do triplo do primeiro com o terceiro.
# O terceiro elevado ao cubo.
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = float(input("Digite o terceiro número real: "))

print(f"O produto do dobro do primeiro com metade do segundo é {(n1 * 2) * (n2 / 2)}")
print(f"A soma do triplo do primeiro com o terceiro é {(n1 * 3) + n3}")
print(f"O terceiro elevado ao cubo é {n3 ** 3}")


# ex012: Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes, usando a seguinte fórmula:
# Formula
# Gigabytes * 1024
gigabytes = int(input("Digite a quantidade de Gigabytes do arquivo: "))
megabytes = gigabytes * 1024

print(f"A conversão de {gigabytes} Gigabytes para Megabytes é {megabytes}.")


# ex013: Tendo como dados de entrada um arquivo em Gigabytes, construa um algoritmo que faça a conversão para Megabytes e Kilobytes, usando as seguintes fórmulas:

# Para Megabytes: Gigabytes * 1024
# Para Kilobytes: Gigabytes * 1024 * 1024
# Responda o tamanho do arquivo em Megabytes e o tamanho em Kilobytes.
gigabytes = int(input("Digite a quantidade de Gigabytes do arquivo: "))
megabytes = gigabytes * 1024
kilobytes = gigabytes * 1024 * 1024

print(f"{gigabytes} Gigabytes equivalem a {megabytes} megabytes ou {kilobytes} kilobytes.")


# ex014: João, um pescador, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
peso = float(input("Digite o peso total dos peixes em kg: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4

    print(f"O excesso de quilos de peixe é {excesso}, e a multa é de R${multa}.")
else:
    print("Não houve excesso de peso.")


# ex015: Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.
ganho_hora = float(input("Insira a quantidade de reais que você ganha por hora: "))
horas_mes = int(input("Digite a quantidade de horas trabalhadas num mês: "))

salario_bruto = ganho_hora * horas_mes
IMPOSTO_RENDA = (salario_bruto * 11) / 100
INSS = (salario_bruto * 8) / 100
SINDICATO = (salario_bruto * 5) / 100

salario_liquido = salario_bruto - (IMPOSTO_RENDA + INSS + SINDICATO)

print(" Detalhes do Salário ".center(50, "-"))
print(f"Salário Bruto: R${salario_bruto:.2f}")
print(f"Salário líquido: R${salario_liquido:.2f}")
print(f"Imposto de Renda: R${IMPOSTO_RENDA:.2f}")
print(f"INSS: R${INSS:.2f}")
print(f"Sindicato: R${SINDICATO:.2f}")


# ex016: Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
area = int(input("Digite o tamanho da área em metros quadrados: "))

cobertura = area / 3
latas = cobertura / 18
preco = latas * 80

print(" Detalhes ".center(25, "-"))
print(f"Área: {area:.2f}")
print(f"Cobertura: {cobertura:.2f} litros")
print(f"Latas: {latas:.2f}")
print(f"Preço: {preco:.2f}")


# ex017: Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
area = int(input("Digite o tamanho da área em metros quadrados: "))
cobertura = area / 6

latas = cobertura / 18
preco_latas = latas * 80

galoes = cobertura / 3.6
preco_galoes = galoes * 25

print(" Detalhes ".center(25, "-"))
print(f"Cobertura: {cobertura:.2f} litros")
print("Comprando em Latas:")
print(f"Latas: {latas:.2f}")
print(f"Preço: {preco_latas:.2f}")
print("Comprando em Galões:")
print(f"Galões: {galoes:.2f}")
print(f"Preço dos Galões: {preco_galoes:.2f}")


# ex018: Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
tamanho_arquivo = float(input("Digite o tamanho do arquivo (em MB): "))
velocidade_link = float(input("Digite a velocidade da internet (em Mbps): "))
tempo_minutos = (tamanho_arquivo * 8) / (velocidade_link * 60)

print(f"O tempo aproximado de download é de {tempo_minutos:.2f} minutos.")
