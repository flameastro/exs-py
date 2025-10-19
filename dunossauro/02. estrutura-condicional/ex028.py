# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

#                 Até 5 Kg                Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se a compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total e valor do desconto
tipo = input("Qual será o tipo de carne? [File Duplo/Alcatra/Picanha] ").lower().strip()
while tipo not in ["file duplo", "alcatra", "picanha"]:
    print("Por favor, certifique de escolher apenas um dos os seguintes tipos de carne: File Duplo/Alcatra/Picanha")
    tipo = input("Qual será o tipo de carne? [File Duplo/Alcatra/Picanha] ").lower().strip()

quantidade = int(input("Quantas carnes deseja? "))
while quantidade not in range(1, 1000):
    print("Por favor, digite um valor adequado.")
    quantidade = int(input("Quantas carnes deseja? "))

cliente_tabajara = input("Você é cliente do Tabajara? [S/N] ").upper().strip()
while cliente_tabajara not in ["S", "N"]:
    print("Por favor, considere inserir S para SIM e N para NÃO.")
    cliente_tabajara = input("Você é cliente do Tabajara? [S/N] ").upper().strip()

desconto = None
if cliente_tabajara == "S":
    desconto = 5


if tipo == "alcatra":
    if quantidade <= 5:
        preco_unitario = 5.90
    else:
        preco_unitario = 6.80
elif tipo == "file duplo":
    if quantidade <= 5:
        preco_unitario = 4.90
    else:
        preco_unitario = 5.80
elif tipo == "picanha":
    if quantidade <= 5:
        preco_unitario = 6.90
    else:
        preco_unitario = 7.80


preco = (preco_unitario * quantidade) + desconto


print(" NOTA FISCAL ".center(50, "-"))
print(f"Tipo de carne: {tipo}")
print(f"Quantidade de carne: {quantidade}")
print(f"Preço total: {preco:.2f}")
print(f"Valor do desconto: {desconto}%")
