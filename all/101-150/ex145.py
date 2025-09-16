# ex145: Crie uma classe Lampada com métodos ligar() e desligar().
class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada

    def ligar(self):
        if self.ligada:
            print("A lâmpada já está ligada.")
        else:
            print("A lâmpada ligou.")
            self.ligada = True

    def desligar(self):
        if not self.ligada:
            print("A lâmpada já está desligada.")
        else:
            print("A lâmpada desligou.")
            self.ligada = False


if __name__ == "__main__":
    lampada = Lampada(True)
    lampada.ligar()  # A lâmpada já está ligada.
    lampada.desligar()  # A lâmpada desligou.
    lampada.desligar()  #  A lâmpada já está desligada.
    lampada.ligar()  # A lâmpada ligou.
    lampada.desligar()  # A lâmpada desligou.
