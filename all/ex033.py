# ex033: Crie um programa que melhore o procedimento Gerador() da questão anterior para que mostre uma mensagem personalizada, passada como parâmetro.
# Ex: Ao chamar Gerador("Aprendendo Python") aparece:
# +-------=======------+
# Aprendendo Python
# +-------=======------+

def Gerador(texto):
    print('-' * 40)
    print(texto.center(40, ' '))
    print('-' * 40)

Gerador('Aprendendo Python com Guanabara')
Gerador('Guanabara -> O melhor professor de tecnologia')
