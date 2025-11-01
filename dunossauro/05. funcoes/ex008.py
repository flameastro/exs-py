# ex008: Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
def retorna_quantidade_digitos(inteiro: int):
    return len(str(inteiro))

if __name__ == "__main__":
    print(retorna_quantidade_digitos(12))  # 2
    print(retorna_quantidade_digitos(49823))  # 5
    print(retorna_quantidade_digitos(0))  # 1
