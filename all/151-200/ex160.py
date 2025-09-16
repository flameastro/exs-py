# ex160: Classe Academia: parâmetros -> nome, endereco, equipamentos; Funções -> abrir, fechar
class Academia:
    def __init__(self, nome, endereco, equipamentos):
        self.nome = nome
        self.endereco = endereco
        self.equipamentos = equipamentos
        self.aberto = False

    def sobre(self):
        print(f"Seja bem vindo(a) ao {self.nome} localizado em {self.endereco}! Aqui temos equipamentos como {", ".join(self.equipamentos)}!")
        if self.aberto:
            print("Neste momento estamos abertos, esperando por você!")
        else:
            print("A academia está fechada agora. Volte mais tarde, esperamos por você!")

    def usar_academia(self, equipamento):
        if self.aberto:
            print(f"Bora crescer com tudo com {equipamento}!")
        else:
            print("Não é possível usar a academia quando está fechada!")

    def abrir(self):
        if self.aberto:
            print("A academia já está aberta.")
        else:
            self.aberto = True
            print("Academia abriu, venha nos visitar!")

    def fechar(self):
        if self.aberto:
            print("Estamos fechando, volte amanhã mais cedo.")
            self.aberto = False
        else:
            print("A academia já está fechada.")

    def status(self):
        if self.aberto:
            print("A academia está aberta.")
        else:
            print("A academia está fechada.")


if __name__ == "__main__":
    muscle_grow = Academia("MuscleGrow", "Rua Fransisco Ladelmir 778", ["...", "...", "..."])
    muscle_grow.status()
    muscle_grow.sobre()
    muscle_grow.abrir()
    muscle_grow.usar_academia("Supino")
    muscle_grow.fechar()
