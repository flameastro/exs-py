# ex057: Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.
def retorna_dias_pessoa(anos: int, meses: int, dias: int):
    if meses > 12 or meses < 1 or dias < 1 or dias > 31 or anos < 1 or anos > 120:
        return "Cadastro inválido. Por favor, verifique os valores."

    dias += anos * 365
    dias += meses * 30

    return f"Dias totais: {dias}"


if __name__ == "__main__":
    print(retorna_dias_pessoa(15, 2, 10))  # Dias totais: 5545
    print(retorna_dias_pessoa(25, 8, 31))  # Dias totais: 9396
    print(retorna_dias_pessoa(120, 12, 31))  # Dias totais: 44191
    print(retorna_dias_pessoa(0, 45, 12))  # Cadastro inválido. Por favor, verifique os valores.
