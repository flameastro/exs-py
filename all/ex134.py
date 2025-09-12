# ex134: Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

def calcula_media1(notaA: float, notaB: float) -> float:
    pesoA = 3.5
    pesoB = 7.5

    media = (notaA * pesoA + notaB * pesoB) / (pesoA + pesoB)
    return f"MEDIA = {media:.5f}"


if __name__ == "__main__":
    print(calcula_media1(5.0, 7.1))  # MEDIA = 6.43182
    print(calcula_media1(0.0, 7.1))  # MEDIA = 4.84091
    print(calcula_media1(10.0, 10.0))  # MEDIA = 4.84091
