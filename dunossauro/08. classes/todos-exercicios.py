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


# ex006: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
class Televisao:
    def __init__(self, canal: str = None, volume: int = 0):
        self.canal = canal
        self.volume = volume

    def aumentar_volume(self, valor: int):
        if valor > 0 and valor <= 100 and self.volume+valor <= 100:
            self.volume += valor
            return "Volume aumentado com sucesso."

        return "Não foi possível aumentar o volume, verifique as informações."

    def diminuir_volume(self, valor: int):
        if valor > 0 and valor <= 100 and self.volume-valor >= 0 and self:
            self.volume -= valor
            return "Volume diminuido com sucesso."

        return "Não foi possível diminuir o volume, verifique as informações."

    def exibir_valor_volume(self):
        return self.volume

    def alterar_canal(self, canal: str):
        return f"Alterando para o canal {canal}."


if __name__ == "__main__":
    t1 = Televisao("Programa do Ratinho", 12)
    print(t1.aumentar_volume(3))  # Volume aumentado com sucesso.
    print(t1.exibir_valor_volume())  # 15
    print(t1.diminuir_volume(16))  # Não foi possível diminuir o volume, verifique as informações.
    print(t1.exibir_valor_volume())  # 15
    print(t1.alterar_canal("Programa do Silvio Santos"))  # Alterando para o canal Programa do Silvio Santos.
    print(t1.diminuir_volume(6))  # Volume diminuido com sucesso.
    print(t1.exibir_valor_volume())  # 9


# ex007: Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
# Atributos: Nome, Fome, Saúde e Idade.
# Métodos: Alterar Nome, Comer; Retornar Nome, Fome, Saúde e Idade
# Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento.
class Tamagushi:
    def __init__(self, nome: str, fome: bool, saude: bool, idade: int):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, nome: str):
        if self.nome != nome:
            return "Nome alterado com sucesso!"

        return "O Tamagushi já possui esse nome."

    def comer(self, comida: str):
        if not self.saude:
            self.salde = True

        return f"O Tamagushi está comendo {comida}."

    def exibir_informacoes(self):
        return self.nome, self.fome, self.saude, self.idade


if __name__ == "__main__":
    t1 = Tamagushi("João", True, False, 1)
    print(t1.comer("Feijão"))  # O Tamagushi está comendo Feijão.
    print(t1.comer("Repolho"))  # O Tamagushi está comendo Repolho.
    print(t1.alterar_nome("Goku"))  # O Tamagushi está comendo Feijão.
    print(t1.exibir_informacoes())  # ('João', True, False, 1)


# ex008: Desenvolva uma classe Macaco, que possua os atributos nome e pelo menos os métodos comer(), ver_bucho() e fazer_som().
import random

class Macaco:
    def __init__(self, apelido: str):
        self.apelido = apelido

    def comer(self, comida: str = "Banana"):
        print(f"O macaco está comendo {comida}")

    def ver_bucho(self):
        print("Uauu! Que Buchão!")

    def fazer_som(self):
        som = ""

        for i in range(random.randint(8, 21)):
            numero = random.randint(1, 2)
            if numero == 1:
                som += "A"
            else:
                som += "U"

        print(f"O/A {self.apelido} disse: {som}!")


if __name__ == "__main__":
    macaco1 = Macaco("Tommy")
    macaco1.comer()  # O macaco está comendo Banana
    macaco1.fazer_som()  # O/A Tommy disse: UAUAUUUAUAUUAAUUUU!

    macaco2 = Macaco("Manster")
    macaco2.comer()  # O macaco está comendo Banana
    macaco2.ver_bucho()  # Uauu! Que Buchão!
    macaco2.fazer_som()  # O/A Manster disse: UUUAAAAA!
    macaco2.fazer_som()  # O/A Manster disse: UUUUAAUUUUUUAUA!
