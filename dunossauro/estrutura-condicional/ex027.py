# e027: Uma fruteira está vendendo frutas com a seguinte tabela de preços:
#                 Até 5 Kg                Acima de 5 Kg
# Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
# Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
morangos = float(input("Digite a quantidade de morangos em kg: "))
while morangos not in range(1, 10000):
    print("Por favor, insira um valor adequado.")
    morangos = float(input("Digite a quantidade de morangos em kg: "))

macas = float(input("Digite a quantidade de maças em kg: "))
while macas not in range(1, 10000):
    print("Por favor, insira um valor adequado.")
    macas = float(input("Digite a quantidade de maças em kg: "))


if morangos <= 5:
    preco_morango = 2.50
else:
    preco_morango = 2.20


if macas <= 5:
    preco_maca = 1.80
else:
    preco_maca = 1.50

preco = (preco_maca * macas) + (preco_morango * morangos)

if (morangos + macas > 8) or (preco > 25):
    desconto = 10
    preco -= (preco * desconto) / 100

print(f"Preço a pagar: R${preco:.2f}.")
