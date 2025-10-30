# ex003: Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
def soma(x: float, y:float , z:float):
    return sum([x, y, z])


if __name__ == "__main__":
    print(soma(3, 5, 4))  # 12
    print(soma(25, 25, 50))  # 100
    print(soma(56, 7, 1))  # 64
