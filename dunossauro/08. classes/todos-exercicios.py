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


# ex004: # Crie uma classe que receba como parâmetros nome, idade, peso e altura, e tem os métodos fazer_aniversario, comer, andar, fazer_hobby, sair, acessar_internet, comprar
from time import sleep


class Pessoa:
    def __init__(self, nome: str, idade: int, peso: float, altura: float):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def fazer_aniversario(self) -> None:
        self.idade += 1
        print(f"Oba!! Feliz aniversário, {self.nome}!")
        print("Sopre a vela!")
        print("Assoprando a vela.", end="")
        sleep(2)
        print(".", end="")
        sleep(2)
        print(".")

        input("Deseje algo: ")
        print("Seu desejo irá se cumprir!")

    def comer(self, comida: str) -> None:
        print(f"Comendo {comida}...")
        input("Qual sua opnião sobre a comida? Gostou? ")

    def andar(self, metros: int) -> None:
        print(f"A partir de agora, começando a andar {metros} metros.")

    def fazer_hobby(self, hobby: str) -> None:
        print(f"Agora, estou {hobby}!!")

    def sair(self, lugar: str) -> None:
        print(f"Saindo para {lugar}...")

    def acessar_internet(self, website: str) -> None:
        print(f"Acessando o site {website}...")
        input(f"Qual sua opnião sobre o site {website}? ")

    def comprar(self, produto: str, quantidade: int, preco: float) -> None:
        print(f"Informações sobre sua compra\nProduto: {produto}\nQuantidade: {quantidade}\nPreço de Cada Produto: {preco}")


if __name__ == "__main__":
    pessoa1 = Pessoa("Gustavo", 15, 67.45, 1.69)
    pessoa1.comer("Panqueca")  # Comendo Panqueca...
    pessoa1.sair("Parque")  # Saindo para Parque...
    pessoa1.acessar_internet("https://www.mercadolivre.com.br/")  # Acessando o site https://www.mercadolivre.com.br/...
    pessoa1.comprar("Smart TV Samsung 4K", 1, 4569.99)  # Informações sobre sua compra    Produto: Smart TV Samsung 4K    Quantidade: 1    Preço de Cada Produto: 4569.99

    pessoa2 = Pessoa("Maria", 24, 61.80, 1.67)
    pessoa2.comer("Macarrão e Feijão")  # Comendo Macarrão e Feijão...
    pessoa2.acessar_internet("https://www.youtube.com/")  # Acessando o site https://www.youtube.com/...
    pessoa2.fazer_aniversario()


# ex005: Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
class ContaCorrente:
    def __init__(self, numero: int, nome: str, saldo: float = 0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self, novo_nome: str):
        self.nome = novo_nome
        return "Nome alterado com sucesso."

    def realizar_deposito(self, valor: float):
        if valor > 0:
            self.saldo += valor
            return "Depósito realizado com sucesso!"

        return "O depósito não pode ter sido efetuado. Modifique o valor e tente novamente."

    def realizar_saque(self, valor: float):
        if valor > 0 and self.saldo >= valor:
            self.saldo -= valor
            return "Saque efetuado com sucesso!"

        return "O saque não pode ter sido efetuado. Modifique o valor e tente novamente."

    def ver_saldo(self):
        return self.saldo


if __name__ == "__main__":
    cc1 = ContaCorrente(87467, "Gustavo Pinheiro", 34653.79)
    print(cc1.realizar_deposito(4500))  # Depósito realizado com sucesso!
    print(cc1.ver_saldo())  # 39153.79

    cc2 = ContaCorrente(9483, "Maria Peixoto", 76554.67)
    print(cc2.realizar_saque(50000))  # Saque efetuado com sucesso!
    print(cc2.ver_saldo())  # 26554.67
