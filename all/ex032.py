# ex032: Crie um programa que tenha um procedimento Gerador() que, quando chamado, mostre a mensagem "Olá, Mundo!" com algum componente visual (linhas)
# Ex: Ao chamar Gerador() aparece:
# +-------=======------+
# Olá, Mundo!
# +-------=======------+

def Gerador():
    print('-' * 35)
    print('Olá Mundo!'.center(35, ' '))
    print('-' * 35)

Gerador()
