# ex019: Faça um programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# 326 = 3 centenas, 2 dezenas e 6 unidades
# 12 = 1 dezena e 2 unidades
# Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
def decomposicao(numero: int) -> str:
    if numero not in range(1, 1001):
        return "Por favor, insir um número entre 1 a 1000."

    print(f"Número: {numero}")

    if len(str(numero)) == 3:
        centenas = numero // 100
        dezenas = str(numero // 10)[1]
        unidades = numero % 10
        return f"{centenas} centenas, {dezenas} dezenas e {unidades} unidades."
    elif len(str(numero)) == 2:
        dezenas = numero // 10
        unidades = numero % 10
        return f"{dezenas} dezenas e {unidades} unidades."
    elif len(str(numero)) == 1:
        return f"{numero} unidades."
    else:
        return f"1 milhar, 0 centenas, 0 dezenas e 0 unidades."


NUMEROS = [326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]
for numero in NUMEROS:
    print(decomposicao(numero))
