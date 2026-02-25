# ex011: Implemente uma classe chamada Carro com as seguintes propriedades:

# Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
# O consumo é especificado no construtor e o nível de combustível inicial é 0.
# Forneça um método andar() que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
# Forneça um método obter_gasolina(), que retorna o nível atual de combustível.
# Forneça um método adicionar_gasolina(), para abastecer o tanque.
# Exemplo de uso:

# meu_fusca = Carro(15)             # 15 quilômetros por litro de combustível. 
# meu_fusca.adicionar_gasolina(20)  # abastece com 20 litros de combustível. 
# meu_fusca.andar(100)              # anda 100 quilômetros.
# meu_fusca.obter_gasolina()         # Imprime o combustível que resta no tanque.
class Carro:
    def __init__(self, consumo):
        self.consumo = consumo  # km por litro
        self.combustivel = 0    # tanque começa vazio

    def adicionar_gasolina(self, litros):
        self.combustivel += litros
        print(f"Abastecido com {litros} litros. Combustível atual: {self.combustivel:.2f} L")

    def andar(self, distancia):
        litros_necessarios = distancia / self.consumo

        if litros_necessarios > self.combustivel:
            print("⛽ Combustível insuficiente para percorrer essa distância!")
        else:
            self.combustivel -= litros_necessarios
            print(f"O carro andou {distancia} km e consumiu {litros_necessarios:.2f} L.")
            print(f"Combustível restante: {self.combustivel:.2f} L")

    def obter_gasolina(self):
        print(f"Nível atual de combustível: {self.combustivel:.2f} L")
        return self.combustivel
