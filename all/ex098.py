# ex098: Crie uma função que receba uma string como parâmetro e retorne a string sem a primeira letra
def retorna_sem_primeira_letra(string: str):
    try:
        return string[1:]
    except AttributeError as attr_e:
        return f"O argumento deve ser uma string. Erro: {attr_e}"
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    print(retorna_sem_primeira_letra("Olá, mundo!"))  # "lá, mundo!"
    print(retorna_sem_primeira_letra("Python"))  # "ython"
    print(retorna_sem_primeira_letra(""))  # ""
    print(retorna_sem_primeira_letra(23))  # Erro: 'int' object is not subscriptable
