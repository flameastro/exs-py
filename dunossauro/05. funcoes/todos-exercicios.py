# ex001: Faça um programa para imprimir:

# 1
# 2   2
# 3   3   3
# .....
# n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
def imprime_linhas(n: int):
    for x in range(1, n+1):
        yield f'{str(x)}   ' * x


if __name__ == "__main__":
    for l in imprime_linhas(4):
        print(l)
    """
    1   
    2   2   
    3   3   3
    4   4   4   4
    """

    for l in imprime_linhas(6):
        print(l)
    """
    1
    2   2
    3   3   3
    4   4   4   4
    5   5   5   5   5
    6   6   6   6   6   6
    """


# ex002: Faça um programa para imprimir:
# 1
# 1   2
# 1   2   3
# .....
# 1   2   3   ...  n
# Para um n informado pelo usuário. Use uma função que receba um valor n inteiro, imprima até a n-ésima linha.
def imprime_linhas_numeradas(n: int):
    for x in range(1, n+1):
        yield "   ".join([str(x) for x in range(1, x+1)])


if __name__ == "__main__":
    for item in imprime_linhas_numeradas(3):
        print(item)
    """
    1
    1   2
    1   2   3
    """

    for item in imprime_linhas_numeradas(12):
        print(item)
    """
    1
    1   2
    1   2   3
    1   2   3   4
    1   2   3   4   5
    1   2   3   4   5   6
    1   2   3   4   5   6   7
    1   2   3   4   5   6   7   8
    1   2   3   4   5   6   7   8   9
    1   2   3   4   5   6   7   8   9   10
    1   2   3   4   5   6   7   8   9   10   11
    1   2   3   4   5   6   7   8   9   10   11   12
    """


# ex003: Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
def soma(x: float, y:float , z:float):
    return sum([x, y, z])


if __name__ == "__main__":
    print(soma(3, 5, 4))  # 12
    print(soma(25, 25, 50))  # 100
    print(soma(56, 7, 1))  # 64


# ex004: Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere P, se seu argumento for positivo, e N, se seu argumento for zero ou negativo.
def retorna_caractere(numero: int):
    return "P" if numero >= 1 else "N"


if __name__ == "__main__":
    print(retorna_caractere(13))  # P
    print(retorna_caractere(0))  # N
    print(retorna_caractere(-5))  # N


# ex005: Faça um programa com uma função chamada soma_imposto. A função possui dois parâmetros formais: taxa_imposto, que é a quantia de imposto sobre vendas expressas em porcentagem, e custo, que é o custo de um item antes do imposto. A função "altera" o valor de custo para incluir o imposto sobre vendas.
def soma_imposto(custo: float, taxa_imposto: float):
    return custo - (custo * taxa_imposto)


if __name__ == "__main__":
    print(soma_imposto(1250.99, 0.4))  # 750.594
    print(soma_imposto(25350, 0.15))  # 21547.5
    print(soma_imposto(785.8, 0.45))  # 432.18999999999994


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


# ex007: Faça um programa que use a função valor_pagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a função valor_pagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução, o programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento, o programa deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
def valor_pagamento(valor, dias_atraso):
    if dias_atraso == 0:
        return valor
    else:
        return valor * (1 + 0.03 + 0.001 * dias_atraso)

total_prestacoes = 0
quantidade_prestacoes = 0

while True:
    valor = float(input("Digite o valor da prestação (0 para sair): "))

    if valor == 0:
        break

    dias = int(input("Digite o número de dias em atraso: "))

    valor_pago = valor_pagamento(valor, dias)

    print(f"Valor a ser pago: R$ {valor_pago:.2f}\n")

    total_prestacoes += valor_pago
    quantidade_prestacoes += 1

print("\n=== Relatório do dia ===")
print(f"Quantidade de prestações pagas: {quantidade_prestacoes}")
print(f"Valor total de prestações pagas: R$ {total_prestacoes:.2f}")


# ex008: Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
def retorna_quantidade_digitos(inteiro: int):
    return len(str(inteiro))

if __name__ == "__main__":
    print(retorna_quantidade_digitos(12))  # 2
    print(retorna_quantidade_digitos(49823))  # 5
    print(retorna_quantidade_digitos(0))  # 1


# ex009: Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
def reverte_numero(numero: int):
    return str(numero)[::-1]

if __name__ == "__main__":
    print(reverte_numero(12))  # 21
    print(reverte_numero(1551))  # 1551
    print(reverte_numero(84367))  # 76348


# ex010: Jogo de Craps. Faça um programa que implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
from random import randint
def jogo_de_craps():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    soma = dado1 + dado2

    print(f"Resultado do dado 1: {dado1}")
    print(f"Resultado do dado 2: {dado2}")
    print(f"Soma: {soma}")

    if soma == 7 or soma == 11:
        print("Natural -> Ganhou")
    elif soma == 2 or soma == 3 or soma == 12:
        print("Craps -> Perdeu")
    elif soma in range(4, 7) or soma in range(8, 11):
        print("Ponto")

jogo_de_craps()


# ex010: Jogo de Craps. Faça um programa que implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente.
from random import randint
def jogo_de_craps():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    soma = dado1 + dado2

    print(f"Resultado do dado 1: {dado1}")
    print(f"Resultado do dado 2: {dado2}")
    print(f"Soma: {soma}")

    if soma == 7 or soma == 11:
        print("Natural -> Ganhou")
    elif soma == 2 or soma == 3 or soma == 12:
        print("Craps -> Perdeu")
    elif soma in range(4, 7) or soma in range(8, 11):
        print("Ponto")

jogo_de_craps()
