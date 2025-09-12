# ex061: Crie uma função que verifica se um número é inteiro
def verify_integer_number(number):
    return number.is_integer()


if __name__ == "__main__":
    print(verify_integer_number(55))
    print(verify_integer_number(23.4))
    print(verify_integer_number(23.0))
