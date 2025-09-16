# ex067: Melhore o exercício 73, criando além da função Media() uma outra função chamada Situacao(), que vai retornar para o programa principal se o aluno está APROVADO, em RECUPERAÇÃO ou REPROVADO. Essa nova função, vai receber como parâmetro o resultado retornado pela função Media().

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

def Media(n1, n2):
    global media
    media = (n1 + n2) / 2
    return media


def Situacao(media):
    if media >= 7:
        return 'APROVADO'
    elif media >= 5:
        return 'RECUPERAÇÃO'
    else:
        return 'REPROVADO'


print(Media(n1, n2))
print(Situacao(media))
