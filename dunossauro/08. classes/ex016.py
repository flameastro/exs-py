# ex016: Crie uma "porta escondida" no programa do programa do bichinho virtual que mostre os valores exatos dos atributos do objeto. Consiga isto mostrando o objeto quando uma opção secreta, não listada no menu, for informada na escolha do usuário.
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

    while True:
        print("\n1 - Comer\n2 - Brincar\n3 - Alterar Nome\n4 - Ver Status\n0 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            quantidade = int(input("Quantidade de comida: "))
            print(t1.comer(quantidade))
        elif escolha == "2":
            tempo = int(input("Tempo de brincadeira: "))
            print(t1.brincar(tempo))
        elif escolha == "3":
            novo_nome = input("Novo nome: ")
            print(t1.alterar_nome(novo_nome))
        elif escolha == "4":
            print(t1.exibir_informacoes())
        elif escolha == "0":
            break
        elif escolha.lower() == "xyz123":  # opção secreta
            print(vars(t1))
        else:
            print("Opção inválida.")
