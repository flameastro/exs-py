# ex054: Crie um programa que tem a possibilidade de converter reais para doláres e vice-versa. Considere que: 1 dolár = R$6
def conversor(tipo: str, quantidade: float):
    if tipo.lower() == 'doláres':
        conversao = round(quantidade * 6, 2)
        return f'Você tem R${conversao} reais'
    elif tipo.lower() == 'reais':
        conversao = round(quantidade / 6, 2)
        return f'Você tem ${conversao} doláres'

    return 'Algo de errado. Tente novamente'


if __name__ == "__main__":
    print(conversor('doláres', 5))
    print(conversor('reais', 5))
    print(conversor('doláres', 12000))
    print(conversor('reais', 55600))
    print(conversor('reais', 65.90))
