# ex065: Refaça o exercício 105, só que agora em forma de função Maior(), mas faça uma adaptação que vai receber TRÊS números como parâmetro e vai retornar qual foi o maior entre eles.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

def Maior(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return 'O primeiro número é o maior número'
    elif n2 > n1 and n2 > n3:
        return 'O segundo número é o maior número'
    elif n3 > n1 and n3 > n2:
        return 'O terceiro número é o maior número'


print(Maior(n1, n2, n3))
