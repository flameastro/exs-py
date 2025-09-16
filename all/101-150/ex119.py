# ex119: Crie uma função que receba uma lista e retorne "Par", se existe mais números pares, caso contrário, retorne "Ímpar".
def verifica_pares_impares(lista: list):
    pares = 0
    impares = 0

    if len(lista) < 1:
        return "A lista deve ter a menos um número."

    try:
        for numero in lista:
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1

        if pares > impares:
            return "Par"
        elif impares > pares:
            return "Ímpar"

        return "Pares e Ímpares"
    except TypeError:
        return "A lista deve conter apenas números."
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    lista1 = [12, 13, 14, 15, 16, 17, 18, 19, 20]  # Par
    print(verifica_pares_impares(lista1))

    lista2 = [2, 4, 1, 3]
    print(verifica_pares_impares(lista2))  # Pares e Ímpares

    lista3 = ["Par", "Ímpar"]
    print(verifica_pares_impares(lista3))  # A lista deve conter apenas números.
