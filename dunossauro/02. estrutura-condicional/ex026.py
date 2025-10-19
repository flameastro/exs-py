# ex026: Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool:
# até 20 litros: desconto de 3% por litro
# acima de 20 litros: desconto de 5% por litro
# Gasolina: - até 20 litros: desconto de 4% por litro - acima de 20 litros: desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
litros = float(input("Digite a quantidade de litros vendidos: "))
combustivel = input("Digite o tipo de combustível (A para Álcool/G para Gasolina): ").upper()
while combustivel not in ["A", "G"]:
    print("Certifique-se de informar o tipo de combustível corretamente.")
    combustivel = input("Digite o tipo de combustível (A para Álcool/G para Gasolina): ").upper()

if combustivel == "A":
    preco = 1.90
    if litros <= 20:
        desconto = 3
    else:
        desconto = 5

    total = (preco * litros) / ((litros * desconto) / 100)
elif combustivel == "G":
    preco = 2.50
    if litros <= 20:
        desconto = 4
    else:
        desconto = 6

    total = (preco * litros) / ((litros * desconto) / 100)
else:
    print("Algum erro ocorreu. Tente novamente.")

print(f"Total: R${total}")