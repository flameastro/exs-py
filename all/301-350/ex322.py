# ex322: Com o crescimento de sua loja, Pedro solicitou novas funcionalidades para o sistema. Os desenvolvedores sugeriram criar do zero uma versão 2.0 e manter somente as funcionalidades mais utilizadas da versão anterior. O sistema deve funcionar da seguinte maneira:
# Na tela principal, será apresentada a mensagem “Bem-vindo ao autoatendimento da bicicletaria XPTO Bikes.” Abaixo da mensagem deve ser exibida a mensagem solicitando o nome do cliente. Ao digitar seu nome, o sistema deve apresentar o seguinte menu:
# 2.1. Opção 1 – Ver promoções.
# 2.2. Opção 2 – Solicitar serviço de manutenção.
# 2.3. Opção 3 – Listar carrinho de compra.
# 2.3. Opção 4 - Finalizar carrinho de compra.
# 2.5. Opção 0 - Sair.
# Abaixo deve ser exibida a mensagem “Digite sua opção desejada:”.
# Se o cliente digitar a opção 1, o sistema deve apresentar os seguintes itens:
# 4.1. Código 101 - Bicicleta nova na cor amarela, aro 26, com 18 marchas e na promoção pelo preço de R$ 999,99.
# 4.2. Código 102 - Bicicleta usada na cor azul, aro 26, com 18 marchas e com o valor promocional de R$ 400,00.
# 4.3. Código 103 - Capacete de proteção por R$59,99.
# 4.4. Código 104 - Freio a disco por R$ 89,99.
# 4.5. Código 1 – Adicionar ao carrinho de compras.
# 4.6. Código 0 – Voltar.
# Se o cliente digitar a opção 2, o sistema deve apresentar os serviços disponíveis:
# 5.1. Código 201 - Troca de pneu - R$ 55,99.
# 5.2. Código 202 - Lavagem completa -R$ 12,99.
# 5.3. Código 203 - Freio - R$ 10,99.
# 5.4. Código 1 – Adicionar ao carrinho de compras.
# 5.5. Código 0 – Voltar.
# Se o cliente digitar a opção 3, o sistema deve listar o nome e o valor dos produtos incluídos no carrinho de compras. 
# Se o cliente digitar a opção 4, o sistema deve perguntar a forma de pagamento (dinheiro ou cartão). No dinheiro, o sistema deve calcular 10% de desconto do valor final. Observação: no autoatendimento, o cliente consegue adicionar no máximo 3 produtos/serviços em seu carrinho de compras. Se ele atingir esse número, o sistema deve apresentar a mensagem informando que o seu carrinho de compras já está cheio.
# Funcionamento geral do sistema
# - O sistema deve validar todas as entradas do teclado, quando possível;
# - O sistema deve ficar rodando até que seja a opção 0 no menu principal;
# - O sistema deve apresentar a quantidade de vendas e o valor total das vendas do dia ao ser finalizado.

# Funções
def despedidas(nome: str) -> None:
    print(f"Tchau, {nome}! Volte sempre!")


def adiciona_produto(produto: str, valor: float) -> None:
    if carrinho_de_compras.get(produto):
        print("Esse produto já foi adicionado no carrinho de compras. \nPor favor, selecione outro item.")
    else:
        carrinho_de_compras[produto] = valor
        print("Você adicionou o produto no carrinho com sucesso!")


def confirma_pagamento(forma: str) -> None:
    print(f"Valor final: R${valor}")

    continuar_pagamento = input("Tem certeza que deseja continuar? [S/N]: ").upper().strip()
    while continuar_pagamento not in ["S", "N"]:
        print("Por favor, certifique-se de colocar o valor S ou N.")
        continuar_pagamento = input("Tem certeza que deseja continuar? [S/N]: ").upper().strip()

    if continuar_pagamento == "S":
        print(f"Você realizou a compra em {forma} com sucesso!")
        despedidas(nome)

        continuar = False
        return continuar
    else:
        print("Você cancelou a compra.")

# Parte principal
print("---- Bem-vindo ao autoatendimento da bicicletaria XPTO Bikes ----")
nome = input("Digite o seu nome: ")
carrinho_de_compras = {}
continuar = True

