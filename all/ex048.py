# ex048: Crie uma lógica que leia um número inteiro e passe para um procedimento ParOuImpar() que vai verificar e mostrar na tela se o valor passado como parâmetro é PAR ou ÍMPAR.

numero = int(input('Digite um número: '))

def ParOuImpar(numero):
    print('PAR' if numero % 2 == 0 else 'ÍMPAR')


ParOuImpar(numero)
