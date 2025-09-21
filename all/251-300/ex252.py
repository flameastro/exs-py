# ex252: Crie uma função que receba uma hora do dia como parâmetro e retorne a seção do dia por extenso
def mensagem(hora: int):
    return "Bom dia!" if hora >= 6 and hora <= 11 else "Boa tarde!" if hora >= 12 and hora <= 17 else "Boa noite!" if hora >= 18 and hora <= 23 else "Hora de dormir!" if hora == 24 or hora >= 0 and hora <= 5 else "Hora inválida."


if __name__ == "__main__":
    print(mensagem(1))  # Hora de dormir!
    print(mensagem(62))  # Hora inválida.
    print(mensagem(24))  # Hora de dormir!
    print(mensagem(12))  # Boa tarde!
    print(mensagem(7))  # Bom dia!
    print(mensagem(17))  # Boa tarde!
