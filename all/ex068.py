# ex068: Crie uma função que aceite kwargs e retorne a soma de todos os valores passados como argumentos.
def soma(*numeros):
    total = 0
    for numero in numeros:
        total += numero

    return f"O total é {total}"


print(soma(10, 20, 30, 40))  # O total é 100
print(soma(35, 78, 12, 38, 84, 437))  # O total é 684
