# ex035: Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses valores para um procedimento Somador() que vai calcular e mostrar a soma entre eles.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

def soma(n1, n2):
    print(f'A soma é de {n1 + n2}')


soma(n1, n2)
