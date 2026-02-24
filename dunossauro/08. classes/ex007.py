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
