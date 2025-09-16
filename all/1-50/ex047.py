# ex047: Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses valores para um procedimento Maior() que vai verificar qual deles é o maior e mostrá-lo na tela. Caso os dois valores sejam iguais, mostrar uma mensagem informando essa característica.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

def Maior(n1, n2):
    if n1 > n2:
        print('O primeiro número é maior que o segundo número')
    elif n1 < n2:
        print('O primeiro número é menor que o segundo número')
    else:
        print('Ambos são iguais')
Maior(n1, n2)
