# ex162: Classe Astronauta: nome, missao, experiencia, com métodos de apresentar(), explorar() e descansar()
class Astronauta:
    def __init__(self, nome, missao, experiencia):
        self.nome = nome
        self.missao = missao
        self.experiencia = experiencia

    def apresentar(self):
        print(f"Conheça {self.nome}! Está/Já esteve presente na missão {self.missao} e tem {self.experiencia} anos de experiência.")

    def explorar(self):
        print(f"{self.nome} está explorando a missão {self.missao}.")

    def descansar(self):
        print(f"{self.nome} está cansado de explorar, foi descansar.")

if __name__ == "__main__":
    neil_armstrong = Astronauta("Neil Armstrong", "Apollo 11", 27)
    neil_armstrong.apresentar()
    neil_armstrong.explorar()
    neil_armstrong.descansar()
