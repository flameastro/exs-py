# ex136: Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas por semana, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
def retorna_salario(numero: int, horas: int, valor_hora: float) -> float:
    salario = valor_hora * horas

    return (
        f"NÚMERO = {numero}\n"
        f"SALÁRIO = R$ {salario:.2f}"
    )


if __name__ == "__main__":
    print(retorna_salario(25, 100, 5.50))  # NÚMERO = 25; SALÁRIO = R$ 550.00
    print(retorna_salario(1, 200, 20.50))  # NÚMERO = 1; SALÁRIO = R$ 4100.00
    print(retorna_salario(6, 145, 15.55))  # NÚMERO = 6; SALÁRIO = R$ 2254.75
