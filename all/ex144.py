# ex144: Crie uma classe TV com atributos canal e volume, e métodos mudar_canal() e ajustar_volume().
class TV:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def mudar_canal(self, novo_canal):
        print(f"Mudando de {self.canal} para {novo_canal}")

    def ajustar_volume(self, novo_volume):
        print(f"Ajustando volume de {self.volume} para {novo_volume}")


if __name__ == "__main__":
    tv = TV("Show do Milhão", 12)
    tv.mudar_canal("Silvio Santos")  # Mudando de Show do Milhão para Silvio Santos
    tv.ajustar_volume(18)  # Ajustando volume de 12 para 18
