# ex009: Faça um programa completo utilizando funções e classes que:
# Possua uma classe chamada Ponto, com os atributos x e y.
# Possua uma classe chamada Retangulo, com os atributos largura e altura.
# Possua uma função para imprimir os valores da classe Ponto
# Possua uma função para encontrar o centro de um Retângulo.
# A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores de x e y para o centro do objeto.
# O valor do centro do objeto deve ser mostrado na tela
class Ponto:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def exibir_valores(self):
        return self.x, self.y

class Retangulo:
    def __init__(self, largura: float, altura: float):
        self.largura = largura
        self.altura = altura

    def encontra_centro(self):
        return self.largura / 2, self.altura / 2


if __name__ == "__main__":
    p1 = Ponto(12, 5)
    print(p1.exibir_valores())  # (12, 5)

    r1 = Retangulo(12.5, 17)
    print(r1.encontra_centro())  # (6.25, 8.5)
