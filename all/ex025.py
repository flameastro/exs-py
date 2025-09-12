# ex025: O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o indivíduo dentro de certas faixas.
# - abaixo de 18.5: Abaixo do peso
# - entre 18.5 e 25: Peso ideal
# - entre 25 e 30: Sobrepeso
# - entre 30 e 40: Obesidade
# - acima de 40: Obseidade mórbida
# Obs: O IMC é calculado pela expressão peso/altura2 (peso dividido pelo quadrado da altura)

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura em cm: '))

IMC = peso / altura ** 2

print(f'Seu IMC é: {round(IMC, 4)}')

if IMC < 18.5:
    print("Abaixo do peso")
elif IMC < 25:
    print("Peso normal")
elif IMC < 30:
    print("Sobrepeso")
elif IMC < 40:
    print("Obesidade")
else:
    print('Obesidade mórbida')
