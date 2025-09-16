# ex055: Crie uma função que retorna um número, baseado numa string
strings = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
def retorna_numero(string: str):
    if string in strings:
      posicao_string = strings.index(string)
      return f"O número é: {posicao_string}"

    return "Este número não está na string."


if __name__ == "__main__":
    print(retorna_numero('mil'))  # Este número não está na string.
    print(retorna_numero('nove'))  # O número é: 9
    print(retorna_numero('zero'))  # O numero é: 0
