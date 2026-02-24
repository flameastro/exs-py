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