while continuar:
    print("\n\n\n")

    # Menu
    print("----------  M  E  N  U  ----------")
    print("Opção 1 - Ver promoções")
    print("Opção 2 - Solicitar serviço de manutenção")
    print("Opção 3 - Listar carrinho de compra")
    print("Opção 4 - Finalizar carrinho de compra")
    print("Opção 0 - Sair")

    if len(carrinho_de_compras.keys()) == 3:
        print("Você atingiu o limite de compras do carrinho. O seu carrinho está cheio.")

    opcao = int(input("Digite sua opção desejada [1 | 2 | 3 | 4 | 0]: "))
    valor = sum(carrinho_de_compras.values())

    if len(carrinho_de_compras.keys()) == 3 and opcao in range(1, 3):
        print("Seu carrinho está cheio. Você só pode escolher entre as opções 3, 4 ou 0.")
    else:
        if opcao == 1:
            print("P  R  O  M  O  Ç  Õ  E  S")
            print("Código 101 - Bicicleta nova na cor amarela, aro 26, com 18 marchas e na promoção pelo preço de R$ 999,99")
            print("Código 102 - Bicicleta usada na cor azul, aro 26, com 18 marchas e com o valor promocional de R$ 400,00")
            print("Código 103 - Capacete de proteção por R$59,99")
            print("Código 104 - Freio a disco por R$ 89,99")
            print("Código 0 - Voltar")

            # Pede código
            codigo = int(input("Insira um código [101 | 102 | 103 | 104 | 0]: "))
            while codigo not in [0, 101, 102, 103]:
                print("Certifique de que você inseriu o código correto.")
                codigo = int(input("Insira um código [101 | 102 | 103 | 104 | 0]: "))

            if codigo == 101:
                adiciona_produto("Bicicleta NOVA Amarela, Aro 26, 18 marchas", 999.99)
            elif codigo == 102:
                adiciona_produto("Bicicleta USADA Azul, Aro 26, 18 marchas", 400.00)
            elif codigo == 103:
                adiciona_produto("Capacete de proteção", 89.99)
            elif codigo == 0:
                pass
        elif opcao == 2:
            print("S E R V I Ç O  DE  M A N U T E N Ç Ã O")
            print("Código 201 - Troca de pneu - R$ 55,99")
            print("Código 202 - Lavagem completa - R$ 12,99")
            print("Código 203 - Freio - R$ 10,99")
            print("Código 0 - Voltar")

            codigo = int(input("Insira um código [201 | 202 | 203 | 0]: "))
            while codigo not in [0, 201, 202, 203]:
                print("Certifique de que você inseriu o código correto.")
                codigo = int(input("Insira um código [201 | 202 | 203 | 0 | 0]: "))

            if codigo == 201:
                adiciona_produto("Troca de pneu", 55.99)
            elif codigo == 202:
                adiciona_produto("Lavagem completa", 12.99)
            elif codigo == 203:
                adiciona_produto("Freio", 10.99)
            elif codigo == 0:
                pass
        elif opcao == 3:
            print("C A R R I N H O  DE  C O M P R A")
            for produto, valor in carrinho_de_compras.items():
                print(produto, valor)

            print(f"Valor total até o momento: R${valor}")
        elif opcao == 4:
            print("F O R M A  DE  P A G A M E N T O")
            print("Código 401 - Dinheiro")
            print("Código 402 - Cartão")
            print("Código 0 - Voltar")

            codigo = int(input("Insira um código [401 | 402 | 0]: "))
            while codigo not in [0, 401, 402]:
                print("Certifique de que você inseriu o código correto.")
                codigo = int(input("Insira um código [401 | 402 | 0]: "))

            if codigo == 401:
                valor = valor - (valor * 0.10)  # 10% de desconto do valor final
                if not confirma_pagamento("dinheiro"):
                    break
            elif codigo == 402:
                if not confirma_pagamento("cartão"):
                    break
            elif codigo == 0:
                pass
        elif opcao == 0:
            despedidas(nome)
            break
