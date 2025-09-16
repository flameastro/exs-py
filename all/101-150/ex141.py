# ex141: Crie uma classe Pessoa com atributos nome e idade, e um método para dizer a idade.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_idade(self):
        return f"{self.nome} tem {self.idade} anos."


if __name__ == "__main__":
    pessoa1 = Pessoa("Lucas", 45)
    print(pessoa1.exibir_idade())  # Lucas tem 45 anos.

    pessoa2 = Pessoa("Maria", 21)
    print(pessoa2.exibir_idade())  # Maria tem 21 anos.

    pessoa3 = Pessoa("Felipe", 15)
    print(pessoa3.exibir_idade())  # Felipe tem 15 anos.

