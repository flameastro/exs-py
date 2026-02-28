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
