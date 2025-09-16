# ex099: Crie uma função que retorne o maior valor de dois números
def retorna_maior_valor(n1: int, n2: int):
    try:
        if not isinstance(n1, (int, float)) or not isinstance(n2, (int, float)):
            return "Valores inválidos."

        # Maneira 1
        # maior_valor = max(n1, n2)
        # return f"O maior valor é {maior_valor}"

        # Maneira 2
        if n1 > n2:
            return f"O maior valor é {n1}, no índice 0."
        elif n1 < n2:
            return f"O maior valor é {n2}, no índice 1."

        return "Ambos possuem o mesmo valor."
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    print(retorna_maior_valor(15, 24))  # O maior valor é 24
    print(retorna_maior_valor(12, 12))  # Ambos possuem o mesmo valor.
    print(retorna_maior_valor("Python", "JS"))  # Valores inválidos.
    print(retorna_maior_valor(True, False))  # O maior valor é True, no índice 0. (cry)
