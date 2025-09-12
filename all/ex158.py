# ex158: Crie uma classe Gato com atributos nome e cor, e um método miar().
class Gato:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def miar(self):
        print(f"{self.nome} miou: miauuuu 🐱!")


if __name__ == "__main__":
    patrick = Gato("Patrick", "Cinza Claro")
    patrick.miar()
