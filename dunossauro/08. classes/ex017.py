# ex017: Crie uma fazenda de bichinhos instanciando vários objetos bichinho e mantendo o controle deles através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigis que o usuário tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos).

# Para tornar o programa mais interessante, dê para cada bichinho um nivel inicial aleatório de fome e tédio.
import random

class Tamagushi:
    def __init__(self, nome: str):
        self.nome = nome
        self.fome = random.randint(20, 80)
        self.tedio = random.randint(20, 80)
        self.idade = random.randint(1, 5)

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
    nomes = ["João", "Goku", "Mimi", "Luna", "Thor"]
    fazenda = [Tamagushi(nome) for nome in nomes]

    while True:
        print("\n1 - Alimentar todos\n2 - Brincar com todos\n3 - Ver status de todos\n0 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            quantidade = int(input("Quantidade de comida para cada bichinho: "))
            for bicho in fazenda:
                print(bicho.comer(quantidade))
        elif escolha == "2":
            tempo = int(input("Tempo de brincadeira para cada bichinho: "))
            for bicho in fazenda:
                print(bicho.brincar(tempo))
        elif escolha == "3":
            for bicho in fazenda:
                print(bicho.exibir_informacoes())
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")
