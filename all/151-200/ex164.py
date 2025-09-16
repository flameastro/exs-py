# ex164: Classe Chat com parâmetros -> remetente, destinatario; métodos -> enviar_mensagem()
class Chat:
    def __init__(self, remetente, destinatario):
        self.remetente = remetente
        self.destinatario = destinatario

    def enviar_mensagem(self, mensagem):
        print(f"{self.remetente}: {mensagem}")


if __name__ == "__main__":
    mateus = Chat("Mateus", "Felipe")
    felipe = Chat("Felipe", "Mateus")

    mateus.enviar_mensagem("Oi, Felipe!")
    felipe.enviar_mensagem("Oi, Mateus! Que tal jogar bola?")
    felipe.enviar_mensagem("Mas precisa ser rápido, tenho que voltar logo.")
    mateus.enviar_mensagem("Eu topo, Felipe!")
    felipe.enviar_mensagem("Ok, vamos no parque, te encontro lá!")
    mateus.enviar_mensagem("Tô indo.")
