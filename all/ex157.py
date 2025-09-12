# ex157: Crie uma classe Funcionario com atributos nome, cargo e salário, salario, com método de trabalhar()
class Funcionario:
    def __init__(self, nome, cargo, salario, saldo):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.saldo = saldo

    def trabalhar(self, horas):
        bonus = 15 * horas
        self.saldo += bonus
        print(f"Trabalhando...")
        print(f"Olha, você ganhou +R${bonus} de saldo!")


if __name__ == "__main__":
    funcionario1 = Funcionario("João", "Desenvolvedor de Sistemas", 1350, 2750)
    funcionario1.trabalhar(1)
