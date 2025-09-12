# ex156: Conte as ovelhas! Crie uma função que receba um número inteiro maior que 1 como parâmetro e retorne {numero} ovelha... de 1 até o número.
def contar_ovelhas(ovelhas: int) -> str:
    if ovelhas <= 1:
        print("O número deve ser maior que 1.")
        return False

    for ovelha in range(1, ovelhas+1):
        print(f"{ovelha} ovelha(s)... ", end="")


if __name__ == "__main__":
    contar_ovelhas(3)  # 1 ovelha(s)... 2 ovelha(s)... 3 ovelha(s)... 
    contar_ovelhas(1)  # O número deve ser maior que 1.
    contar_ovelhas(12)  # 1 ovelha(s)... 2 ovelha(s)... 3 ovelha(s)... 4 ovelha(s)... 5 ovelha(s)... 6 ovelha(s)... 7 ovelha(s)... 8 ovelha(s)... 9 ovelha(s)... 10 ovelha(s)... 11 ovelha(s)... 12 ovelha(s)...
