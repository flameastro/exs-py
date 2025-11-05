# ex013: Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.
def desenha_moldura(linhas=1, colunas=1):
    if linhas < 1:
        linhas = 1
    elif linhas > 20:
        linhas = 20

    if colunas < 1:
        colunas = 1
    elif colunas > 20:
        colunas = 20

    print("+" + "-" * colunas + "+")

    for _ in range(linhas):
        print("|" + " " * colunas + "|")

    print("+" + "-" * colunas + "+")


if __name__ == "__main__":
    desenha_moldura(4, 10)
    desenha_moldura(7, 15)
    desenha_moldura(12, 8)
