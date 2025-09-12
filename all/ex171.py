# ex171: Crie uma função que receba um número e diga se aquele número tem números adjacentes. Ou seja, números que são iguais e estão um ao lado do outro. Exemplo: 2435543 -> é um número adjacente pois o primeiro 5 está ao lado do segundo 5.
def numero_adjacente(numero: int) -> bool:
    if not numero.is_integer() or isinstance(numero, (bool, float, str, list, tuple, dict, set)):
        return "Resposta incorreta, deve ser um número inteiro."

    # Jeito mais fácil (não envolve quase nenhum esforço de raciocínio)
    # numero = str(numero)

    # for i in range(99, -1, -11):
    #     if str(i) in numero:
    #         return True

    # return False

    numero = str(numero)

    for index, _ in enumerate(numero):
        if not index+1 >= len(numero) and numero[index] == numero[index+1]:
            return True

    return False


if __name__ == "__main__":
    print(numero_adjacente(23456403894799))  # True
    print(numero_adjacente(74346236723500438))  # True
    print(numero_adjacente(549224.32))  # Resposta incorreta, deve ser um número inteiro.
    print(numero_adjacente(True))  # Resposta incorreta, deve ser um número inteiro.
    print(numero_adjacente(843653468))  # False
    print(numero_adjacente(4))  # False
