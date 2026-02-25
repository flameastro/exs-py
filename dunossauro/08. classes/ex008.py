# ex008: Desenvolva uma classe Macaco, que possua os atributos nome e pelo menos os métodos comer(), ver_bucho() e fazer_som().
import random

class Macaco:
    def __init__(self, apelido: str):
        self.apelido = apelido

    def comer(self, comida: str = "Banana"):
        print(f"O macaco está comendo {comida}")

    def ver_bucho(self):
        print("Uauu! Que Buchão!")

    def fazer_som(self):
        som = ""

        for i in range(random.randint(8, 21)):
            numero = random.randint(1, 2)
            if numero == 1:
                som += "A"
            else:
                som += "U"

        print(f"O/A {self.apelido} disse: {som}!")


if __name__ == "__main__":
    macaco1 = Macaco("Tommy")
    macaco1.comer()  # O macaco está comendo Banana
    macaco1.fazer_som()  # O/A Tommy disse: UAUAUUUAUAUUAAUUUU!

    macaco2 = Macaco("Manster")
    macaco2.comer()  # O macaco está comendo Banana
    macaco2.ver_bucho()  # Uauu! Que Buchão!
    macaco2.fazer_som()  # O/A Manster disse: UUUAAAAA!
    macaco2.fazer_som()  # O/A Manster disse: UUUUAAUUUUUUAUA!
