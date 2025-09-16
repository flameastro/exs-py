# ex050: Crie uma função que retorne o quadrado de um número
def retorna_quadrado(numero: int):
    if numero.is_integer():
        quadrado = numero ** 2
        return f"O quadrado de {numero} é {quadrado}"


if __name__ == "__main__":
    print(retorna_quadrado(15))
    print(retorna_quadrado(23))
    print(retorna_quadrado(0))
    print(retorna_quadrado(-4))
