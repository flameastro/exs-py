# ex153: Crie uma função que receba dois números e uma string, indicando a operação a ser feita entre estes dois números. As opções de operações são: "add", "subtract", "divide", "multiply".
def calculadora_aritmetica(a: float, b: float, operacao: str):
    if operacao not in ["add", "subtract", "divide", "multiply"]:
        return "Operação inválida."

    if operacao == "add":
        return a + b
    elif operacao == "subtract":
        return a - b
    elif operacao == "divide":
        return a / b

    return a * b


if __name__ == "__main__":
    print(calculadora_aritmetica(4, 9, "add"))  # 13
    print(calculadora_aritmetica(45, 8, "multiply"))  # 360
    print(calculadora_aritmetica(1, 1.2, "divide"))  # 0.8333333333333334
    print(calculadora_aritmetica(60, 50, "subtract"))  # 10
    print(calculadora_aritmetica(0, 0, "disconhecido"))  # Operação inválida.
