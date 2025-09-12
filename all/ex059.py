# ex059: Faça um Programa que leia um número e exiba o dia correspondente da semana
def dia_de_semana(numero: int):
    dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

    if numero not in range(1, 8):
        return 'Não foi possível acessar o dia.'

    return dias[numero-1]


if __name__ == "__main__":
    print(dia_de_semana(1))  # Segunda
    print(dia_de_semana(6))  # Sábado
    print(dia_de_semana(7))  # Domingo
    print(dia_de_semana("Python"))  # Não foi possível acessar o dia.
