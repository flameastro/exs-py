# ex288: Implemente a classe Funcionário. Deve haver como parâmetro nome e salário, e métodos de ver_salario, ajuste_salarial, trocar_emprego, hora_lanche.
class Funcionario:
    def __init__(self, nome: str, salario: float, saldo: float, emprego: str):
        self.nome = nome
        self.salario = salario
        self.saldo = saldo
        self.emprego = emprego

    def ver_saldo(self):
        print(f"Seu saldo é de {self.saldo}")

    def trocar_emprego(self, emprego: str, acao: str):
        self.emprego = emprego
        print(f"Seu novo emprego é {self.emprego} e você {acao}")

    def hora_lanche(self, comida: str):
        print(f"Comendo {comida}")

    def ajuste_salarial(self, aumento: bool, porcentagem: int):
        if aumento:
            self.salario += (self.salario * porcentagem) / 100
            print(f"Seu novo salário com o aumento é {self.salario}")
        else:
            self.salario -= (self.salario * porcentagem) / 100
            print(f"Seu novo salário com a diminuição é {self.salario}")


if __name__ == "__main__":
    programador = Funcionario("Carlos", 7600.45, 675853.57, "Programador")
    programador.ver_saldo()  # Seu saldo é de 675853.57
    programador.ajuste_salarial(True, 3)  # Seu novo salário com o aumento é 7828.4635
    programador.hora_lanche("Arroz e Feijão com Ovo e Carne")  # Comendo Arroz e Feijão com Ovo e Carne

    medico = Funcionario("Felipe", 23985.59, 2457894.34, "Médico")
    medico.ajuste_salarial(True, 2)  # Seu novo salário com o aumento é 24465.3018
    medico.hora_lanche("Arroz com Frango e Salada")  # Comendo Arroz com Frango e Salada
    medico.trocar_emprego("Taxista", "Dirige Carros")  # Seu novo emprego é Taxista e você Dirige Carros
    medico.ajuste_salarial(False, 90)  # Seu novo salário com a diminuição é 2446.5301800000016
