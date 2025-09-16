# ex114: Crie uma função que retorne a soma de todos os valores de uma lista
def soma_valores_lista(lista: list):
    if len(lista) > 1:
        try:
            soma = sum(lista)
            return f"A soma de todos os elementos da lista é de {soma}"
        except TypeError:
            return "A lista deve conter apenas números."
        except Exception as e:
            return f"Erro: {e}"

    return "A lista deve contér mais de um elemento."   


if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(soma_valores_lista(lista1))  # A soma de todos os elementos da lista é de 55

    lista2 = [2, 2]
    print(soma_valores_lista(lista2))  # A soma de todos os elementos da lista é de 4

    lista3 = []
    print(soma_valores_lista(lista3))  # A lista deve contér mais de um elemento.

    lista4 = ["Python", "JavaScript", "HTML", "CSS"]
    print(soma_valores_lista(lista4))  # A lista deve conter apenas números.
