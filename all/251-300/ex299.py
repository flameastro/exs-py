# ex299: Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool
# até 20 litros, desconto de 3% por litro
# acima de 20 litros, desconto de 5% por litro
# Gasolina
# até 20 litros, desconto de 4% por litro
# acima de 20 litros, desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 4.30 e o preço do litro do álcool é R$ 3.90.
litros = int(input("Litros: "))
combustivel = input("Tipo de combustível [A-Álcool/G-Gasolina]: ").upper()
while combustivel not in ["A", "G"]:
    print("Considere escrever o valor corretamente")
    combustivel = input("Tipo de combustível [A-Álcool/G-Gasolina]: ").upper()

if combustivel == "A":
    preco = 3.90
    if litros > 20:
        desconto = 0.05
    else:
        desconto = 0.03
else:
    preco = 4.30
    if litros > 20:
        desconto = 0.06
    else:
        desconto = 0.04

total = preco * (litros - (litros * desconto))
print(f"O total é R${total}")
