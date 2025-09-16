# ex133: Crie uma função que tenha raio como parâmetro e retorne a área de um círculo. Sabendo que a fórmula é: π x raio^2
import math


def retorna_area_circulo(raio: int) -> float:
    PI = math.pi
    area = PI * raio**2

    return area

if __name__ == "__main__":
    print(retorna_area_circulo(2))  # 12.566370614359172
    print(retorna_area_circulo(45))  # 6361.725123519331
    print(retorna_area_circulo(15))  # 706.8583470577034
    print(retorna_area_circulo(1))  # 3.141592653589793
