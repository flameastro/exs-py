# ex001: Crie uma classe que modele uma bola:
# Atributos: cor, circunferência, material
# Métodos: troca_cor e mostra_cor
class Bola:
    def __init__(self, cor: str, circunferencia: float):
        self.cor = cor
        self.circunferencia = circunferencia

    def trocar_cor(self, cor: str) -> None:
        print(f"Trocadondo de cor de {self.cor} para {cor}...")
        self.cor = cor


    def mostrar_cor(self):
        print(f"A cor da bola é {self.cor}")


if __name__ == "__main__":
    bola1 = Bola("Azul", 3.14)
    bola1.trocar_cor("Vermelho")
    bola1.mostrar_cor()  # A cor da bola é Vermelho


# ex002: Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
class Quadrado:
    def __init__(self, tamanho_lado: float):
        self.tamanho_lado = tamanho_lado

    def alterar_valor_lado(self, valor):
        self.tamanho_lado = valor
        return "Tamanho do lado alterado com sucesso."

    def retornar_valor_lado(self):
        return self.tamanho_lado

    def calcular_area(self):
        return self.tamanho_lado * self.tamanho_lado


if __name__ == "__main__":
    q1 = Quadrado(12.5)
    print(q1.calcular_area())  # 156.25
    print(q1.alterar_valor_lado(21.4))  # Tamanho do lado alterado com sucesso.
    print(q1.calcular_area())  # 457.9599999999999


# ex003: Crie uma classe que modele um retângulo:
# Atributos: Lado_a, Lado_b (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
class Retangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def alterar_valor(self, valor_base: float, valor_altura: float):
        self.base = valor_base
        self.altura = valor_altura

    def retornar_valor(self):
        return self.base, self.altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (self.base + self.altura) * 2

if __name__ == "__main__":
    r1 = Retangulo(12.4, 25.4)
    print(r1.alterar_valor(26.5, 12.3))
    print(r1.calcular_area())  # 325.95000000000005
    print(r1.calcular_perimetro())  # 77.6

    r2 = Retangulo(23.4, 12.3)
    print(r2.calcular_area())  # 287.82
    print(r2.calcular_perimetro())  # 71.4
