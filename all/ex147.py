# ex147: Crie uma classe Cachorro com atributos nome e raça, e um método latir().
class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        print(f"{self.nome} da raça {self.raca} latiu: au au au 🐶!")

if __name__ == "__main__":
    snoopy = Cachorro("Snoopy", "BullDog")
    snoopy.latir()  # Snoopy da raça BullDog latiu: au au au 🐶!
