# ex009: Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
def reverte_numero(numero: int):
    return str(numero)[::-1]

if __name__ == "__main__":
    print(reverte_numero(12))  # 21
    print(reverte_numero(1551))  # 1551
    print(reverte_numero(84367))  # 76348
