# ex010: Faça um programa completo utilizando classes e métodos que:

# Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:

# tipo_combustivel
# valor_litro
# quantidade_combustivel
# Possua no mínimo esses métodos:

# abastecer_por_valor(): método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
# abastecer_por_litro(): método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
# alterar_valor(): altera o valor do litro do combustível.
# alterar_combustivel(): altera o tipo do combustível.
# alterar_quantidade_combustivel(): altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
class BombaCombustivel:
    def __init__(self, tipo_combustivel: str, valor_litro: float, quantidade_combustivel: float):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor: float):
        litros = valor / self.valor_litro
        if litros > self.quantidade_combustivel:
            print("⛽ Erro: combustível insuficiente na bomba.")
            return
        self.quantidade_combustivel -= litros
        print(f"Abastecidos {litros:.2f} litros de {self.tipo_combustivel}.")
        print(f"Quantidade restante na bomba: {self.quantidade_combustivel:.2f} litros.")

    def abastecer_por_litro(self, litros: float):
        if litros > self.quantidade_combustivel:
            print("⛽ Erro: combustível insuficiente na bomba.")
            return
        valor = litros * self.valor_litro
        self.quantidade_combustivel -= litros
        print(f"Valor a pagar: R${valor:.2f}")
        print(f"Quantidade restante na bomba: {self.quantidade_combustivel:.2f} litros.")

    def alterar_valor(self, novo_valor: float):
        self.valor_litro = novo_valor
        print(f"Novo valor do litro: R${self.valor_litro:.2f}")

    def alterar_combustivel(self, novo_tipo: str):
        self.tipo_combustivel = novo_tipo
        print(f"Novo tipo de combustível: {self.tipo_combustivel}")

    def alterar_quantidade_combustivel(self, nova_qtd: float):
        self.quantidade_combustivel = nova_qtd
        print(f"Nova quantidade de combustível na bomba: {self.quantidade_combustivel:.2f} litros")
