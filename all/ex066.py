# ex066: Crie um programa que tenha uma função SuperSomador(), que vai receber dois números como parâmetro e depois vai retornar a soma de todos os valores no intervalo entre os valores recebidos.
# Ex:
# SuperSomador(1, 6) vai somar 1 + 2 + 3 + 4 + 5 + 6 e vai retornar 21
# SuperSomador(15, 19) vai somar 15 + 16 + 17 + 18 + 19 e vai retornar 85

def SuperSomador(n1, n2):
    soma = 0
    for i in range(n1, n2+1):
        a = i
        soma += a
    return f'Soma: {soma}'


print(SuperSomador(1, 6))
print(SuperSomador(4, 10))
print(SuperSomador(3, 9))
print(SuperSomador(15, 19))
print(SuperSomador(7, 14))
