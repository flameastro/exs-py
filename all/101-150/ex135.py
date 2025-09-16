# ex135: Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

def calcula_media2(notaA: float, notaB: float, notaC: float) -> float:
    pesoA = 2
    pesoB = 3
    pesoC = 5

    media = (notaA * pesoA + notaB * pesoB + notaC * pesoC) / (pesoA + pesoB + pesoC)
    return f"MEDIA = {media:.1f}"


if __name__ == "__main__":
    print(calcula_media2(5.0, 6.0, 7.0))  # MEDIA = 6.3
    print(calcula_media2(3.7, 3.7, 9.3))  # MEDIA = 6.5
    print(calcula_media2(1.5, 3.9, 10.0))  # MEDIA = 6.5
