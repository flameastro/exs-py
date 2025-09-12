# ex169: Crie uma função que recebe um número inteiro como parâmetro e retorne o fatorial deste número.
def fatorial(numero_usuario: int) -> int:
    if numero_usuario <= 1:
        return "O número deve ser maior que 1."

    fatorial = 1

    for numero in range(1, numero_usuario+1):
        fatorial *= numero

    return fatorial


if __name__ == "__main__":
    print(fatorial(5))  # 120
    print(fatorial(4))  # 24
    print(fatorial(6))  # 720
    print(fatorial(7))  # 5040
    print(fatorial(1))  # O número deve ser maior que 1.

