# ex006: Faça um programa que converta a notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M.
def converte_horario(horas, minutos):
    if (horas > 24 or horas < 0) or (minutos > 60 or minutos < 0):
        return "Insira um valor correto."

    if horas > 12:
        horas -= 12
        horario = f"{horas}:{minutos} P.M."
    else:
        horario = f"{horas}:{minutos} A.M."

    return horario


if __name__ == "__main__":
    print(converte_horario(14, 25))  # 2:25 P.M.
    print(converte_horario(25, 12))  # Insira um valor correto.
    print(converte_horario(5, 45))  # 5:45 A.M.
