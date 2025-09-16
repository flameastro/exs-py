# ex051: Escreva uma função que tem como argumento minutos e converta para segundos
def converte_minutos_para_segundos(minutos: int):
    if minutos.is_integer():
        segundos = minutos * 60
        return f"O total de segundos é {segundos}"

    return "Os minutos devem ser inteiros."


if __name__ == "__main__":
    print(converte_minutos_para_segundos(5))
    print(converte_minutos_para_segundos(12))
    print(converte_minutos_para_segundos(10))
