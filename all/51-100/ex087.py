# ex087: Crie uma função que calcule a tabuada de 0 até o número que o usuário digitou.
def tabuada(numero_tabuada: int):
    if numero_tabuada < 1 or numero_tabuada > 1_000_000:
        print("O número deve estar entre 1 a 1 milhão.")
        return False

    for numero in range(0, 11):
        resultado = numero * numero_tabuada
        print(f"{numero_tabuada} * {numero} = {resultado}")


if __name__ == "__main__":
    tabuada(7)
    tabuada(45)
    tabuada(154)
