# ex045: Crie um programa que tenha uma função Media(), que vai receber as 2 notas de um aluno e retornar a sua média para o programa principal.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

def Media(n1, n2):
    media = (n1 + n2) / 2
    return media


print('Média:', Media(n1, n2))
