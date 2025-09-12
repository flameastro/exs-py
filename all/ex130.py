# ex130: Crie uma função com Celsius como parâmetro e retorne a temperatura equivalente a Fahrenheit.
def converte_temperatura(Celsius: int) -> int:
    fahrenheit = (Celsius * 9/5) + 32

    return fahrenheit


if __name__ == "__main__":
    print(converte_temperatura(32))  # 89.6
    print(converte_temperatura(45))  # 113.0
    print(converte_temperatura(12))  # 53.6
    print(converte_temperatura(4.5))  # 40.1
    print(converte_temperatura(1))  # 33.8
