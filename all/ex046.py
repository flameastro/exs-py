# ex046: Crie um programa que melhore o procedimento Gerador() da questão anterior para que mostre a mensagem repetida varias vezes
# Ex: Ao chamar Gerador("Aprendendo Portugol", 4) aparece:
# +-------=======------+
# Aprendendo Portugol
# Aprendendo Portugol
# Aprendendo Portugol
# Aprendendo Portugol
# +-------=======------+

def Gerador(texto, quantidade=1):
    print('-' * 35)
    for _ in range(quantidade):
        print(texto)
    print('-' * 35)


Gerador("Aprendendo Python com Guanabara", 7)
