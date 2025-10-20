# ex031: O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

# Lojas Tabajara
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
print("Lojas Tabajara")
total = 0
i = 1
while True:
    preco = float(input(f"Produto {i}: R$ "))
    while preco < 0:
        print("Certifique-se de inserir um valor positivo.")
        preco = float(input(f"Produto {i}: R$ "))

    total += preco

    if preco == 0:
        break

    i += 1

print(f"Total: {total:.2f}")

dinheiro = float(input("Dê o dinheiro ao caixa: R$ "))
if dinheiro >= total:
    troco = dinheiro - total
    print(f"Total: {total:.2f}")
    print(f"Dinheiro: {dinheiro:.2f}")
    print(f"Troco: {troco:.2f}")
else:
    print("Oops, não é possível realizar o pagamento, pois o dinheiro é menor que o total da compra.")
