# ex140: Crie uma classe Carro com atributos marca e ano, e um método para exibir informações.
class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def exibir_informacoes(self):
        return f"O carro é da marca {self.marca} do ano {self.ano}"


if __name__ == "__main__":
    carro1 = Carro("Fiat", 2006)
    print(carro1.exibir_informacoes())  # O carro é da marca Fiat do ano 2006

    carro2 = Carro("Civic", 2015)
    print(carro2.exibir_informacoes())  # O carro é da marca Civic do ano 2015

    carro3 = Carro("Ferrari", 2021)
    print(carro3.exibir_informacoes())  # O carro é da marca Ferrari do ano 2021
