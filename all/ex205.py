# Crie uma função que calcula porcentagens
def calcula_porcentagem(x, y):
    return f"{x}% de {y} é {x * y / 100}"


if __name__ == "__main__":
    print(calcula_porcentagem(25, 150))  # 25% de 150 é 37.5
    print(calcula_porcentagem(35, 890))  # 35% de 890 é 311.5
    print(calcula_porcentagem(78, 964))  # 78% de 964 é 751.92
