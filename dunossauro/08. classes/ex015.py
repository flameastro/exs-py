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
