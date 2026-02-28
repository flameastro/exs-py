# ex013: Implemente a classe Funcionário. Um empregado tem um nome (um string) e um salário(um float). Escreva um construtor com dois parâmetros (nome e salário) e métodos para devolver nome e salário. Escreva um pequeno programa que teste sua classe.
class Funcionario:
    def __init__(self, nome: str, salario: float):
        self.nome = nome
        self.salario = salario

    def exibir_informacoes(self):
        return self.nome, self.salario
