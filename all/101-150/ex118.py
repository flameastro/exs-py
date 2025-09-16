# ex118: Crie uma programa que pede ao usuário 10 números, e separe e armazene números pares e números ímpares em duas listas diferentes.
def separar_pares_impares():
    pares = []
    impares = []

    try:
        for numero in range(10):
            numero = int(input(f'Digite o número {numero+1}: '))
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)
    except ValueError as value_e:
        return f"A lista pode conter apenas números. Erro: {value_e}"
    except Exception as e:
        return f"Erro: {e}"

    return (
        f"Lista de números pares: {pares}\n"
        f"Lista de números ímpares: {impares}"
    )


if __name__ == "__main__":
    print(separar_pares_impares())
