# ex021: Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
saque = int(input("Digite o valor do saque: "))

notas_cem = 0
notas_cinquenta = 0
notas_dez = 0
notas_cinco = 0
notas_um = 0

while saque >= 100:
    saque -= 100
    notas_cem += 1

while saque >= 50:
    saque -= 50
    notas_cinquenta += 1

while saque >= 10:
    saque -= 10
    notas_dez += 1

while saque >= 5:
    saque -= 5
    notas_cinco += 1

while saque >= 1:
    saque -= 1
    notas_um += 1


print(f"Notas de cem: {notas_cem}")
print(f"Notas de cinquenta: {notas_cinquenta}")
print(f"Notas de dez: {notas_dez}")
print(f"Notas de cinco: {notas_cinco}")
print(f"Notas de um: {notas_um}")
print(f"Resultado: {(notas_cem * 100) + (notas_cinquenta * 50) + (notas_dez * 10) + (notas_cinco * 5) + (notas_um * 1)}")
