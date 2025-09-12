# ex049: Crie uma função que retorne o número de pontos baseado na vitória, no empate e na derrota de um time de futebol. Sabendo que: vitória = 3 pontos, empate = 1 ponto e derrota = 0 pontos
def retorna_numero_pontos(vitoria, empate, derrota):
    pontos_vitoria = vitoria * 3
    pontos_empate = empate * 1
    pontos_derrota = 0

    total = pontos_vitoria + pontos_empate + pontos_derrota
    return f"Os pontos totais são de {total}"


if __name__ == "__main__":
    print(retorna_numero_pontos(15, 2, 5))  # Os pontos totais são de 47
    print(retorna_numero_pontos(23, 12, 8))  # Os pontos totais são de 81
    print(retorna_numero_pontos(3, 3, 54))  # Os pontos totais são de 12
