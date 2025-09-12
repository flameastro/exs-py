# ex163: Classe Calculadora básica que realiza as 4 operações básicas
class Calculadora:
    def __init__(self):
        pass

    def adicao(self, a, b):
        print(a + b)

    def subtracao(self, a, b):
        print(a - b)

    def multiplicacao(self, a, b):
        print(a * b)

    def divisao(self, a, b):
        print(a / b)


if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.adicao(12, 6)  # 18
    calculadora.multiplicacao(70, 4)  # 280
    calculadora.divisao(48, 4)  # 12.0
    calculadora.subtracao(900, 1800)  # -900
