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


# ex010: Faça um programa completo utilizando classes e métodos que:

# Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:

# tipo_combustivel
# valor_litro
# quantidade_combustivel
# Possua no mínimo esses métodos:

# abastecer_por_valor(): método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
# abastecer_por_litro(): método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
# alterar_valor(): altera o valor do litro do combustível.
# alterar_combustivel(): altera o tipo do combustível.
# alterar_quantidade_combustivel(): altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
class BombaCombustivel:
    def __init__(self, tipo_combustivel: str, valor_litro: float, quantidade_combustivel: float):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor: float):
        litros = valor / self.valor_litro
        if litros > self.quantidade_combustivel:
            print("⛽ Erro: combustível insuficiente na bomba.")
            return
        self.quantidade_combustivel -= litros
        print(f"Abastecidos {litros:.2f} litros de {self.tipo_combustivel}.")
        print(f"Quantidade restante na bomba: {self.quantidade_combustivel:.2f} litros.")

    def abastecer_por_litro(self, litros: float):
        if litros > self.quantidade_combustivel:
            print("⛽ Erro: combustível insuficiente na bomba.")
            return
        valor = litros * self.valor_litro
        self.quantidade_combustivel -= litros
        print(f"Valor a pagar: R${valor:.2f}")
        print(f"Quantidade restante na bomba: {self.quantidade_combustivel:.2f} litros.")

    def alterar_valor(self, novo_valor: float):
        self.valor_litro = novo_valor
        print(f"Novo valor do litro: R${self.valor_litro:.2f}")

    def alterar_combustivel(self, novo_tipo: str):
        self.tipo_combustivel = novo_tipo
        print(f"Novo tipo de combustível: {self.tipo_combustivel}")

    def alterar_quantidade_combustivel(self, nova_qtd: float):
        self.quantidade_combustivel = nova_qtd
        print(f"Nova quantidade de combustível na bomba: {self.quantidade_combustivel:.2f} litros")


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


# ex012: Faça uma classe ContaInvestimento que seja semelhante a classe ContaBancaria, com a diferença de que se adicione um atributo taxa_juros. Forneça um inicializador que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicione_juros() (sem parâmetro explícito) que adicione juros à conta.

# Escreva um programa que construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método adicione_juros() cinco vezes e imprime o saldo resultante.
class ContaInvestimento:
    def __init__(self, numero: int, nome: str, taxa_juros: float, saldo: float = 0):
        self.numero = numero
        self.nome = nome
        self.taxa_juros = taxa_juros
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

    def adicione_juros(self):
        self.saldo += self.saldo * self.taxa_juros
        print(f"Juros aplicados! Novo saldo: R${self.saldo:.2f}")


if __name__ == "__main__":
    poupanca = ContaInvestimento(1, "Poupança", 0.10, 1000.00)

    for _ in range(5):
        poupanca.adicione_juros()

    print(f"Saldo final após 5 aplicações de juros: R${poupanca.ver_saldo():.2f}")


# ex013: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um float). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.
class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def exibir_informacoes(self):
        return self.nome, self.salario


# ex014: Aprimore a classe do exercício anterior para adicionar o método aumentar_salario() (porcentual_de_aumento) que aumente o salário do funcionário em uma certa porcentagem.

# Exemplo de uso:

# harry = funcionário('Harry', 25000)
# harry.aumentar_salario(10)
class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def exibir_informacoes(self):
        return self.nome, self.salario

    def aumentar_salario(self, porcentagem: float):
        self.salario += (self.salario * porcentagem) / 100
        return self.salario

if __name__ == "__main__":
    harry = Funcionario('Harry', 25000)
    print(harry.aumentar_salario(10))  # 27500.0


# ex015: Melhore o programa do bichinho virtual, permitindo que o usuário especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho. Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.
class Tamagushi:
    def __init__(self, nome: str, fome: int, tedio: int, idade: int):
        self.nome = nome
        self.fome = fome
        self.tedio = tedio
        self.idade = idade

    def alterar_nome(self, novo_nome: str):
        if self.nome != novo_nome:
            self.nome = novo_nome
            return "Nome alterado com sucesso!"
        return "O Tamagushi já possui esse nome."

    def comer(self, quantidade: int):
        self.fome -= quantidade
        if self.fome < 0:
            self.fome = 0
        return f"{self.nome} comeu {quantidade} unidades de comida. Fome agora: {self.fome}"

    def brincar(self, tempo: int):
        self.tedio -= tempo
        if self.tedio < 0:
            self.tedio = 0
        return f"{self.nome} brincou por {tempo} minutos. Tédio agora: {self.tedio}"

    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Fome: {self.fome}, Tédio: {self.tedio}, Idade: {self.idade}"


if __name__ == "__main__":
    t1 = Tamagushi("João", fome=50, tedio=50, idade=1)
    print(t1.comer(20))
    print(t1.brincar(30))
    print(t1.alterar_nome("Goku"))
    print(t1.exibir_informacoes())
