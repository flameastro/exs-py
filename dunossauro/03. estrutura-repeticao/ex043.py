# ex043: O cardápio de uma lanchonete é o seguinte:

# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade).
print("Especificação   Código  Preço")
print("Cachorro Quente 100     R$ 1,20")
print("Bauru Simples   101     R$ 1,30")
print("Bauru com ovo   102     R$ 1,50")
print("Hambúrguer      103     R$ 1,20")
print("Cheeseburguer   104     R$ 1,30")
print("Refrigerante    105     R$ 1,00")

codigo = int(input("Digite o código do item: "))
while codigo not in range(100, 106):
    print("Por favor, insira um código válido.")
    codigo = int(input("Digite o código do item: "))

quantidade = int(input("Digite a quantidade do item: "))

if codigo == 100 or codigo == 103:
    preco = 1.20
elif codigo == 101 or codigo == 104:
    preco = 1.30
elif codigo == 102:
    preco = 1.50
elif codigo == 105:
    preco = 1

print(f"O preço total do pedido é de R${preco * quantidade}")
