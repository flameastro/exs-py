# ex131: Crie uma função que converta quilômetros para milhas (1 km  ≈  0,621371mi).
def quilometros_para_milhas(quilometros: int) -> float:
    milhas = quilometros * 0.621371

    return milhas


if __name__ == "__main__":
    print(quilometros_para_milhas(5))  # 3.106855
    print(quilometros_para_milhas(504))  # 313.170984
    print(quilometros_para_milhas(1))  # 0.621371

