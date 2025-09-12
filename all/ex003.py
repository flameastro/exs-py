# ex003: Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno. Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

print(f'A média é de {media}')
