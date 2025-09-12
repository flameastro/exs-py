# ex132: Crie uma função que receba uma string como parâmetro e retorna seu acrônimo (Python Vs JavaScript -> PVJ)
def retorna_acronimo(string: str):
    string = string.split()

    acronimo = ""

    for palavra in string:
        letra = palavra[0]
        acronimo += letra.upper()

    return acronimo


if __name__ == "__main__":
    print(retorna_acronimo("Python Vs JavaScript"))  # PVJ
    print(retorna_acronimo("Albert Einstein e Oppenheimer"))  # AEEO
    print(retorna_acronimo())
