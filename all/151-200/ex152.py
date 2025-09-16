# ex152: Encontre a próxima raíz quadrada perfeita de um número, retorne -1 caso o número dado não seja uma raíz quadrada perfeita
import math

def retorna_proxima_raiz(numero: int) -> int:
    raiz_quadrada = math.sqrt(numero) + 1
    if not raiz_quadrada.is_integer():
        return -1

    proxima_raiz = int(raiz_quadrada**2)

    return proxima_raiz


if __name__ == "__main__":
    print(retorna_proxima_raiz(144))  # 169
    print(retorna_proxima_raiz(34))  # -1
    print(retorna_proxima_raiz(61858225))  # 61873956
