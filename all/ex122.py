# ex122: Crie um programa em que pede ao usuário um número e o programa deve retornar se este número é uma raíz exata ou não.
import math

while True:
    try:
        numero = int(input("Digite um número inteiro:\n>>>"))

        def verifica_raiz_exata(numero: int):
            raiz = math.sqrt(numero)

            if raiz.is_integer():
                yield f"{numero} é uma raíz quadrada exata"
            else:
                yield f"{numero} não é uma raíz quadrada exata"

            yield f"Resultado da raíz: {raiz}"

        for i in verifica_raiz_exata(numero):
            print(i)

    except ValueError:
        print("Por favor, digite um número inteiro\n")
    else:
        break
