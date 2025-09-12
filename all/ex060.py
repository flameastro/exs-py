# ex060: Faça um programa que tenha um procedimento chamado Contador() que recebe três valores como parâmetro: o início, o fim e o incremento de uma contagem. O programa principal deve solicitar a digitação desses valores e passá-los ao procedimento, que vai mostrar a contagem na tela.
# Ex: Para os valores de início (4), fim (20) e incremento(3) teremos Contador(4, 20, 3) vai mostrar na tela 4 >> 7 >> 10 >> 13 >> 16 >> 19 >> FIM


inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passos = int(input('Digite os passos: '))

def Contador(inicio, fim, passos):
    for i in range(inicio, fim+1, passos):
        print(f'{i} >> ', end='')
    print('FIM')


Contador(inicio, fim, passos)
