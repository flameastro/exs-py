# ex056: Crie uma função que simule a chance de ser impostor no Among Us. Considere a fórmula: (numero_impostores / quantidade_jogadores) * 100
def chance_impostor_AmongUs(impostores: int, jogadores: int):
    chance = round((impostores / jogadores) * 100)
    return f"A chance de você ser impostor é de {chance}%"


if __name__ == "__main__":
    print(chance_impostor_AmongUs(2, 16))  # A chance de você ser impostor é de 12%
    print(chance_impostor_AmongUs(1, 10))  # A chance de você ser impostor é de 10%
    print(chance_impostor_AmongUs(2, 5))  # A chance de você ser impostor é de 40%
