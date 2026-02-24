# ex006: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas.
class Televisao:
    def __init__(self, canal: str = None, volume: int = 0):
        self.canal = canal
        self.volume = volume

    def aumentar_volume(self, valor: int):
        if valor > 0 and valor <= 100 and self.volume+valor <= 100:
            self.volume += valor
            return "Volume aumentado com sucesso."

        return "Não foi possível aumentar o volume, verifique as informações."

    def diminuir_volume(self, valor: int):
        if valor > 0 and valor <= 100 and self.volume-valor >= 0 and self:
            self.volume -= valor
            return "Volume diminuido com sucesso."

        return "Não foi possível diminuir o volume, verifique as informações."

    def exibir_valor_volume(self):
        return self.volume

    def alterar_canal(self, canal: str):
        return f"Alterando para o canal {canal}."


if __name__ == "__main__":
    t1 = Televisao("Programa do Ratinho", 12)
    print(t1.aumentar_volume(3))  # Volume aumentado com sucesso.
    print(t1.exibir_valor_volume())  # 15
    print(t1.diminuir_volume(16))  # Não foi possível diminuir o volume, verifique as informações.
    print(t1.exibir_valor_volume())  # 15
    print(t1.alterar_canal("Programa do Silvio Santos"))  # Alterando para o canal Programa do Silvio Santos.
    print(t1.diminuir_volume(6))  # Volume diminuido com sucesso.
    print(t1.exibir_valor_volume())  # 9
