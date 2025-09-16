# ex090: Crie um programa que realiza a contagem regressiva de 5 segundos
from time import sleep

def contagem_regressiva():
    for i in range(5, 0, -1):
        print(i)
        sleep(1)


contagem_regressiva()
