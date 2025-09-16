# ex042: O exercicio 79 vai ter um problema quando digitarmos o primeiro valor maior que o último. Resolva esse problema com um código que funcione em qualquer situação.

inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passos = int(input('Digite os passos: '))

if inicio < fim:
    for i in range(inicio, fim+1, passos):
        print(i)
else:
    for i in range(inicio, fim-1, -passos):
        print(i)
