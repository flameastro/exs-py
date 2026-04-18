# ex334: Idem ao anterior, porém só se sabe que a moeda falsa tem massa diferente. Para descobrir se ela é mais leve ou mais pesada que as outras, muda-se alguma coisa?
# Resposta (Antes do Pensamento): Sim, pois devemos medir todas as moedas. Se tivessem 5 moedas, teriamos que medir todas elas, porque se medissemos por exemplo, apenas 3, e coletassemos apenas valores iguais, não iriamos saber qual era a falsa. Então temos que medir todas as 5 uma por uma e depois realizar uma operação para saber qual a falsa
# Resposta (Após pensar um pouco): Na verdade, podemos iterar sobre cada moeda (Nesse caso, com a exceção do último elemento, porque nesse algoritmo, resultaria em um erro de índices). Verificamos se aquela moeda é igual a moeda da lista com o índice + 1. Se for, simplesmente ignoramos. Se não for, resta apenas duas opções: Verificamos se a moeda do índice atual é maior que a moeda do índice atual + 1. Se for, imprimimos a posição da moeda. Se não for, só pode ser que a moeda do índice + 1 seja maior que o índice atual.
# Obs: Esse algoritmo foi projetado especialmente para números pequenos, já que é feita uma avaliação entre apenas 5 números.
def posicao_moeda_falsa(moedas: list) -> str:
    for moeda in range(len(moedas)-1):
        if not(moedas[moeda] == moedas[moeda+1]):
            if moedas[moeda] > moedas[moeda+1]:
                return f"Posição {moeda}"
            elif moedas[moeda] < moedas[moeda+1]:
                return f"Posição {moeda+1}"


# Testando com todas as posições possíveis (5 no total)
print(posicao_moeda_falsa([1, 0, 0, 0, 0]))  # Posição 0
print(posicao_moeda_falsa([1, 11, 1, 1, 1]))  # Posição 1
print(posicao_moeda_falsa([3, 3, 3.0003, 3, 3]))  # Posição 2
print(posicao_moeda_falsa([0.5, 0.5, 0.5, 0.56, 0,5]))  # Posição 3
print(posicao_moeda_falsa([6, 6, 6, 6, 7]))  # Posição 4
