# ex001: Imprima Hello, World!
print("Hello, World!")


# ex002: Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B atribuindo o seu resultado na variável soma. Imprima soma.
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
soma = a + b

print(f'A soma entre {a} e {b} é {soma}')


# ex003: Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno. Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

print(f'A média é de {media}')


# ex004: Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3

print(f'A média é de {media}')


# ex005: Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
d = int(input('Digite o quarto valor: '))

diferenca = (a * b - c * d)
print(diferenca)


# ex006: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas para ela
nome = input('Digite o seu nome: ')
print(f'Prazer, {nome}!')


# ex007: Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório entre eles.
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

soma = x + y
print(f'A soma entre os dois números é {soma}')


# ex008: Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina.
n1 = float(input('Digite a primeira nota do(a) aluno(a): '))
n2 = float(input('Digite a segunda nota do(a) aluno(a): '))

media = (n1 + n2) / 2
print(f'A média do aluno é {media}')


# ex009: Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a sua terça parte.
numero = float(input('Digite um número real: '))

print(f'O dobro de seu número é {numero * 2}')
print(f'A terça parte do seu número é {numero / 3}')


# ex010: Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.
metros = float(input('Digite uma distância em metros: '))
print(f'{metros / 1000}Km')
print(f'{metros / 100}Hm')
print(f'{metros / 10}Dam')
print(f'{metros * 10}dm')
print(f'{metros * 100}cm')
print(f'{metros * 1000}mm')


# ex011: Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$6.
reais = int(input('Quantos reais você tem? '))
dolares = reais / 6

print(f'Você pode comprar {round(dolares, 2)} doláres.')


# ex012: Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2m².
largura = float(input('Digite a largura da parede (em metros): '))
altura = float(input('Digite a altura da parede (em metros): '))

area = largura * altura
tinta = area / 2

print(f'A área da parede é de {area}m²')
print(f'A tinta necessária é {tinta} litros de tinta')


# ex013: Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.
produto = float(input('Digite o preço do produto: '))
desconto = produto * 0.05
preco = produto - desconto

print(f'O preço do produto com um desconto de 5% é de {preco}')


# ex014: Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.
salario = float(input('Digite o seu salário: '))
aumento = salario * 0.15
salario += aumento

print(f'O seu novo salário com 15% de aumento é {salario}')


# ex015: A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.
km = float(input('Digite a quantidade de Kms percorridos: '))
dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))

total = 0
total += (dias * 90) + (km * 0.20)

print(f'O total a se pagar é {total}')


# ex016: Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada.
dias = int(input('Quantos dias em um mês você trabalha? '))
horas = 8
lucro_hora = 25

salario = (lucro_hora * horas) * dias

print(f'O salário do funcionário é de {salario}')


# ex017: [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule quantos dias de vida um fumante perderá e exiba o total em dias.
cigarros_dia = int(input('Quantos cigarros fuma por dia? '))
anos = int(input('Quantos anos fuma? '))

total_cigarros = cigarros_dia * 365 * anos
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / 60 / 24

print(f'Dias perdidos: {dias_perdidos}')


# ex018: Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).
x = float(input("Qual a posição de x? "))
y = float(input("Qual a posição de y? "))

if x > 0 and y > 0:
    print('Q1')
elif x > 0 and y < 0:
    print('Q4')
elif x < 0 and y < 0:
    print('Q3')
elif x < 0 and y > 0:
    print('Q2')
else:
    print('Origem')


# ex019: Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.
velocidade = int(input('Digite a velocidade do carro: '))
valor_multa = 0
if velocidade > 80:
    valor_multa = (velocidade - 80) * 5
    print(f'Sua multa é de R${valor_multa} reais por ultrapassar o limite estabelecido!')
else:
    print('Parabéns pela sua velocidade!')


# ex020: Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela. No final, analise a média e mostre se o aluno teve ou não um bom aproveitamento (se ficou acima da média 7.0).
nome = input('Digite o seu nome: ').strip().title()
n1 = float(input(f'{nome}, Digite a primeira nota: '))
n2 = float(input(f'{nome}, Digite a segunda nota: '))

media = (n1 + n2) / 2

if media > 7.0:
    print('Você está aprovado')
elif media > 5.0:
    print('Você está em recuperação')
else:
    print('Você está reprovado')


# ex021: Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")


# ex022: Faça um algoritmo que leia um determinado ano e mostre se ele é ou não BISSEXTO. (formula básica)
ano = int(input('Digite um ano qualquer: '))

if ano % 4 == 0 and ano % 100 != 0:
    print('Ano é Bissexto')
else:
    print('Ano não é Bissexto')


# ex023: Faça um algoritmo que pergunte a distância que um passageiro deseja percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200Km e R$0.45 para viagens mais longas.
distancia = int(input('Quantos Kms deseja percorrer? '))

if distancia < 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'O preço final é de R${preco} reais')


# ex024: Desenvolva um programa que leia o nome de um funcionário, seu salário, quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de acordo com a tabela a seguir:
# - Até 3 anos de empresa: aumento de 3%
# - entre 3 e 10 anos: aumento de 12.5%
# - 10 anos ou mais: aumento de 20%
funcionario = input('Digite o nome do funcionário: ')
salario = int(input('Digite o salário do funcionário: '))
anos = int(input('Quantos anos trabalha na empresa? '))


if anos < 3:
    aumento = salario * 0.03
elif anos > 3 and anos < 10:
    aumento = salario * 12.5
elif anos >= 10:
    aumento = salario * 0.20
print(f'O novo salário de {funcionario} agora é de {salario + aumento}')


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


# ex026: Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a tabela a seguir:
# - Carros populares (aluguel de R$90 por dia)
# - Até 100Km percorridos: R$0,20 por Km
# - Acima de 100Km percorridos: R$0,10 por Km
# - Carros de luxo (aluguel de R$150 por dia)
# - Até 200Km percorridos: R$0,30 por Km
# - Acima de 200Km percorridos: R$0,25 por Km

carro = input('Qual o tipo de carro? [popular/luxo]: ').strip().lower()
dias = int(input('Quantos dias? '))
kms = float(input('Quantos kms percorridos? '))

if carro == 'popular':
    aluguel = dias * 90
    if kms > 100:
        aluguel += kms * 0.10
    else:
        aluguel += kms * 0.20
elif carro == 'luxo':
    aluguel = dias * 150 
    if kms > 200:
        aluguel += kms * 0.25
    else:
        aluguel += kms * 0.30
else:
    print('Carro não encontrado.')

print(f'O aluguel do carro está com o preço de R${aluguel:.2f}')


# ex027: Um programa de vida saudável quer dar pontos de atividades físicas que podem ser trocados por dinheiro. O sistema funciona assim:
# - Cada hora de atividade física no mês vale pontos
# - até 10h de atividade no mês: ganha 2 pontos por hora
# - de 10h até 20h de atividade no mês: ganha 5 pontos por hora
# - acima de 20h de atividade no mês: ganha 10 pontos por hora
# - A cada ponto ganho, o cliente fatura R$0,05 (5 centavos)
# Faça um programa que leia quantas horas de atividade uma pessoa teve por mês, calcule e mostre quantos pontos ela teve e quanto dinheiro ela conseguiu ganhar.

horas = int(input('Quantas horas de atividade você teve no mês? '))
pontos = 0

if horas <= 10:
    pontos = horas * 2
elif horas <= 20:
    pontos = 10 * 2 + (horas - 10) * 5
else:
    pontos = 10 * 2 + 10 * 5 + (horas - 20) * 10
    
dinheiro = pontos * 0.05

print(f'Parabéns! Você teve {pontos} pontos e obteve R${dinheiro} reais!')


# ex028: # Crie um programa que calcule e mostre na tela o resultado da soma entre 6 + 8 + 10 + 12 + 14 + ... + 98 + 100.
soma = 0
for i in range(6, 101, 2):
    soma += i
print(f'A soma dos números de 6 a 100 pulando em 2 em 2 é {soma}')


# ex029: # Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 + 450 + 400 + 350 + 300 + ... + 50 + 0
soma = 0
for i in range(500, 0, -50):
    soma += i

print(f'O resultado da expressão é {soma}')


# ex030: Crie um algoritmo que leia o valor inicial da contagem, o valor final e o incremento, mostrando em seguida todos os valores no intervalo:
# Ex: Digite o primeiro Valor: 3
# Digite o último Valor: 10
# Digite o incremento: 2
# Contagem: 3 5 7 9 Acabou!
inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passos = int(input('Digite os passos: '))

for i in range(inicio, fim+1, passos):
    print(i)


# ex031: Faça um programa que leia 7 números inteiros e no final mostre o somatório entre eles.
soma = 0
for i in range(7):
    numero = int(input(f'Digite o número {i+1}: '))
    soma += numero

print(f'A soma dos números digitados foi {soma}')


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


# ex034: A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159. Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.
from math import pi

raio = float(input('Digite o valor do raio: '))
area = (raio ** 2) * pi

print(f'A área do círculo é {round(area, 4)}')


# ex035: Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses valores para um procedimento Somador() que vai calcular e mostrar a soma entre eles.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

def soma(n1, n2):
    print(f'A soma é de {n1 + n2}')


soma(n1, n2)


# ex036: Faça um programa que leia a largura e o comprimento de um terreno retangular, calculando e mostrando a sua área em m2. O programa também deve mostrar a classificação desse terreno, de acordo com a lista abaixo:
# - Abaixo de 100m2 = TERRENO POPULAR
# - Entre 100m2 e 500m2 = TERRENO MASTER
# - Acima de 500m2 = TERRENO VIP

largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))

area = largura * comprimento

if area > 500:
    print('Terreno VIP')
elif area < 500 and area > 100:
    print('Terreno MASTER')
elif area < 100:
    print('Terreno POPULAR')


# ex037: Desenvolva um algoritmo que mostre uma contagem regressiva de 30 até 1, marcando os números que forem divisíveis por 4, exatamente como mostrado abaixo:
# 30 29 [28] 27 26 25 [24] 23 22 21 [20] 19 18 17 [16]...

i = 30
while i >= 0:
    if i % 4 == 0:
        print([i])
    else:
        print(i)
    i -= 1


# ex038: Faça um programa que possua uma função chamada Potencia(), que vai receber dois parâmetros numéricos (base e expoente) e vai calcular o resultado da exponenciação.
# Ex: Potencia(5,2) vai calcular 5² = 25

def Potencia(base, expoente):
    return base ** expoente

print(Potencia(5, 2))
print(Potencia(6, 5))
print(Potencia(8, 2))
print(Potencia(5, 3))


# ex039: Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.
pares = 0
for i in range(5):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        pares += 1

print(f'Ao total são {pares} números pares')


# ex040: Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para todos, mas especialmente para mulheres. Faça um programa que leia nome, genero e o valor das compras do cliente e calcule o preço com desconto. Sabendo que:
# - Homens ganham 5% de desconto
# - Mulheres ganham 13% de desconto

nome = input('Digite o seu nome: ').strip().title()
genero = input(f'{nome}, Digite o seu genero [M/F]: ').strip().upper()
while genero not in ['M', 'F']:
    genero = input(f'{nome}, Digite corretamente [M/F]: ').strip().upper()
valor = float(input('Qual foi o valor das compras? '))

if genero == 'M':
    desconto = valor * 0.05
    preco = valor - desconto
    print(f'Como você é homem, o preço final da compra com desconto será de R${preco} reais')
elif genero == 'F':
    desconto = valor * 0.13
    preco = valor - desconto
    print(f'Como você é mulher terá um super desconto de 13%, então sua compra agora custa R${preco} reais!')


# ex041: Uma empresa precisa reajustar o salário dos seus funcionários, dando um aumento de acordo com alguns fatores. Faça um programa que leia o salário atual, o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa. No final, mostre o seu novo salário, baseado na tabela a seguir:
# - Mulheres
# - menos de 15 anos de empresa: +5%
# - de 15 até 20 anos de empresa: +12%
# - mais de 20 anos de empresa: +23%
# - Homens
# - menos de 20 anos de empresa: +3%
# - de 20 até 30 anos de empresa: +13%
# - mais de 30 anos de empresa: +25%

salario = float(input('Digite o salário: '))
genero = input('Digite o gênero [M/F]: ').strip().upper()

while genero not in ['M', 'F']:
    genero = input('Digite corretamente [M/F]: ').strip().upper()

anos = int(input('Quantos anos trabalha na empresa? '))

if genero == 'F':
    if anos < 15:
        aumento = salario * 0.05
    elif anos >= 15 and anos < 20:
        aumento = salario * 0.12
    elif anos >= 20:
        aumento = salario * 0.23
elif genero == 'M':
    if anos < 20:
        aumento = salario * 0.03
    elif anos >= 20 and anos < 30:
        aumento = salario * 0.13
    elif anos >= 30:
        aumento = salario * 0.25
salario += aumento

print(f'Seu novo salário reajustado é de R${salario} reais')


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


# ex043: Crie um programa que leia 6 números inteiros e no final mostre quantos deles são pares e quantos são ímpares.
pares = 0
impares = 0

for i in range(6):
    numero = int(input(f'Digite o número {i+1}: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Foram {pares} pares digitados e {impares} ímpares digitados.')


# ex044: Faça um programa que leia 7 nomes de pessoas e guarde-os em um vetor. No final, mostre uma listagem com todos os nomes informados, na ordem inversa daquela em que eles foram informados.

vetor = [[], [], [], [], [], [], []]

for i in range(7):
    pessoa = input('Digite o nome da pessoa: ')
    vetor[i] = pessoa

vetor.reverse()
print(vetor)


# ex045: Crie um programa que tenha uma função Media(), que vai receber as 2 notas de um aluno e retornar a sua média para o programa principal.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

def Media(n1, n2):
    media = (n1 + n2) / 2
    return media


print('Média:', Media(n1, n2))


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


# ex047: Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses valores para um procedimento Maior() que vai verificar qual deles é o maior e mostrá-lo na tela. Caso os dois valores sejam iguais, mostrar uma mensagem informando essa característica.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

def Maior(n1, n2):
    if n1 > n2:
        print('O primeiro número é maior que o segundo número')
    elif n1 < n2:
        print('O primeiro número é menor que o segundo número')
    else:
        print('Ambos são iguais')
Maior(n1, n2)


# ex048: Crie uma lógica que leia um número inteiro e passe para um procedimento ParOuImpar() que vai verificar e mostrar na tela se o valor passado como parâmetro é PAR ou ÍMPAR.

numero = int(input('Digite um número: '))

def ParOuImpar(numero):
    print('PAR' if numero % 2 == 0 else 'ÍMPAR')


ParOuImpar(numero)


# ex049: Crie uma função que retorne o número de pontos baseado na vitória, no empate e na derrota de um time de futebol. Sabendo que: vitória = 3 pontos, empate = 1 ponto e derrota = 0 pontos
def retorna_numero_pontos(vitoria, empate, derrota):
    pontos_vitoria = vitoria * 3
    pontos_empate = empate * 1
    pontos_derrota = 0

    total = pontos_vitoria + pontos_empate + pontos_derrota
    return f"Os pontos totais são de {total}"


if __name__ == "__main__":
    print(retorna_numero_pontos(15, 2, 5))  # Os pontos totais são de 47
    print(retorna_numero_pontos(23, 12, 8))  # Os pontos totais são de 81
    print(retorna_numero_pontos(3, 3, 54))  # Os pontos totais são de 12


# ex050: Crie uma função que retorne o quadrado de um número
def retorna_quadrado(numero: int):
    if numero.is_integer():
        quadrado = numero ** 2
        return f"O quadrado de {numero} é {quadrado}"


if __name__ == "__main__":
    print(retorna_quadrado(15))
    print(retorna_quadrado(23))
    print(retorna_quadrado(0))
    print(retorna_quadrado(-4))


# ex051: Escreva uma função que tem como argumento minutos e converta para segundos
def converte_minutos_para_segundos(minutos: int):
    if minutos.is_integer():
        segundos = minutos * 60
        return f"O total de segundos é {segundos}"

    return "Os minutos devem ser inteiros."


if __name__ == "__main__":
    print(converte_minutos_para_segundos(5))
    print(converte_minutos_para_segundos(12))
    print(converte_minutos_para_segundos(10))


# ex052: Crie uma função que recebe um número e imprima seu sucessor e seu antecessor
def sucessor_antecessor(numero: int):
    if numero < 1 or numero > 10000000:
        return "O número deve estar entre 1 e 10mi."

    sucessor = numero + 1
    antecessor = numero - 1

    return f"O número sucessor é {sucessor} e o número antecessor é {antecessor}"


if __name__ == "__main__":
    print(sucessor_antecessor(15))
    print(sucessor_antecessor(23))
    print(sucessor_antecessor(1))
    print(sucessor_antecessor(9999999))


# ex053: Crie uma função que recebe um número e imprima o seu dobro.
def dobro(numero: int):
    if numero < 1 or numero > 10000000:
        return "O número deve estar entre 1 e 10mi."
    dobro = numero * 2
    return f"O dobro de {numero} é {dobro}"


if __name__ == "__main__":
    print(dobro(15))
    print(dobro(25))


# ex054: Crie um programa que tem a possibilidade de converter reais para doláres e vice-versa. Considere que: 1 dolár = R$6
def conversor(tipo: str, quantidade: float):
    if tipo.lower() == 'doláres':
        conversao = round(quantidade * 6, 2)
        return f'Você tem R${conversao} reais'
    elif tipo.lower() == 'reais':
        conversao = round(quantidade / 6, 2)
        return f'Você tem ${conversao} doláres'

    return 'Algo de errado. Tente novamente'


if __name__ == "__main__":
    print(conversor('doláres', 5))
    print(conversor('reais', 5))
    print(conversor('doláres', 12000))
    print(conversor('reais', 55600))
    print(conversor('reais', 65.90))


# ex055: Crie uma função que retorna um número, baseado numa string
strings = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
def retorna_numero(string: str):
    if string in strings:
      posicao_string = strings.index(string)
      return f"O número é: {posicao_string}"

    return "Este número não está na string."


if __name__ == "__main__":
    print(retorna_numero('mil'))  # Este número não está na string.
    print(retorna_numero('nove'))  # O número é: 9
    print(retorna_numero('zero'))  # O numero é: 0


# ex056: Crie uma função que simule a chance de ser impostor no Among Us. Considere a fórmula: (numero_impostores / quantidade_jogadores) * 100
def chance_impostor_AmongUs(impostores: int, jogadores: int):
    chance = round((impostores / jogadores) * 100)
    return f"A chance de você ser impostor é de {chance}%"


if __name__ == "__main__":
    print(chance_impostor_AmongUs(2, 16))  # A chance de você ser impostor é de 12%
    print(chance_impostor_AmongUs(1, 10))  # A chance de você ser impostor é de 10%
    print(chance_impostor_AmongUs(2, 5))  # A chance de você ser impostor é de 40%


# ex057: Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.
def retorna_dias_pessoa(anos: int, meses: int, dias: int):
    if meses > 12 or meses < 1 or dias < 1 or dias > 31 or anos < 1 or anos > 120:
        return "Cadastro inválido. Por favor, verifique os valores."

    dias += anos * 365
    dias += meses * 30

    return f"Dias totais: {dias}"


if __name__ == "__main__":
    print(retorna_dias_pessoa(15, 2, 10))  # Dias totais: 5545
    print(retorna_dias_pessoa(25, 8, 31))  # Dias totais: 9396
    print(retorna_dias_pessoa(120, 12, 31))  # Dias totais: 44191
    print(retorna_dias_pessoa(0, 45, 12))  # Cadastro inválido. Por favor, verifique os valores.


# ex058: Crie uma função que retorne todos os livros que uma pessoa leu. Cadastre pessoas
def livros(nome, *livros):
    return f"{nome} leu {", ".join(livros)}"

if __name__ == "__main__":
    print(livros("Maria", 'O poder dos Hábitos', 'Hábitos Atómicos'))  # Maria leu O poder dos Hábitos, Hábitos Atómicos
    print(livros("Pedro", 'Como fazer amigos e influenciar pessoas', 'As 48 leis do poder', 'A coragem de ser imperfeito'))  # Pedro leu Como fazer amigos e influenciar pessoas, As 48 leis do poder, A coragem de ser imperfeito
    print(livros("Lucas", 'Os segredos da mente milionária', 'Comece pelo porquê'))  # Lucas leu Os segredos da mente milionária, Comece pelo porquê


# ex059: Faça um Programa que leia um número e exiba o dia correspondente da semana
def dia_de_semana(numero: int):
    dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

    if numero not in range(1, 8):
        return 'Não foi possível acessar o dia.'

    return dias[numero-1]


if __name__ == "__main__":
    print(dia_de_semana(1))  # Segunda
    print(dia_de_semana(6))  # Sábado
    print(dia_de_semana(7))  # Domingo
    print(dia_de_semana("Python"))  # Não foi possível acessar o dia.


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


# ex061: Crie uma função que verifica se um número é inteiro
def verify_integer_number(number):
    return number.is_integer()


if __name__ == "__main__":
    print(verify_integer_number(55))
    print(verify_integer_number(23.4))
    print(verify_integer_number(23.0))


# ex062: Crie um programa que leia o nome de várias pessoas e exiba a lista em ordem alfabética.
lista = []

while True:
    nome = input('Digite o nome da pessoa: ').strip().title()
    lista.append(nome)

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Digite corretamente [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue

print(f'A lista com os nomes em ordem alfabética é {sorted(lista)}')


# ex063: Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela qual foi o maior e qual foi o menor preço digitados.

maior = menor = 0
for i in range(8):
    preco = float(input(f'Digite o preço do produto {i+1}: '))

    if i == 0:
        maior = menor = preco
    else:
        if preco > maior:
            maior = preco
        elif preco < menor:
            menor = preco
print(f'O maior preço digitado foi {maior} e o menor preço digitado foi {menor}')


""" # Outras maneiras de fazer o mesmo programa
Gostaria de colocar aqui outras maneiras de se fazer este mesmo
programa em especifico, porque ele pode ser escrito de diversas
formas até melhores que esta."""

# Maneira 1
# precos = []

# for i in range(8):
#     preco = float(input(f'Digite o preço do produto {i+1}: '))
#     precos.append(preco)

# maior = max(precos)
# menor = min(precos)

# print(f'O maior preço digitado foi {maior} e o menor preço digitado foi {menor}')




# Maneira 2
# maior = menor = 0
# contador = 1

# while contador <= 8:
#     preco = float(input(f'Digite o preço do produto {contador}: '))
    
#     if contador == 1:
#         maior = menor = preco
#     else:
#         maior = max(maior, preco)
#         menor = min(menor, preco)
    
#     contador += 1

# print(f'O maior preço digitado foi {maior} e o menor preço digitado foi {menor}')

# print("\n" + "="*50 + "\n")


# ex064: # Crie um programa que leia vários números pelo teclado e mostre no final o somatório entre eles.
# Obs: O programa será interrompido quando o número 1111 for digitado

numeros = []
soma = 0
while True:
    numero = int(input('Digite um número: '))

    if numero == 1111:
        break

    numeros.append(numero)
    soma += numero

print(f'A soma dos números digitados é {soma}')


# ex065: Refaça o exercício 105, só que agora em forma de função Maior(), mas faça uma adaptação que vai receber TRÊS números como parâmetro e vai retornar qual foi o maior entre eles.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

def Maior(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return 'O primeiro número é o maior número'
    elif n2 > n1 and n2 > n3:
        return 'O segundo número é o maior número'
    elif n3 > n1 and n3 > n2:
        return 'O terceiro número é o maior número'


print(Maior(n1, n2, n3))


# ex066: Crie um programa que tenha uma função SuperSomador(), que vai receber dois números como parâmetro e depois vai retornar a soma de todos os valores no intervalo entre os valores recebidos.
# Ex:
# SuperSomador(1, 6) vai somar 1 + 2 + 3 + 4 + 5 + 6 e vai retornar 21
# SuperSomador(15, 19) vai somar 15 + 16 + 17 + 18 + 19 e vai retornar 85

def SuperSomador(n1, n2):
    soma = 0
    for i in range(n1, n2+1):
        a = i
        soma += a
    return f'Soma: {soma}'


print(SuperSomador(1, 6))
print(SuperSomador(4, 10))
print(SuperSomador(3, 9))
print(SuperSomador(15, 19))
print(SuperSomador(7, 14))


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


# ex068: Crie uma função que aceite kwargs e retorne a soma de todos os valores passados como argumentos.
def soma(*numeros):
    total = 0
    for numero in numeros:
        total += numero

    return f"O total é {total}"


print(soma(10, 20, 30, 40))  # O total é 100
print(soma(35, 78, 12, 38, 84, 437))  # O total é 684


# ex069: Crie uma função que recebe um texto e uma letra e verifica quantas vezes essa letra está presente no texto
def conta_letras(texto: str, letra: str):
    if len(letra) == 1:
        if letra in texto:
            contagem = texto.count(letra)
            return f"A letra aparece {contagem} vezes no texto."

        return "A letra não aparece no texto."

    return "A letra deve conter apenas um caractere."


if __name__ == "__main__":
    print(conta_letras("Python", "o"))  # A letra aparece 1 vez no texto.
    print(conta_letras("JavaScript", "a"))  # A letra aparece 2 vezes no texto.
    print(conta_letras("Branco", "Z"))  # A letra não aparece no texto.
    print(conta_letras("Amazônia", "ama"))  # A letra deve conter apenas um caractere.


# ex070: Exercício do FizzBuzz
def FizzBuzz():
    for number in range(1, 101):
        if number % 5 == 0 and number % 3 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


FizzBuzz()


# ex071: Crie uma função que recebe um número e faz uma contagem regressiva desse número
def contagem_regressiva(contagem: int):
    for numero in range(contagem, 0, -1):
        print(numero)


if __name__ == "__main__":
    contagem_regressiva(15)
    contagem_regressiva(5)
    contagem_regressiva(23)


# ex072: Crie um jogo de JoKenPo (Pedra-Papel-Tesoura) com o computador
from random import randint
computador = randint(1, 3)
escolha = input('pedra, papel ou tesoura? ').strip().lower()

computador = 'pedra' if computador == 1 else 'papel' if computador == 2 else 'tesoura'
print(f'A máquina escolheu {computador}')   

empate = computador == escolha

vitoria = (computador == "pedra" and escolha == "papel") or (computador == "papel" and escolha == "tesoura") or (computador == "tesoura" and escolha == "pedra")

derrota = (computador == "pedra" and escolha == "tesoura") or (computador == "papel" and escolha == "pedra") or (computador == "tesoura" and escolha == "papel")

print('Empate' if empate else 'Você ganhou! A máquina perdeu' if vitoria else 'Você perdeu! A máquina ganhou' if derrota else 'Escolha inválida! Digite "pedra", "papel" ou "tesoura"')


# ex073: Crie uma função que recebe uma lista e um elemento, e verifique se aquele elemento está ou não presente na lista
def verifica_elemento_na_lista(lista: list, elemento):
    if elemento in lista:
        indice_elemento = lista.index(elemento)
        return f"O elemento está na lista, no índice {indice_elemento}"

    return f"O elemento ({elemento}) não está presente na lista ({lista})"


if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5]
    print(verifica_elemento_na_lista(lista1, 2))  # O elemento está na lista, no índice 1

    lista2 = ["A", "B", "C", "D", "E"]
    print(verifica_elemento_na_lista(lista2, "Z"))  # O elemento (Z) não está presente na lista (['A', 'B', 'C', 'D', 'E'])

    lista3 = []
    print(verifica_elemento_na_lista(lista3, "A"))  # O elemento (A) não está presente na lista ([])


# ex074: Faça um programa que simule o lançamento de dois dados e exiba o resultado da soma.
from random import randint

def simulacao_dado():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)

    resultado = dado1 + dado2
    print(f'O resultado do dado 1 ({dado1}) com o dado 2 ({dado2}) é {resultado}')


simulacao_dado()


# ex075: Simule um caixa eletrônico, onde o usuário tem apenas 3 tentativas para digitar a senha correta. (senha="admin")
def caixa_eletronico():
    tentativas = 3

    while tentativas >= 1:
        senha = input("Olá, digite a sua senha:\n>>> ")

        if senha == "admin":
            print("Senha correta. Bem-vindo(a)!")
            tentativas = 0
        else:
            tentativas -= 1
            if tentativas != 0:
                print(f"Senha incorreta. Tentativas restantes: {tentativas}")
            else:
                print("Você excedeu o número máximo de tentativas. Tente novamente mais tarde.")


if __name__ == "__main__":
    caixa_eletronico()


# ex076: Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou não votar.
from datetime import datetime
nascimento = int(input('Digite a sua data de nascimento: '))

ano = datetime.now().year
idade = ano - nascimento

if idade >= 18:
    print('Você pode votar')
else:
    print(f'Você não pode votar, pois tem {idade} anos')


# ex077: Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
# a) Qual é a média de idade do grupo
# b) Quantas pessoas tem mais de 18 anos
# c) Quantas pessoas tem menos de 5 anos
# d) Qual foi a maior idade lida

idades = []
maior18 = menor5 = 0
for i in range(10):
    idade = int(input(f'Digite a idade da pessoa {i+1}: '))
    while idade < 0 or idade > 120:
        idade = int(input(f'Digite a idade corretamente {i+1}: '))
        
    idades.append(idade)

    if idade > 18:
        maior18 += 1

    if idade < 5:
        menor5 += 1

media = sum(idades) / len(idades)
maior = max(idades)

print(f'A média das idades é de {media}')
print(f'Há {maior18} pessoas maiores de 18 anos')
print(f'Há {menor5} pessoas menores de 5 anos')
print(f'A maior idade foi {maior}')


# ex078: Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
# a) Quantos homens foram cadastrados
# b) Quantas mulheres foram cadastradas
# c) A média de idade do grupo
# d) A média de idade dos homens
# e) Quantas mulheres tem mais de 20 anos

idades = []
grupo_homens = []
homens = mulheres = mulher_maior20 = 0
for i in range(5):
    idade = int(input(f'Digite a idade da pessoa {i+1}: '))
    sexo = input(f'Digite o sexo da pessoa {i+1} [M/F]: ').strip().upper()

    while sexo not in ['M', 'F']:
        sexo = input(f'O sexo deve ser M ou F: ').strip().upper()

    idades.append(idade)
    
    if sexo == 'M':
        grupo_homens.append(idade)
        homens += 1
    elif sexo == 'F':
        mulheres += 1
        if idade > 20:
            mulher_maior20 += 1

media = sum(idades) / len(idades)
media_homens = sum(grupo_homens) / len(grupo_homens)

print(f'Foram cadastrados {homens} {"homem" if homens == 1 else "homens"}')
print(f'Foram cadastradas {mulheres} {"mulher" if mulheres == 1 else "mulheres"}')
print(f'A média das idades é {media}')
print(f'A média das idades dos homens é {media_homens}')
print(f'Há {mulher_maior20} {"mulher" if mulher_maior20 == 1 else "mulheres"} com mais de 20 anos')


# ex079: Desenvolva um aplicativo que leia o peso e a altura de 5 pessoas, mostrando no final:
# a) Qual foi a média de altura do grupo
# b) Quantas pessoas pesam mais de 90Kg
# c) Quantas pessoas que pesam menos de 50Kg e tem menos de 1.60m
# d) Quantas pessoas que medem mais de 1.90m e pesam mais de 100Kg.

alturas = []
mais90 = peso50_alt160 = peso100_alt190 = 0
for i in range(5):
    peso = float(input(f'Digite o peso da pessoa {i+1}: '))
    altura = float(input(f'Digite a altura da pessoa {i+1}: '))

    alturas.append(altura)

    if peso > 90:
        mais90 += 1
    
    if peso < 50 and altura < 1.60:
        peso50_alt160 += 1
    
    if peso > 100 and altura > 1.90:
        peso100_alt190 += 1


media = sum(alturas) / len(alturas) / 10

print(f'A média das alturas é de {media}')
print(f'Há {mais90} {"pessoa que pesa" if mais90 == 1 else "pessoas que pesam"} mais de 90 quilos')
print(f'Há {peso50_alt160} {"pessoa que pesa" if peso50_alt160 == 1 else "pessoas que pesam"}  menos de 50 quilos e tem menos de 1.60m')
print(f'Há {peso100_alt190} {"pessoa que pesa" if peso100_alt190 == 1 else "pessoas que pesam"} mais de 100 quilos e tem mais de 1.90m')


# ex080: Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários. No final, mostre o total de salários pagos aos homens e o total pago às mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não sempre que ler os dados de um funcionário.

salarios_homens = []
salarios_mulheres = []
while True:
    salario = float(input('Digite o salário: '))
    sexo = input('Digite o sexo [M/F]: ').strip().upper()

    while sexo not in ['M', 'F']:
        sexo = input('Digite corretamente [M/F]: ').strip().upper()

    if sexo == 'M':
        salarios_homens.append(salario)
    elif sexo == 'F':
        salarios_mulheres.append(salario)

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Digite corretamente [S/N]: ').strip().upper()
    if continuar == 'N':
        break 
    elif continuar == 'S':
        continue

homens = sum(salarios_homens)
mulheres = sum(salarios_mulheres)

print(f'O salário total dos homens é {homens}')
print(f'Já o salário total das mulheres é {mulheres}')


# ex081: Faça um algoritmo que leia a nota de vários alunos de uma turma. O programa vai parar quando for digitada a nota 999. No final, mostre quantos alunos existem na turma e qual é a média de notas do grupo.

notas = []
alunos = 0
while True:
    nota = int(input(f'Digite a nota do aluno [999 = sair]: '))
    while nota < 0 or nota > 10 and nota != 999:
        nota = int(input(f'Digite corretamente [999 = sair]: '))
    if nota == 999:
        break



    alunos += 1
    notas.append(nota)

if len(notas) > 1:
    media = sum(notas) / len(notas)
    print(f'Nessa turma, existem {alunos} alunos')
    print(f'A média de notas da turma é de {media}')


# ex082: Crie um programa que leia o sexo e a idade de várias pessoas. O programa vai perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre:
# a) qual é a maior idade lida
# b) quantos homens foram cadastrados
# c) qual é a idade da mulher mais jovem
# d) qual é a média de idade entre os homens

idades = []
idades_homens = []
idades_mulheres = []
while True:
    idade = int(input('Digite a idade: '))

    sexo = input('Digite o sexo [M/F]: ').strip().upper()
    while sexo not in ['M', 'F']:
        sexo = input('Digite corretamente [M/F]: ').strip().upper()
    
    idades.append(idade)

    if sexo == 'M':
        idades_homens.append(idade)
    elif sexo == 'F':
        idades_mulheres.append(idade)


    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue


maior = max(idades)
homens = len(idades_homens)
mulher_jovem = min(idades_mulheres)
media = sum(idades_homens) / len(idades_homens)

print(f'A maior idade é {maior}')
print(f'Foram cadastrados {homens} {"homem" if homens == 1 else "homens"}')
print(f'A idade da mulher mais jovem é {mulher_jovem}')
print(f'A média da idade dos homens é de {media}')


# ex083: Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas. O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
# a) O nome da pessoa mais velha
# b) O nome da mulher mais jovem
# c) A média de idade do grupo
# d) Quantos homens tem mais de 30 anos
# e) Quantas mulheres tem menos de 18 anos

nomes = []
idades = []
homens30 = mulheres18 = 0
while True:
    nome = input('Digite o nome: ').strip().title()
    idade = int(input('Digite a idade: '))

    sexo = input('Digite o sexo [M/F]: ').strip().upper()
    while sexo not in ['M', 'F']:
        sexo = input('Digite corretamente [M/F]: ').strip().upper()

    if sexo == 'M':
        if idade > 30:
            homens30 += 1
    elif sexo == 'F':
        if idade < 18:
            mulheres18 += 1
    nomes.append(nome)
    idades.append(idade)

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue

velho = idades.index(max(idades))
jovem = idades.index(min(idades))
media = sum(idades) / len(idades)
print(f'O nome da pessoa mais velha é {nomes[velho]}, e tem {idades[velho]} anos')
print(f'A pessoa mais jovem é {nomes[jovem]}, e tem {idades[jovem]} anos')
print(f'A média das idades é de {media}')
print(f'Há {homens30} {"homem" if homens30 == 1 else "homens"} com mais de 30 anos')
print(f'Há {mulheres18} {"mulher" if mulheres18 == 1 else "mulheres"} com menos de 18 anos')


# ex084: Faça um programa usando a estrutura “faça enquanto” que leia a idade de várias pessoas. A cada laço, você deverá perguntar para o usuário se ele quer ou não continuar a digitar dados. No final, quando o usuário decidir parar, mostre na tela:
# a) Quantas idades foram digitadas
# b) Qual é a média entre as idades digitadas
# c) Quantas pessoas tem 21 anos ou mais.

idades = []
idade21 = 0
while True:
    idade = int(input('Digite a idade: '))

    idades.append(idade)

    if idade > 21:
        idade21 += 1

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue

media = sum(idades) / len(idades)
print(f'Há {len(idades)} idades cadastradas')
print(f'A média das idades é de {round(media, 2)}')
print(f'Há {idade21} {"pessoa" if len(idades) == 1 else "pessoas"} com mais de 21 anos.')


# ex085: Crie um programa usando a estrutura “faça enquanto” que leia vários números. A cada laço, pergunte se o usuário quer continuar ou não. No final, mostre na tela:
# a) O somatório entre todos os valores
# b) Qual foi o menor valor digitado
# c) A média entre todos os valores
# d) Quantos valores são pares

numeros = []
pares = 0
while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)

    pares += 1

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue

media = sum(numeros) / len(numeros)
menor = numeros.index(min(numeros))

print(f'A soma de todos os valores é de {sum(numeros)}')
print(f'O menor número digitado foi {numeros[menor]}, e aparece na {numeros.index(numeros[menor])+1}ª posição')
print(f'A média dos números é de {round(media, 2)}')
print(f'Há {pares} números {"par" if pares == 1 else "pares"}')


# ex086: Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura “para”. No final, mostre na tela:
# a) Quantas mulheres foram cadastradas
# b) Quantos homens pesam mais de 100Kg
# c) A média de peso entre as mulheres
# d) O maior peso entre os homens

homem_peso100 = mulheres = 0
peso_homens = []
peso_mulheres = []
for i in range(8):
    sexo = input('Digite o sexo [M/F]: ').strip().upper()
    while sexo not in ['M', 'F']:
        sexo = input('Digite corretamente [M/F]: ').strip().upper()

    peso = float(input('Digite o peso: '))

    if sexo == 'F':
        peso_mulheres.append(peso)
        mulheres += 1
    if sexo == 'M':
        peso_homens.append(peso)
        if peso > 100:
            homem_peso100 += 1


maior = peso_homens.index(max(peso_homens))
media_mulheres = sum(peso_mulheres) / len(peso_mulheres)
print(f'Foram cadastradas {mulheres} {"mulher" if mulheres == 1 else "mulheres"}')
print(f'Há {homem_peso100} {"homem" if homem_peso100 == 1 else "homens"} com mais de 100Kg.')
print(f'A média de pesos entre as mulheres é de {media_mulheres}')
print(f'O maior peso entre os homens foi de {peso_homens[maior]}')


# ex087: Crie uma função que calcule a tabuada de 0 até o número que o usuário digitou.
def tabuada(numero_tabuada: int):
    if numero_tabuada < 1 or numero_tabuada > 1_000_000:
        print("O número deve estar entre 1 a 1 milhão.")
        return False

    for numero in range(0, 11):
        resultado = numero * numero_tabuada
        print(f"{numero_tabuada} * {numero} = {resultado}")


if __name__ == "__main__":
    tabuada(7)
    tabuada(45)
    tabuada(154)


# ex088: Smith criou uma loja de produtos. Ele tem uma conta especial para ele mesmo, com mais de 100 mil clientes em sua loja. Ele precisa que você crie uma função que retorne uma mensagem agradável se a senha for a de Smith. Caso contrário, retorne uma mensagem de boas-vindas ao Cliente.
def verifica_usuario(usuario, senha):
    if usuario == "admin" and senha == 'admin':
        return 'O Criador entrou!'

    return 'Olá, usuário!'


if __name__ == "__main__":
    print(verifica_usuario("SmithFan", "ILoveSmith"))  # Olá, usuário!
    print(verifica_usuario("admin", "admin"))  # O Criador entrou!
    print(verifica_usuario("Smith", "password"))  # Olá, usuário!


# ex089: Crie uma função que receba um número como parâmetro e retorne todos os números pares de 0 até este número.
def encontra_pares(numero: int):
    if numero < 1 or numero > 1_000_000:
        return "O número deve estar entre 1 a 1 milhão."

    pares = [par for par in range(numero+1) if par % 2 == 0]
    return f"Os números pares de 0 até {numero} são: {pares}"


if __name__ == "__main__":
    print(encontra_pares(12))  # Os números pares de 0 até 12 são: [0, 2, 4, 6, 8, 10, 12]
    print(encontra_pares(450))  # Os números pares de 0 até 450 são: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 254, 256, 258, 260, 262, 264, 266, 268, 270, 272, 274, 276, 278, 280, 282, 284, 286, 288, 290, 292, 294, 296, 298, 300, 302, 304, 306, 308, 310, 312, 314, 316, 318, 320, 322, 324, 326, 328, 330, 332, 334, 336, 338, 340, 342, 344, 346, 348, 350, 352, 354, 356, 358, 360, 362, 364, 366, 368, 370, 372, 374, 376, 378, 380, 382, 384, 386, 388, 390, 392, 394, 396, 398, 400, 402, 404, 406, 408, 410, 412, 414, 416, 418, 420, 422, 424, 426, 428, 430, 432, 434, 436, 438, 440, 442, 444, 446, 448, 450]
    print(encontra_pares(1))  # Os números pares de 0 até 1 são: [0]


# ex090: Crie um programa que realiza a contagem regressiva de 5 segundos
from time import sleep

def contagem_regressiva():
    for i in range(5, 0, -1):
        print(i)
        sleep(1)


contagem_regressiva()


# ex091: Crie uma função que receba um número e imprima uma escada de estrelas (asteriscos)
def piramide_de_estrelas(quantidade: int):
    if quantidade < 1 or quantidade > 100:
        print("A quantidade deve estar entre 1 a 100.")
        return None

    for numero in range(1, quantidade+1):
        print("*" * numero)


quantidade = int(input("Digite a quantidade de 1 a 100:\n>>> "))
piramide_de_estrelas(quantidade)


# ex092: Inverta o exercício 11 - imprima uma escada de estrelas invertidas
def piramide_de_estrelas(quantidade: int):
    if quantidade < 1 or quantidade > 100:
        print("A quantidade deve estar entre 1 a 100.")
        return None

    for numero in range(quantidade, 0, -1):
        print("*" * numero)


quantidade = int(input("Digite a quantidade de 1 a 100:\n>>> "))
piramide_de_estrelas(quantidade)


# ex093: Crie uma função que retorne o primeiro elemento de uma lista
def retorna_primeiro_elemento(lista: list):
    if len(lista) > 0:
        return f"O primeiro elemento da lista é {lista[0]}"

    return "A lista deve possuir ao menos um elemento."

if __name__ == "__main__":
    lista1 = ["Maçã", "Banana", "Laranja", "Abacaxi"]
    print(retorna_primeiro_elemento(lista1))  # O primeiro elemento da lista é Maçã

    lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # O primeiro elemento da lista é 1
    print(retorna_primeiro_elemento(lista2))

    lista3 = []
    print(retorna_primeiro_elemento(lista3))  # A lista deve possuir ao menos um elemento.


# ex094: Ingressos de cinema: Um cinema cobra preços de ingressos diferentes, dependendo da idade da pessoa. Se a pessoa for menor de 3 anos, o ingresso é gratuito; se tiver entre 3 e 12 anos, o ingresso custa U$S10; e caso tenha mais de 12 anos, o ingresso custa US$15. Escreva um loop que pergunte a idade dos usuários e, em seguida, informe o preço do ingresso do cinema.
def ingressos_cinema(pessoas: int):
    if pessoas < 1 or pessoas > 50:
        return f"O limite de pessoas foi alcançado."

    preco = 0
    for i in range(pessoas):
        idade = int(input(f'Digite a idade da pessoa {i+1}: '))
        while idade < 1 or idade > 120:
            idade = int(input(f'A idade excedeu o limite.\nDigite a idade da pessoa {i+1}: '))

        if idade < 3: # Se idade for menor que 3, ingresso gratuito
            ingresso = 0
        elif idade >= 3 and idade <= 12: # Se idade estiver entre 3 e 12, ingresso custa 10 reais.
            ingresso = 10
        elif idade > 12: # Se idade for maior que 12, ingresso custa 15 reais
            ingresso = 15

        preco += ingresso

    return f"O preço total dos ingressos é de R${preco} reais."


if __name__ == "__main__":
    pessoas = int(input("Digite a quantidade de pessoas: "))
    print(ingressos_cinema(pessoas))


# ex095: Crie um programa que preencha automaticamente um vetor numérico com 7 números gerados aleatoriamente pelo computador e depois mostre os valores gerados na tela.
import random

vetor = [[], [], [], [], [], [], []]

for i in range(7):
    vetor[i] = random.randint(1, 10)

print(vetor)


# ex096: Crie uma uma função que retorne a maior palavra de uma string.
def biggest_word(text: str):
    if len(text) < 1 or len(text) > 10000:
        return "Texto inválido."

    words = text.split()

    lenghts = list(map(len, words))
    position = lenghts.index(max(lenghts))

    word = words[position]
    return word


if __name__ == "__main__":
    print(biggest_word(""))  # Texto inválido.
    print(biggest_word("# a b c d"))  # #
    print(biggest_word("Tor is the best anonymous and security browser")) # anonymous


# ex097: Crie um programa que receba o nome de um arquivo como parâmetro e retorne o conteúdo do arquivo
def retorna_conteudo_arquivo(arquivo: str):
    try:
        with open(arquivo, 'r', encoding="utf-8") as f:
            f.seek(0)
            conteudo = f.read()

            return f"Conteúdo:\n---------------------------------------\n{conteudo}\n---------------------------------------"
    except FileNotFoundError as file_found_e:
        return f"Arquivo não encontrado: {file_found_e}"
    except OSError as os_e:
        return f"Erro de sistema: {os_e}"
    except SyntaxError as syntax_e:
        return f"Erro de sintaxe: {syntax_e}"
    except NameError as name_e:
        return f"Erro de nome: {name_e}"
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    print(retorna_conteudo_arquivo("arquivo.txt"))  # [conteúdo]
    print(retorna_conteudo_arquivo("README.md"))  # Arquivo não encontrado: [Errno 2] No such file or directory: 'README.md'
    print(retorna_conteudo_arquivo(7))  # Erro de sistema: [WinError 6] Identificador inválido


# ex098: Crie uma função que receba uma string como parâmetro e retorne a string sem a primeira letra
def retorna_sem_primeira_letra(string: str):
    try:
        return string[1:]
    except AttributeError as attr_e:
        return f"O argumento deve ser uma string. Erro: {attr_e}"
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    print(retorna_sem_primeira_letra("Olá, mundo!"))  # "lá, mundo!"
    print(retorna_sem_primeira_letra("Python"))  # "ython"
    print(retorna_sem_primeira_letra(""))  # ""
    print(retorna_sem_primeira_letra(23))  # Erro: 'int' object is not subscriptable


# ex099: Crie uma função que retorne o maior valor de dois números
def retorna_maior_valor(n1: int, n2: int):
    try:
        if not isinstance(n1, (int, float)) or not isinstance(n2, (int, float)):
            return "Valores inválidos."

        # Maneira 1
        # maior_valor = max(n1, n2)
        # return f"O maior valor é {maior_valor}"

        # Maneira 2
        if n1 > n2:
            return f"O maior valor é {n1}, no índice 0."
        elif n1 < n2:
            return f"O maior valor é {n2}, no índice 1."

        return "Ambos possuem o mesmo valor."
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    print(retorna_maior_valor(15, 24))  # O maior valor é 24
    print(retorna_maior_valor(12, 12))  # Ambos possuem o mesmo valor.
    print(retorna_maior_valor("Python", "JS"))  # Valores inválidos.
    print(retorna_maior_valor(True, False))  # O maior valor é True, no índice 0. (cry)


# ex100: Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua situação em relação ao alistamento militar.
# - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o alistamento.
# - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do alistamento.

from datetime import datetime
nascimento = int(input('Digite a sua data de nascimento: '))

ano = datetime.now().year
idade = ano - nascimento

if idade < 18:
    falta = 18 - idade
    print(f'Faltam {falta} anos')
else:
    passou = idade - 18
    print(f'Já se passou {passou} anos')


# ex101: Crie um jogo onde o computador vai sortear um número entre 1 e 5 o jogador vai tentar descobrir qual foi o valor sorteado.
from random import randint

computador = randint(1, 5)
escolha = int(input('Tente adivinhar o número entre 1 a 5: '))

while escolha <= 0 or escolha > 5:
    escolha = int(input('Por favor, escolha um número entre 1 a 5: '))

print(f'Você acertou' if escolha == computador else f'Você errou, o número era {computador}')


# ex102: # Faça um aplicativo onde o computador deve sortear um número entre 1 e 10 e o jogador tem 4 tentativas para tentar acertar
from random import randint

computador = randint(1, 10)

for i in range(4):
    print(f'⏳Tentativa {i+1}/4⏳'.center(50, '-'))

    escolha = int(input('Tente adivinhar o número entre 1 a 10: '))
    while escolha <= 0 or escolha > 10:
        escolha = int(input('❓Por favor, escolha um número entre 1 a 10❓: '))
    
    if escolha == computador:
        print('🎇 Você acertou!🎇')
        break
    else:
        if i == 3:
            print(f'🎈O número era {computador}🎈')
        else:
            print('❌ Você errou. Tente novamente❌')


# ex103: Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem.
def salario_funcionario():
    try:
        funcionario = input('Digite o nome do funcionário: ')
        salario = float(input('Digite o salário do funcionário: '))
    except ValueError as value_e:
        return f"O salário deve ser um número. Erro: {value_e}"
    except Exception as e:
        return f"Ocorreu um erro: {e}"

    return f'O(a) funcionário(a) {funcionario} tem um salário de R${salario}.'


if __name__ == "__main__":
    print(salario_funcionario())
    # if salario_funcionario(salario="e") -> O salário deve ser um número. Erro: could not convert string to float: 'e'


# ex104: Conte quantas linhas tem um arquivo.

def conta_linhas_arquivo(arquivo: str):
    try:
        with open(arquivo, "r", encoding="utf-8") as arquivo:
            arquivo.seek(0)

            linhas = 0
            for _ in arquivo.readlines():
                linhas += 1
            arquivo.seek(0)

            return f"Quantidade de linhas encontradas: {linhas}"
    except FileNotFoundError:
        return "Erro: Arquivo não encontrado/não existe. Verifique o caminho do arquivo ou crie um."
    except Exception as erro:
        return f"Erro: {erro}"


print(conta_linhas_arquivo("arquivo.txt"))


# ex105: Faça um programa que leia um número menor que 1000 e imprima centenas, dezenas e unidades.

def decomposicao(numero: int) -> str:
    if numero < 1 or numero >= 1000:
        return "O número deve ser maior ou igual a 1 e menor que 1000"

    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    return f"Centenas: {centenas} | Dezenas: {dezenas} | Unidades: {unidades}"


def main():
    try:
        numero = int(input("Digite um número entre 1 e 999: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return

    print(decomposicao(numero))


if __name__ == "__main__":
    main()


# ex106: Crie uma função que tem uma string como parâmetro e verifica se a string é um palíndromo.
def verifica_palindromo(string: str):
    try:
        if len(string) < 1:
            return "A string deve ter ao mínimo 1 caractere."

        if string[::-1].lower() == string.lower():
            return "A string é um palíndromo."
    except TypeError as type_e:
        return f"A string deve conter apenas letras. Erro: {type_e}"
    except Exception as e:
        return f"Erro: {e}"

    return "A string não é um palíndromo."


if __name__ == "__main__":
    print(verifica_palindromo("radar"))  # A string é um palíndromo.
    print(verifica_palindromo("Ana"))  # A string é um palíndromo.
    print(verifica_palindromo(""))  # A string deve ter ao mínimo 1 caractere.
    print(verifica_palindromo(12345))  # A string deve ter ao mínimo 1 caractere.


# ex107: Faça um programa que verifique se uma letra digitada é vogal ou consoante.
def verifica_vogal_consoante(letra: str):
    vogais = ['a', 'á', 'à', 'ã', 'â', 'e', 'é', 'è', 'ê', 'í', 'ì', 'î', 'i', 'o', 'ó', 'ò', 'ô', 'õ', 'ú', 'ù', 'û', 'u']

    try:
        if not letra.isalpha() or len(letra) != 1:
            return 'Por favor, digite uma letra válida'
    except AttributeError as attr_e:
        return f"A função aceita apenas letras. Erro: {attr_e}"
    except Exception as e:
        return f"Erro: {e}"

    if letra.lower() in vogais:
        return f'vogal'

    return f'consoante'


if __name__ == "__main__":
    print(verifica_vogal_consoante("a"))  # vogal
    print(verifica_vogal_consoante(6))  # A função aceita apenas letras. Erro: 'int' object has no attribute 'isalpha'
    print(verifica_vogal_consoante(""))  # Por favor, digite uma letra válida
    print(verifica_vogal_consoante("ABC"))  # Por favor, digite uma letra válida
    print(verifica_vogal_consoante("é"))  # vogal
    print(verifica_vogal_consoante("w"))  # consoante


# ex108: Crie uma função que receba um texto como parâmetro e retorne a quantidade de palavras no texto.
def retorna_quantidade_palavras(texto: str):
    try:
        palavras = texto.split()
        quantidade_palavras = len(palavras)

        return f"A quantidade de palavras é de {quantidade_palavras}"
    except TypeError as type_e:
        return f"A função aceita apenas strings. Erro: {type_e}"


if __name__ == "__main__":
    print(retorna_quantidade_palavras("Python foi criado por Guido van Rossum"))  # A quantidade de palavras é de 7
    print(retorna_quantidade_palavras("Lorem, ipsum dolor sit amet consectetur adipisicing elit. Placeat illo aut eius totam quaerat ad expedita ducimus explicabo, asperiores eaque, doloremque labore fugiat consequuntur, voluptatum nobis veniam quae animi hic!"))  # A quantidade de palavras é de 30


# ex109: Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e mostre na tela:
# a) Quais foram os números sorteados
# b) Quantos números estão acima de 5
# c) Quantos números são divisíveis por 3
from random import randint

numeros = []
acima5 = div3 = 0

for i in range(20):
    numero = randint(0, 10)
    numeros.append(numero)

    if numero > 5:
        acima5 += 1

    if numero % 3 == 0:
        div3 += 1

print(f'Os números sorteados foram {numeros}')
print(f'São {acima5} números sorteados acima de 5')
print(f'São {div3} números sorteados que são divisíveis por 3')


# ex110: Crie uma função que recebe uma lista como parâmetro e retorne quais elementos NÃO são repetidos
def verifica_nao_repetidos(lista: list):
    if len(lista) < 1:
        return "A lista deve possuir ao menos 1 elemento."

    nao_repetidos = []
    for elemento in lista:
        if lista.count(elemento) == 1:
            nao_repetidos.append(elemento)

    if len(nao_repetidos) > 0:
        return f"Os elementos não repetidos são: {nao_repetidos}"

    return "Todos os itens se repetem."


if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Os elementos não repetidos são: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(verifica_nao_repetidos(lista1))

    lista2 = ["a", "b", "a", "c"]
    print(verifica_nao_repetidos(lista2))  # Os elementos não repetidos são: ['b', 'c']

    lista3 = []
    print(verifica_nao_repetidos(lista3))  # A lista deve possuir ao menos 1 elemento.

    lista4 = ["a"]
    print(verifica_nao_repetidos(lista4))  # Os elementos não repetidos são: ['a']

    lista5 = ["a", "a", "a"]
    print(verifica_nao_repetidos(lista5))  # Todos os itens se repetem.


# ex111: Um grupo de amigos decidiu criar uma sociedade secrta. O nome dessa sociedade será a primeira letra de cada nome do grupo de amigos. Crie uma função que receba uma lista de nomes e retorne o nome da sociedade secreta.
def nome_sociedade_secreta(membros: list):
    nome = ""

    if len(membros) < 2:
        return "A lista deve possuir ao menos dois membros."

    for membro in membros:
        primeira_letra = membro[0]
        nome += primeira_letra

    return f"Nome da sociedade: {nome}"


if __name__ == "__main__":
    print(nome_sociedade_secreta(["João", "Maria", "Pedro", "Ana"]))  # Nome da sociedade: JMPA
    print(nome_sociedade_secreta(["Pedro", "Gabriel", "Gustavo", "Renata", "Marcos", "José"]))  # Nome da sociedade: PGGRMJ
    print(nome_sociedade_secreta(["Marcos"]))  # A lista deve possuir ao menos dois membros.
    print(nome_sociedade_secreta(["Marcos", "Felipe"]))  # Nome da sociedade: MF


# ex112: Crie um programa que verifica em que posições há disjuntores ligados e desligados
def verifica_posicoes_disjuntores(disjuntores: list):
    lista_pos = []

    if isinstance(disjuntores, list):
        for pos, disjuntor in enumerate(disjuntores):
            if isinstance(disjuntor, bool) and disjuntor:
                lista_pos.append(pos)

    if len(lista_pos) == 0:
        return "Nenhuma posição."

    return f"Lista de posições: {lista_pos}"


if __name__ == "__main__":
    lista1 = [True, True, False, False, True, False, False, False, True]
    print(verifica_posicoes_disjuntores(lista1))  # Lista de posições: [0, 1, 4, 8]

    lista2 = [False, True, False, False, False, True, True]
    print(verifica_posicoes_disjuntores(lista2))  # Lista de posições: [1, 5, 6]

    lista3 = [True, False, False, True, True, False, False]
    print(verifica_posicoes_disjuntores(lista3))  # Lista de posições: [0, 3, 4]

    lista4 = [1, 4, 6, 7, "Python"]
    print(verifica_posicoes_disjuntores(lista4))  # Nenhuma posição.


# ex113: Crie uma função que retorne a soma de todos os valores de um número
def sum_numbers(number: int):
    if number < 1 or number > 10000000:
        return "O número deve estar entre 1 a 10.000.000"

    number_list = []

    for num in str(number):
        number_list.append(int(num))

    sum_numbers = sum(number_list)
    return sum_numbers


if __name__ == "__main__":
    print(sum_numbers(548))  # 5 + 4 + 8 = 17
    print(sum_numbers(77732))  # 7 + 7 + 7 + 3 + 2 = 26
    print(sum_numbers(301))  # 3 + 0 + 1 = 4


# ex114: Crie uma função que retorne a soma de todos os valores de uma lista
def soma_valores_lista(lista: list):
    if len(lista) > 1:
        try:
            soma = sum(lista)
            return f"A soma de todos os elementos da lista é de {soma}"
        except TypeError:
            return "A lista deve conter apenas números."
        except Exception as e:
            return f"Erro: {e}"

    return "A lista deve contér mais de um elemento."   


if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(soma_valores_lista(lista1))  # A soma de todos os elementos da lista é de 55

    lista2 = [2, 2]
    print(soma_valores_lista(lista2))  # A soma de todos os elementos da lista é de 4

    lista3 = []
    print(soma_valores_lista(lista3))  # A lista deve contér mais de um elemento.

    lista4 = ["Python", "JavaScript", "HTML", "CSS"]
    print(soma_valores_lista(lista4))  # A lista deve conter apenas números.


# ex115: Faça uma função que conta o número de vogais em uma string.
def count_vowels(string: str):
    if len(string) < 1 or len(string) > 250:
        return "O tamanho da string deve estar entre 1 a 250."

    try:
        VOWELS = ["a", "e", "i", "o", "u"]

        count = 0
        for letter in string.lower():
            if letter in VOWELS:
                count += 1

        return count
    except ValueError as value_e:
        return f"Erro de valor: {value_e}"
    except KeyboardInterrupt as keyboard_e:
        return f"Erro de teclado: {keyboard_e}"
    except TypeError as type_e:
        return f"Erro de tipo: {type_e}"
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    print(count_vowels("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))  # 5
    print(count_vowels("Existe uma cobra chamada Python."))  # 11
    print(count_vowels("Eistein é o maior cientista de todos os tempos."))  # 18
    print(count_vowels(""))  # O tamanho da string deve estar entre 1 a 250.
    print(count_vowels("Lorem, ipsum dolor sit amet consectetur adipisicing elit. Provident facilis sequi voluptas, veritatis quaerat id repellendus blanditiis quo corporis, quis tempore obcaecati amet? Error, qui! Quam quidem consectetur tempore inventore? Placeat, saepe atque natus recusandae neque porro vel repellendus inventore molestiae ut?"))  # O tamanho da string deve estar entre 1 a 250.


# ex116: Crie uma classe chamada User. Crie dois atributos chamados nome e sobrenome e diversos outros atributos que normalmente são armazenados em um perfil de usuário. Crie um método chamado describe_user() que exiba um resumo das informações do usuário. Crie outro método chamado greet_user que exiba um cumprimento personalizado ao usuário.
class User:
    def __init__(self, ID: int = None, nome: str = None, sobrenome: str = None, idade: int = None, nascimento: str = None):
        self.ID = ID
        self.nome = nome.title()
        self.sobrenome = sobrenome.title()
        self.idade = idade
        self.nascimento = nascimento

    def describe_user(self):
        print(f'ID: {self.ID}, nome: {self.nome}, sobrenome: {self.sobrenome}, idade: {self.idade}, nascimento: {self.nascimento}')
  
    def greet_user(self):
        print(f'Olá, {self.nome} {self.sobrenome}!')

    def login(self):
        senha = input('Digite a sua senha: ')
        tentativas = 1
        while True:
            senha = int(input('Digite corretamente: '))
            if senha == 123456:
                print(f"Olá, {self.nome}. Seja bem-vindo(a).")
                break
            else:
                tentativas += 1
                print(f'Senha incorreta! {tentativas} tentativas já foram feitas.')


pedro = User(4, 'Pedro', 'Feitosa', 16, '23/06/2009')
pedro.describe_user()
pedro.greet_user()
pedro.login()


# ex117: # Escreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório desses números na tela. Após exibir a soma, o programa deve mostrar também os números que o usuário digitou, um por linha.
def mostrar_soma_e_numeros():
    numeros = []
    total = 0

    try:
        for i in range(5):
            numero = int(input(f'Digite o número {i+1}: '))

            numeros.append(numero)
            total += numero
    except ValueError as value_e:
        return f"A lista pode conter apenas números. Erro: {value_e}"
    except Exception as e:
        return f"Erro: {e}"

    return (f'A soma dos números digitados é {total}\n'
            f'Os números digitados foram: {numeros}')


if __name__ == "__main__":
    print(mostrar_soma_e_numeros())


# ex118: Crie uma programa que pede ao usuário 10 números, e separe e armazene números pares e números ímpares em duas listas diferentes.
def separar_pares_impares():
    pares = []
    impares = []

    try:
        for numero in range(10):
            numero = int(input(f'Digite o número {numero+1}: '))
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)
    except ValueError as value_e:
        return f"A lista pode conter apenas números. Erro: {value_e}"
    except Exception as e:
        return f"Erro: {e}"

    return (
        f"Lista de números pares: {pares}\n"
        f"Lista de números ímpares: {impares}"
    )


if __name__ == "__main__":
    print(separar_pares_impares())


# ex119: Crie uma função que receba uma lista e retorne "Par", se existe mais números pares, caso contrário, retorne "Ímpar".
def verifica_pares_impares(lista: list):
    pares = 0
    impares = 0

    if len(lista) < 1:
        return "A lista deve ter a menos um número."

    try:
        for numero in lista:
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1

        if pares > impares:
            return "Par"
        elif impares > pares:
            return "Ímpar"

        return "Pares e Ímpares"
    except TypeError:
        return "A lista deve conter apenas números."
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    lista1 = [12, 13, 14, 15, 16, 17, 18, 19, 20]  # Par
    print(verifica_pares_impares(lista1))

    lista2 = [2, 4, 1, 3]
    print(verifica_pares_impares(lista2))  # Pares e Ímpares

    lista3 = ["Par", "Ímpar"]
    print(verifica_pares_impares(lista3))  # A lista deve conter apenas números.


# ex120: Crie uma função que receba uma lista de números como parâmetro e retorne a média de números daquela lista.
def retorna_media(lista: int):
    if len(lista) < 2:
        return "A lista deve ter ao menos 2 elementos."

    try:
        soma = sum(lista)
        media = soma / len(lista)

        return f"A média de números da lista é de: {media}"
    except TypeError as type_e:
        return f"A lista deve conter apenas números. Erro: {type_e}"
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    print(retorna_media([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # A média de números da lista é de: 5.0
    print(retorna_media(["a", "b", "c"]))  # A lista deve conter apenas números. Erro: unsupported operand type(s) for +: 'int' and 'str'
    print(retorna_media([]))  # A lista deve ter ao menos 2 elementos.


# ex121: Crie um programa que simule um jogo de "cara ou coroa" com estatísticas de vitórias.
from random import randint


def cara_ou_coroa(quantidade: int):
    if quantidade > 100 or quantidade < 1:
        return "A quantidade de tentativas deve ser menor que 100 e maior que 1."

    resultados = []
    for _ in range(quantidade):
        moeda = randint(0, 1)

        if not moeda:
            resultados.append("Cara")
        else:
            resultados.append("Coroa")

    return (
        f"Resultados: {", ".join(resultados)}\n"
        f"Qntd. de vezes que caiu Cara: {resultados.count("Cara")}\n"
        f"Qntd. de vezes que caiu Coroa: {resultados.count("Coroa")}\n"
    )


quantidade = int(input("Quantas vezes deseja jogar?\n>>> "))
print(cara_ou_coroa(quantidade))


# ex122: Crie um programa em que pede ao usuário um número e o programa deve retornar se este número é uma raíz exata ou não.
import math

while True:
    try:
        numero = int(input("Digite um número inteiro:\n>>>"))

        def verifica_raiz_exata(numero: int):
            raiz = math.sqrt(numero)

            if raiz.is_integer():
                yield f"{numero} é uma raíz quadrada exata"
            else:
                yield f"{numero} não é uma raíz quadrada exata"

            yield f"Resultado da raíz: {raiz}"

        for i in verifica_raiz_exata(numero):
            print(i)

    except ValueError:
        print("Por favor, digite um número inteiro\n")
    else:
        break


# ex123: Faça um simulador de dado
from random import randint


def simular_dado(quantidade: int):
    if quantidade > 10000 or quantidade < 1:
        yield "A quantidade de tentativas deve ser menor que 10000 e maior que 0."
        return None

    resultados = []
    for _ in range(quantidade):
        dado = randint(1, 6)

        resultados.append(dado)

    for i in range(1, 7):
        yield f"Dado caiu em {i}: {resultados.count(i)} vezes."

    yield f"Resultados: {resultados}"


try:
    quantidade = int(input("Digite a quantidade de vezes para sortear o dado:\n>>> "))
except ValueError:
    print("Valor inválido. Digite um número!")
except Exception as erro:
    print(f"Erro: {erro}")
else:
    for item in simular_dado(quantidade):
        print(item)


# ex124: Crie uma função que conta quantas letras há numa string.
def count_letters(text):
    already_list = []

    for letter in text:
        if letter.isalpha():
            if letter not in already_list:
                already_list.append(letter)
                print(f"{letter}: {text.count(letter)}")

if __name__ == "__main__":
    count_letters("Contador de Letras com Python!")
    count_letters("JavaScript ou Python?")
    count_letters("AAA BBB CCC DDD EEE")


# ex125: Crie uma função que conta quantas palavras há numa string.
def count_words(text):
    splitted_text = text.split()
    already_list = []

    for element in splitted_text:
        if element not in already_list:
            already_list.append(element)
            print(f"{element}: {splitted_text.count(element)}")

if __name__ == "__main__":
    count_words("Hello world! Hello Python!")
    count_words("Olá mundo! Olá Python!")


# ex126: Crie uma função que: Verifica se um número é primo; Mostra a quantidade de divisores; e quais são eles.
def prime_number(number: int):
    if number < 1 or number > 100000:
        return "The number need to be in a range of 2 and 100000."

    if number == 2:
        return True

    primes = []
    counter = 0
    number_range = range(1, number+1)

    for num in number_range:
        if number % num == 0:
            counter += 1
            primes.append(num)

    return (
    "----------------------------------\n"
    f"Número: {number}\n"
    f"Primo: {counter == 2}\n"
    f"Quant. Divisores: {counter}\n"
    f"Divisores: {primes}"
    "\n----------------------------------\n"
    )

if __name__ == "__main__":
    print(prime_number(16))
    print(prime_number(25))
    print(prime_number(3301))  # Cidada3301!
    print(prime_number(2597))


# ex127: Crie uma função que remove itens duplicados de uma lista, sem usar set.
def remove_duplicate_items(any_list: list, ordered: bool = False):
    if len(any_list) < 1:
        return "Lista Inválida."

    new_list = []
    for element in any_list:
        if element not in new_list:
            new_list.append(element)

    if ordered:
        new_list.sort()

    return new_list


if __name__ == "__main__":
    list1 = ["Mario", "Maria", "Felipe", "Jorge", "Jorge", "Maria"]
    print(remove_duplicate_items(list1, False))  # ['Mario', 'Maria', 'Felipe', 'Jorge']

    list2 = []
    print(remove_duplicate_items(list2, False))  # Lista Inválida.

    list3 = [3, 9, 8, 3, 2, 0, 5, 2, 8, 1, 5, 3, 8, 4, 5, 2, 1, 0]
    print(remove_duplicate_items(list3, True))  # [0, 1, 2, 3, 4, 5, 8, 9]


# ex128: Crie uma agenda que armazena o nome da pessoa, ID da pessoa, número do telefone, idade. Sua agenda deve possibilitar:
# (1) – inserir um contato
# (2) – Remover um contato
# (3) – buscar um contato pelo Código.

def mostrar():
    print('Cadastrados'.center(50, '-'))
    for elemento in agenda:
        print(elemento)

agenda = []

while True:
    menu = int(input('Digite o menu:\n1: Inserir um contato\n2: Remover um contato\n3: Ver um contato\n4: Sair\n'))
    while menu < 0 or menu > 4:
        menu = int(input('Opção inválida. Digite novamente:\n1: Inserir um contato\n2: Remover um contato\n3: Ver um contato\n4: Sair\n'))

    if menu == 1:
        nome = input('Digite o nome da pessoa: ').strip().title()
        codigo = len(agenda) + 1

        for elemento in agenda:
            while elemento[1] == codigo:
                codigo = int(input('Este código já existe. Digite novamente: '))
        telefone = int(input('Digite o telefone da pessoa: '))
        idade = int(input('Digite a idade da pessoa: '))
        agenda.append([codigo, nome, telefone, idade])

    elif menu == 2:
        mostrar()

        remover = int(input('Digite o código que quer remover: '))
        for elemento in agenda:
            if elemento[0] == remover:
                print(f'Usuário {elemento[1]} com o ID de {elemento[0]} removido com sucesso.')
                agenda.remove(elemento)

    elif menu == 3:
        mostrar()

        buscar = int(input('Digite um contato pelo seu código (ID): '))
        for elemento in agenda:
            if elemento[0] == buscar:
                print(f"O nome da pessoa é {elemento[1]}, possui o ID {elemento[0]}, tem o telefone {elemento[2]} e tem {elemento[3]} anos.")
        else:
            if elemento[0] != buscar:
                print('Não foi possível identificar este usuário.')

    elif menu == 4:
        break


# ex129: Compactador RLE (Run-Length Encoding: "AAABBBCC" → "A3B3C2").

def compactador_RLE(string: str):
    if len(string) < 0:
        return "A frase deve ter mais de um caractere."

    if not string.isalpha():
        return "A frase deve conter somente letras do alfabeto, sem espaços."

    caracteres = []
    RLE = ""

    for letra in string:
        if letra not in caracteres:
            caracteres.append(letra)
            RLE += f"{letra}{string.count(letra)}"

    return f"Resultado do RLE: {RLE}"


print(compactador_RLE("compactadorRLE"))  # c2o2m1p1a2t1d1r1R1L1E1
print(compactador_RLE("Pyyyyyyyyyyyyython"))  # Resultado do RLE: P1y13t1h1o1n1
print(compactador_RLE("aaaaaaa"))  # Resultado do RLE: a7


# ex130: Crie uma função com Celsius como parâmetro e retorne a temperatura equivalente a Fahrenheit.
def converte_temperatura(Celsius: int) -> int:
    fahrenheit = (Celsius * 9/5) + 32

    return fahrenheit


if __name__ == "__main__":
    print(converte_temperatura(32))  # 89.6
    print(converte_temperatura(45))  # 113.0
    print(converte_temperatura(12))  # 53.6
    print(converte_temperatura(4.5))  # 40.1
    print(converte_temperatura(1))  # 33.8


# ex131: Crie uma função que converta quilômetros para milhas (1 km  ≈  0,621371mi).
def quilometros_para_milhas(quilometros: int) -> float:
    milhas = quilometros * 0.621371

    return milhas


if __name__ == "__main__":
    print(quilometros_para_milhas(5))  # 3.106855
    print(quilometros_para_milhas(504))  # 313.170984
    print(quilometros_para_milhas(1))  # 0.621371


# ex132: Crie uma função que receba uma string como parâmetro e retorna seu acrônimo (Python Vs JavaScript -> PVJ)
def retorna_acronimo(string: str):
    string = string.split()

    acronimo = ""

    for palavra in string:
        letra = palavra[0]
        acronimo += letra.upper()

    return acronimo


if __name__ == "__main__":
    print(retorna_acronimo("Python Vs JavaScript"))  # PVJ
    print(retorna_acronimo("Albert Einstein e Oppenheimer"))  # AEEO
    print(retorna_acronimo())


# ex133: Crie uma função que tenha raio como parâmetro e retorne a área de um círculo. Sabendo que a fórmula é: π x raio^2
import math


def retorna_area_circulo(raio: int) -> float:
    PI = math.pi
    area = PI * raio**2

    return area

if __name__ == "__main__":
    print(retorna_area_circulo(2))  # 12.566370614359172
    print(retorna_area_circulo(45))  # 6361.725123519331
    print(retorna_area_circulo(15))  # 706.8583470577034
    print(retorna_area_circulo(1))  # 3.141592653589793


# ex134: Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

def calcula_media1(notaA: float, notaB: float) -> float:
    pesoA = 3.5
    pesoB = 7.5

    media = (notaA * pesoA + notaB * pesoB) / (pesoA + pesoB)
    return f"MEDIA = {media:.5f}"


if __name__ == "__main__":
    print(calcula_media1(5.0, 7.1))  # MEDIA = 6.43182
    print(calcula_media1(0.0, 7.1))  # MEDIA = 4.84091
    print(calcula_media1(10.0, 10.0))  # MEDIA = 4.84091


# ex135: Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.

def calcula_media2(notaA: float, notaB: float, notaC: float) -> float:
    pesoA = 2
    pesoB = 3
    pesoC = 5

    media = (notaA * pesoA + notaB * pesoB + notaC * pesoC) / (pesoA + pesoB + pesoC)
    return f"MEDIA = {media:.1f}"


if __name__ == "__main__":
    print(calcula_media2(5.0, 6.0, 7.0))  # MEDIA = 6.3
    print(calcula_media2(3.7, 3.7, 9.3))  # MEDIA = 6.5
    print(calcula_media2(1.5, 3.9, 10.0))  # MEDIA = 6.5


# ex136: Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas por semana, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
def retorna_salario(numero: int, horas: int, valor_hora: float) -> float:
    salario = valor_hora * horas

    return (
        f"NÚMERO = {numero}\n"
        f"SALÁRIO = R$ {salario:.2f}"
    )


if __name__ == "__main__":
    print(retorna_salario(25, 100, 5.50))  # NÚMERO = 25; SALÁRIO = R$ 550.00
    print(retorna_salario(1, 200, 20.50))  # NÚMERO = 1; SALÁRIO = R$ 4100.00
    print(retorna_salario(6, 145, 15.55))  # NÚMERO = 6; SALÁRIO = R$ 2254.75


# ex137: Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.
vendedor = input("Digite o nome do vendedor:\n>>> ")
salario = float(input(f"Digite o salário fixo de {vendedor}:\n>>> "))
vendas = float(input(f"Qual foi o total de venda que {vendedor} fez?\n>>> "))

total = (vendas * 0.15) + salario

print(f"TOTAL = R$ {total:.2f}")


# ex138: Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.
codigo1 = int(input("Digite o código da peça 1:\n>>> "))
numero1 = int(input("Digite quantas peças são:\n>>> "))
valor1 = float(input("Digite o valor unitário de cada peça 1:\n>>> "))
calculo1 = numero1 * valor1

codigo2 = int(input("Digite o código da peça 2:\n>>> "))
numero2 = int(input("Digite quantas peças são:\n>>> "))
valor2 = float(input("Digite o valor unitário de cada peça 2:\n>>> "))
calculo2 = numero2 * valor2

valor = calculo1 + calculo2

print(f"VALOR A PAGAR: R$ {valor:.2f}")


# ex139: Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula: distância = sqrt((x2 - x1)^2 + (y2 - y1)^2). O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2. Calcule e imprima o valor da distância segundo a fórmula fornecida, considerando 4 casas decimais.
from math import sqrt

x1 = float(input("Valor do x1:\n>>> "))
y1 = float(input("Valor do y1:\n>>> "))

x2 = float(input("Valor do x2:\n>>> "))
y2 = float(input("Valor do y2:\n>>> "))

distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"{distancia:.4f}")


# ex140: Crie uma classe Carro com atributos marca e ano, e um método para exibir informações.
class Carro:
    def __init__(self, marca, ano):
        self.marca = marca
        self.ano = ano

    def exibir_informacoes(self):
        return f"O carro é da marca {self.marca} do ano {self.ano}"


if __name__ == "__main__":
    carro1 = Carro("Fiat", 2006)
    print(carro1.exibir_informacoes())  # O carro é da marca Fiat do ano 2006

    carro2 = Carro("Civic", 2015)
    print(carro2.exibir_informacoes())  # O carro é da marca Civic do ano 2015

    carro3 = Carro("Ferrari", 2021)
    print(carro3.exibir_informacoes())  # O carro é da marca Ferrari do ano 2021


# ex141: Crie uma classe Pessoa com atributos nome e idade, e um método para dizer a idade.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_idade(self):
        return f"{self.nome} tem {self.idade} anos."


if __name__ == "__main__":
    pessoa1 = Pessoa("Lucas", 45)
    print(pessoa1.exibir_idade())  # Lucas tem 45 anos.

    pessoa2 = Pessoa("Maria", 21)
    print(pessoa2.exibir_idade())  # Maria tem 21 anos.

    pessoa3 = Pessoa("Felipe", 15)
    print(pessoa3.exibir_idade())  # Felipe tem 15 anos.


# ex142: Crie uma classe ContaBancaria com atributos titular e saldo, e métodos sacar e depositar.
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def sacar(self, valor):
        if valor > self.saldo:
            print("O valor do saque é maior que o valor do saldo, não foi possível fazer o saque.")
            return 0

        if valor <= 0:
            print("O valor do saque não pode ser negativo nem nulo.")
            return 0

        self.saldo -= valor
        print("Saque realizado com sucesso.")

    def depositar(self, valor):
        if valor <= 0:
            print("O valor do depósito não pode ser negativo nem nulo.")
            return 0

        self.saldo += valor
        print("Depósito realizado com sucesso.")

    def exibir_saldo(self):
        print(f"O valor do seu saldo é de R${self.saldo}")


if __name__ == "__main__":
    conta1 = ContaBancaria("João", 34500)
    conta1.sacar(560)
    conta1.exibir_saldo()


# ex143: Crie uma classe Aluno com atributos nome e notas, e um método para calcular a média.
class Aluno:
    def __init__(self, nome: str, notas: list):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        media = sum(self.notas) / len(self.notas)

        print(f"{media:.2f}")


if __name__ == "__main__":
    aluno1 = Aluno("Pedro", [7.2, 9.5, 2.3])
    aluno1.calcular_media()  # 6.33

    aluno2 = Aluno("Maria", [4.6, 9.3, 4.7])
    aluno2.calcular_media()  # 6.20

    aluno3 = Aluno("Mateus", [7,.3, 9.0, 4.1])
    aluno3.calcular_media()  # 5.10


# ex144: Crie uma classe TV com atributos canal e volume, e métodos mudar_canal() e ajustar_volume().
class TV:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def mudar_canal(self, novo_canal):
        print(f"Mudando de {self.canal} para {novo_canal}")

    def ajustar_volume(self, novo_volume):
        print(f"Ajustando volume de {self.volume} para {novo_volume}")


if __name__ == "__main__":
    tv = TV("Show do Milhão", 12)
    tv.mudar_canal("Silvio Santos")  # Mudando de Show do Milhão para Silvio Santos
    tv.ajustar_volume(18)  # Ajustando volume de 12 para 18


# ex145: Crie uma classe Lampada com métodos ligar() e desligar().
class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada

    def ligar(self):
        if self.ligada:
            print("A lâmpada já está ligada.")
        else:
            print("A lâmpada ligou.")
            self.ligada = True

    def desligar(self):
        if not self.ligada:
            print("A lâmpada já está desligada.")
        else:
            print("A lâmpada desligou.")
            self.ligada = False


if __name__ == "__main__":
    lampada = Lampada(True)
    lampada.ligar()  # A lâmpada já está ligada.
    lampada.desligar()  # A lâmpada desligou.
    lampada.desligar()  #  A lâmpada já está desligada.
    lampada.ligar()  # A lâmpada ligou.
    lampada.desligar()  # A lâmpada desligou.


# ex146: Crie uma classe Livro com atributos título e autor, e um método para exibir informações.
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def exibir_informacoes(self):
        print(f"O autor {self.autor} escreveu o livro {self.titulo}")


if __name__ == "__main__":
    livro = Livro("Técnicas de Invasão", "Bruno Fraga")
    livro.exibir_informacoes()  # O autor Bruno Fraga escreveu o livro Técnicas de Invasão


# ex147: Crie uma classe Cachorro com atributos nome e raça, e um método latir().
class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        print(f"{self.nome} da raça {self.raca} latiu: au au au 🐶!")

if __name__ == "__main__":
    snoopy = Cachorro("Snoopy", "BullDog")
    snoopy.latir()  # Snoopy da raça BullDog latiu: au au au 🐶!


# ex148: Crie uma função que identifique as partes de um email e separe em Nome, Domínio e TLD
def mail_parts(mail: str):
    if mail.count("@") > 1 or mail.count(".") > 1:
        return "E-mail inválido."

    name = mail[:mail.index("@")]
    domain = mail[mail.index("@")+1:mail.index(".")]
    extension = mail[mail.index(".")+1:]

    return f"Nome: {name} | Domínio (Email): {domain} | Extensão (TLD/GTLD/CCTLD): {extension}"

if __name__ == "__main__":
    print(mail_parts("semprotecao123@gmail.com"))  # Nome: semprotecao123 | Domínio (Email): gmail | Extensão (TLD/GTLD/CCTLD): com
    print(mail_parts("anonymous@proton.me"))  # Nome: anonymous | Domínio (Email): proton | Extensão (TLD/GTLD/CCTLD): me
    print(mail_parts("fbi_acc@tutamail.com"))  # Nome: fbi_acc | Domínio (Email): tutamail | Extensão (TLD/GTLD/CCTLD): com
    print(mail_parts("none.anonymous@gmail.com"))  # E-mail inválido.


# ex149: # Crie uma função que identifique as partes de uma URL.
from requests import get
from requests import exceptions

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.6422.113 Safari/537.36 "
        "Edg/125.0.2535.67"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;"
        "q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
        "application/signed-exchange;v=b3;q=0.7"
    ),
    "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Ch-Ua": (
        '"Chromium";v="125", "Microsoft Edge";v="125", '
        '"Not.A/Brand";v="24"'
    ),
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "DNT": "1",
    "TE": "trailers"
}

def url_parts(URL: str):
    if "." not in URL:
        return "Invalid URL"
    if "http" not in URL:
        URL = f"https://www.{URL}"

    try:
        r = get(URL, headers=headers)
    except exceptions.ConnectionError as conn_e:
        return f"Erro de Conexão: {conn_e}"
    except exceptions.Timeout as timeout_e:
        return f"Tempo limite de tentativa de conexão: {timeout_e}"
    except exceptions.InvalidURL as inv_url_e:
        return f"URL inválida: {inv_url_e}"
    except Exception as e:
        return f"Erro: {e}"
    else:
        return r.url


if __name__ == "__main__":
    print(url_parts("google.com"))  # https://www.google.com/
    print(url_parts("nasa.gov"))  # https://www.nasa.gov/
    print(url_parts("unknoooooownnnn.com"))  # Erro de Conexão: HTTPSConnectionPool(host='www.unknoooooownnnn.com', port=443): Max retries exceeded with url: / (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x000002811896B110>: Failed to resolve 'www.unknoooooownnnn.com' ([Errno 11001] getaddrinfo failed)"))
    print(url_parts("cia.gov"))  # https://www.cia.gov/


# ex150: Crie uma função que inverta uma string
def invert_string(string: str):
    if not isinstance(string, str) or len(string) <= 1:
        return "String inválida, preencha corretamente."

    letters = len(string)
    inversed_string = ""

    for letter in range(letters):
        last_letter = string[-letter-1]
        inversed_string += last_letter

    return inversed_string


if __name__ == "__main__":
    print(invert_string("Flame"))  # emalF
    print(invert_string("Python"))  # nohtyp
    print(invert_string("subi no onibus"))  # subino on ibus

    string = input("Por favor, digite a string que queira inverter:\n>>> ")
    print(invert_string(string))


# ex151: Crie uma função que cria senhas criptografadas (letras randômicas)
import random

def criptografar_senha(tamanho: int):
    if tamanho > 82 or tamanho < 8:
        return "Tamanho inválido. O tamanho deve ser entre 8 e 82 caracteres"

    criptografia = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()%-_=+-&*?"
    senha = "".join(random.sample(criptografia, tamanho))

    return senha

try:
    tamanho = int(input("Digite o tamanho da senha (8-82):\n>>> "))
    quantidade = int(input("Digite a quantidade de senhas a gerar (1 a 100):\n>>> "))

    if quantidade < 1 or quantidade > 100:
        print("A quantidade de senhas deve ser entre 1 a 100.")
    else:
        for i in range(quantidade):
            print(criptografar_senha(tamanho))

except Exception as e:
    print(f"Erro: {e}")


# ex152: Encontre a próxima raíz quadrada perfeita de um número, retorne -1 caso o número dado não seja uma raíz quadrada perfeita
import math

def retorna_proxima_raiz(numero: int) -> int:
    raiz_quadrada = math.sqrt(numero) + 1
    if not raiz_quadrada.is_integer():
        return -1

    proxima_raiz = int(raiz_quadrada**2)

    return proxima_raiz


if __name__ == "__main__":
    print(retorna_proxima_raiz(144))  # 169
    print(retorna_proxima_raiz(34))  # -1
    print(retorna_proxima_raiz(61858225))  # 61873956


# ex153: Crie uma função que receba dois números e uma string, indicando a operação a ser feita entre estes dois números. As opções de operações são: "add", "subtract", "divide", "multiply".
def calculadora_aritmetica(a: float, b: float, operacao: str):
    if operacao not in ["add", "subtract", "divide", "multiply"]:
        return "Operação inválida."

    if operacao == "add":
        return a + b
    elif operacao == "subtract":
        return a - b
    elif operacao == "divide":
        return a / b

    return a * b


if __name__ == "__main__":
    print(calculadora_aritmetica(4, 9, "add"))  # 13
    print(calculadora_aritmetica(45, 8, "multiply"))  # 360
    print(calculadora_aritmetica(1, 1.2, "divide"))  # 0.8333333333333334
    print(calculadora_aritmetica(60, 50, "subtract"))  # 10
    print(calculadora_aritmetica(0, 0, "disconhecido"))  # Operação inválida.


# ex154: Crie uma função que receba uma lista e retorne a soma de todos os valores positivos.
def soma_positivos(lista: list) -> int:
    soma = 0

    for valor in lista:
        if valor > 0:
            soma += valor

    return soma


if __name__ == "__main__":
    print(soma_positivos([12, -5, 12, -3, 0, -9]))  # 24
    print(soma_positivos([40, 10, -50, 0, 90]))  # 140
    print(soma_positivos([-5, -3, -15, -999]))  # 0


# ex155: Crie uma função que receba uma lista de números como parâmetro e retorne cada valor com a sua operação trocada (positivos viram negativos e vice-versa).
def inverte_operacoes(lista: list):
    lista_operacoes_inversa = []

    for valor in lista:
        if valor > 0:
            lista_operacoes_inversa.append(-valor)
        else:
            lista_operacoes_inversa.append(abs(valor))

    return lista_operacoes_inversa

if __name__ == "__main__":
    print(inverte_operacoes([12, -3, 50, -15]))  # [-12, 3, -50, 15]
    print(inverte_operacoes([0, 12, -7, 999, 4]))  # [0, -12, 7, -999, -4]
    print(inverte_operacoes([56, 12, 3, -9, 15]))  # [-56, -12, -3, 9, -15]


# ex156: Conte as ovelhas! Crie uma função que receba um número inteiro maior que 1 como parâmetro e retorne {numero} ovelha... de 1 até o número.
def contar_ovelhas(ovelhas: int) -> str:
    if ovelhas <= 1:
        print("O número deve ser maior que 1.")
        return False

    for ovelha in range(1, ovelhas+1):
        print(f"{ovelha} ovelha(s)... ", end="")


if __name__ == "__main__":
    contar_ovelhas(3)  # 1 ovelha(s)... 2 ovelha(s)... 3 ovelha(s)... 
    contar_ovelhas(1)  # O número deve ser maior que 1.
    contar_ovelhas(12)  # 1 ovelha(s)... 2 ovelha(s)... 3 ovelha(s)... 4 ovelha(s)... 5 ovelha(s)... 6 ovelha(s)... 7 ovelha(s)... 8 ovelha(s)... 9 ovelha(s)... 10 ovelha(s)... 11 ovelha(s)... 12 ovelha(s)...


# ex157: Crie uma classe Funcionario com atributos nome, cargo e salário, salario, com método de trabalhar()
class Funcionario:
    def __init__(self, nome, cargo, salario, saldo):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario
        self.saldo = saldo

    def trabalhar(self, horas):
        bonus = 15 * horas
        self.saldo += bonus
        print(f"Trabalhando...")
        print(f"Olha, você ganhou +R${bonus} de saldo!")


if __name__ == "__main__":
    funcionario1 = Funcionario("João", "Desenvolvedor de Sistemas", 1350, 2750)
    funcionario1.trabalhar(1)


# ex158: Crie uma classe Gato com atributos nome e cor, e um método miar().
class Gato:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def miar(self):
        print(f"{self.nome} miou: miauuuu 🐱!")


if __name__ == "__main__":
    patrick = Gato("Patrick", "Cinza Claro")
    patrick.miar()


# ex159: Crie uma função que receba quantidade como parâmetro e retorne n lorems, em que n é a quantidade.
from random import choice


def lorem(quantidade: int):
    lorems = [
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet.",
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    ]

    for item in range(quantidade):
        print(choice(lorems))


if __name__ == "__main__":
    lorem(5)
    lorem(12)
    lorem(9)


# ex160: Classe Academia: parâmetros -> nome, endereco, equipamentos; Funções -> abrir, fechar
class Academia:
    def __init__(self, nome, endereco, equipamentos):
        self.nome = nome
        self.endereco = endereco
        self.equipamentos = equipamentos
        self.aberto = False

    def sobre(self):
        print(f"Seja bem vindo(a) ao {self.nome} localizado em {self.endereco}! Aqui temos equipamentos como {", ".join(self.equipamentos)}!")
        if self.aberto:
            print("Neste momento estamos abertos, esperando por você!")
        else:
            print("A academia está fechada agora. Volte mais tarde, esperamos por você!")

    def usar_academia(self, equipamento):
        if self.aberto:
            print(f"Bora crescer com tudo com {equipamento}!")
        else:
            print("Não é possível usar a academia quando está fechada!")

    def abrir(self):
        if self.aberto:
            print("A academia já está aberta.")
        else:
            self.aberto = True
            print("Academia abriu, venha nos visitar!")

    def fechar(self):
        if self.aberto:
            print("Estamos fechando, volte amanhã mais cedo.")
            self.aberto = False
        else:
            print("A academia já está fechada.")

    def status(self):
        if self.aberto:
            print("A academia está aberta.")
        else:
            print("A academia está fechada.")


if __name__ == "__main__":
    muscle_grow = Academia("MuscleGrow", "Rua Fransisco Ladelmir 778", ["...", "...", "..."])
    muscle_grow.status()
    muscle_grow.sobre()
    muscle_grow.abrir()
    muscle_grow.usar_academia("Supino")
    muscle_grow.fechar()


# ex161: Classe Agenda: parâmetros -> dono; Funções -> adicionar_compromisso(), listar_crompromissos()
class Agenda:
    def __init__(self, dono):
        self.dono = dono
        self.compromissos = []

    def adicionar_compromisso(self, compromisso, data):
        self.compromissos.append([compromisso, data])
        print("Compromisso adicionado com sucesso")

    def listar_compromissos(self):
        for lista_compromisso in self.compromissos:
            print(", ".join(lista_compromisso))


if __name__ == "__main__":
    agenda = Agenda("Gabriel")
    agenda.adicionar_compromisso("Ir à NASA", "14:30")
    agenda.listar_compromissos()


# ex162: Classe Astronauta: nome, missao, experiencia, com métodos de apresentar(), explorar() e descansar()
class Astronauta:
    def __init__(self, nome, missao, experiencia):
        self.nome = nome
        self.missao = missao
        self.experiencia = experiencia

    def apresentar(self):
        print(f"Conheça {self.nome}! Está/Já esteve presente na missão {self.missao} e tem {self.experiencia} anos de experiência.")

    def explorar(self):
        print(f"{self.nome} está explorando a missão {self.missao}.")

    def descansar(self):
        print(f"{self.nome} está cansado de explorar, foi descansar.")

if __name__ == "__main__":
    neil_armstrong = Astronauta("Neil Armstrong", "Apollo 11", 27)
    neil_armstrong.apresentar()
    neil_armstrong.explorar()
    neil_armstrong.descansar()


# ex163: Classe Calculadora básica que realiza as 4 operações básicas
class Calculadora:
    def __init__(self):
        pass

    def adicao(self, a, b):
        print(a + b)

    def subtracao(self, a, b):
        print(a - b)

    def multiplicacao(self, a, b):
        print(a * b)

    def divisao(self, a, b):
        print(a / b)


if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.adicao(12, 6)  # 18
    calculadora.multiplicacao(70, 4)  # 280
    calculadora.divisao(48, 4)  # 12.0
    calculadora.subtracao(900, 1800)  # -900


# ex164: Classe Chat com parâmetros -> remetente, destinatario; métodos -> enviar_mensagem()
class Chat:
    def __init__(self, remetente, destinatario):
        self.remetente = remetente
        self.destinatario = destinatario

    def enviar_mensagem(self, mensagem):
        print(f"{self.remetente}: {mensagem}")


if __name__ == "__main__":
    mateus = Chat("Mateus", "Felipe")
    felipe = Chat("Felipe", "Mateus")

    mateus.enviar_mensagem("Oi, Felipe!")
    felipe.enviar_mensagem("Oi, Mateus! Que tal jogar bola?")
    felipe.enviar_mensagem("Mas precisa ser rápido, tenho que voltar logo.")
    mateus.enviar_mensagem("Eu topo, Felipe!")
    felipe.enviar_mensagem("Ok, vamos no parque, te encontro lá!")
    mateus.enviar_mensagem("Tô indo.")


# ex165: Nathan ama ciclismo. Porque Nathan sabe que é importante se manter hidratado. Ele toma 0.5 litros de água para cada hora de ciclismo. Você recebeu o tempo em horas e precisa retornar o número de litros que Nathan tomou, arredondado.
def litros_agua(horas: float) -> int:
    litros_hora = 0.5

    litros = int(horas * litros_hora)
    return litros


if __name__ == "__main__":
    print(litros_agua(3))  # 1
    print(litros_agua(6.7))  # 3
    print(litros_agua(11.8))  # 5
    print(litros_agua(15))  # 7


# ex166: Crie uma função que converta nomes em inicias separados por pontos. Exemplo: Albert Einstein -> A.E
def acronimo_nome(nome: str):
    iniciais = []

    for inicial in nome.split():
        iniciais.append(inicial[0])

    return ".".join(iniciais)


if __name__ == "__main__":
    print(acronimo_nome("Albert Einstein"))  # A.E
    print(acronimo_nome("Isaac Newton"))  # I.N
    print(acronimo_nome("Leonardo Da Vinci"))  # L.D.V


# ex167: Crie uma função que recebe uma string como parâmetro e retorne
def remove_espacos(string: str):
    string = string.replace(" ", "")

    return string


if __name__ == "__main__":
    print(remove_espacos("html é uma linguagem de marcação de hipertexto."))  # htmléumalinguagemdemarcaçãodehipertexto.
    print(remove_espacos("brave é um ótimo navegador para segurança."))  # braveéumótimonavegadorparasegurança.


# ex168: Dois amigos desejam trocar informações entre si num chat de bots. Os amigos querem conversar sobre hacking, e os bots filtram qualquer tipo de palavra inadequada e relacionada a hacking. Sabendo disso, os dois amigos criaram algumas substituições. A = 4; I = 1;E = 3;S = 5; O = 0.
# Crie uma função que receba uma string como parâmetro e retorne a string com as substituições.
# Atenção: APENAS PARA FINS DIDÁTICOS.
def substituir_caracteres(string: str) -> str:
    string = string.lower()
    string = string.replace("a", "4")
    string = string.replace("i", "1")
    string = string.replace("e", "3")
    string = string.replace("s", "5")
    string = string.replace("o", "0")

    return string

if __name__ == "__main__":
    print(substituir_caracteres("Que tal fazer um DDoS?"))  # qu3 t4l f4z3r um dd05?
    print(substituir_caracteres("Obaa! Aprendi SQL INJECTION!"))  # 0b44! 4pr3nd1 5ql 1nj3ct10n!
    print(substituir_caracteres("Instalei mais de 500 malwares nas vítimas!"))  # 1n5t4l31 m415 d3 500 m4lw4r35 n45 vít1m45!


# ex169: Crie uma função que recebe um número inteiro como parâmetro e retorne o fatorial deste número.
def fatorial(numero_usuario: int) -> int:
    if numero_usuario <= 1:
        return "O número deve ser maior que 1."

    fatorial = 1

    for numero in range(1, numero_usuario+1):
        fatorial *= numero

    return fatorial


if __name__ == "__main__":
    print(fatorial(5))  # 120
    print(fatorial(4))  # 24
    print(fatorial(6))  # 720
    print(fatorial(7))  # 5040
    print(fatorial(1))  # O número deve ser maior que 1.


# ex170: Crie uma função que recebe uma string com uma ou mais palavras como parâmetro e retorne a mesma string, mas caso a palavra tiver 5 ou mais caracteres, retorne a palavra ao contrário. Por exemplo: VSCode é um belo editor -> edoCSV é um belo rotide.
def inverte_parcialmente(string: str):
    resultado = []

    for palavra in string.split():
        if len(palavra) >= 5:
            resultado.append(palavra[::-1])
        else:
            resultado.append(palavra)

    return " ".join(resultado)


if __name__ == "__main__":
    print(inverte_parcialmente("VSCode é um belo editor"))  # edoCSV é um belo rotide
    print(inverte_parcialmente("A mente é um lugar curioso."))  # A etnem é um ragul .osoiruc
    print(inverte_parcialmente("Você voltaria para o passado ou avançaria para o futuro?"))  # Você airatlov para o odassap ou airaçnava para o ?orutuf


# ex171: Crie uma função que receba um número e diga se aquele número tem números adjacentes. Ou seja, números que são iguais e estão um ao lado do outro. Exemplo: 2435543 -> é um número adjacente pois o primeiro 5 está ao lado do segundo 5.
def numero_adjacente(numero: int) -> bool:
    if not numero.is_integer() or isinstance(numero, (bool, float, str, list, tuple, dict, set)):
        return "Resposta incorreta, deve ser um número inteiro."

    # Jeito mais fácil (não envolve quase nenhum esforço de raciocínio)
    # numero = str(numero)

    # for i in range(99, -1, -11):
    #     if str(i) in numero:
    #         return True

    # return False

    numero = str(numero)

    for index, _ in enumerate(numero):
        if not index+1 >= len(numero) and numero[index] == numero[index+1]:
            return True

    return False


if __name__ == "__main__":
    print(numero_adjacente(23456403894799))  # True
    print(numero_adjacente(74346236723500438))  # True
    print(numero_adjacente(549224.32))  # Resposta incorreta, deve ser um número inteiro.
    print(numero_adjacente(True))  # Resposta incorreta, deve ser um número inteiro.
    print(numero_adjacente(843653468))  # False
    print(numero_adjacente(4))  # False


# ex172: Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained. Examples "This is an example!" ==> "sihT si na !elpmaxe"; "double  spaces"      ==> "elbuod  secaps"
def reverse_words(text):
    return " ".join([word[::-1] for word in text.split(" ")])

    # or
    #     string = []

    #     for word in text.split(" "):
    #         string.append(word[::-1])

    #     return " ".join(string)


if __name__ == "__main__":
    print(reverse_words("This is an example!"))  # sihT si na !elpmaxe
    print(reverse_words("a b c d"))  # a b c d
    print(reverse_words("double  spaces"))  # elbuod  secaps


# ex173: Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed. For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7. [10, 343445353, 3453445, 3453545353453] should return 3453455.
def sum_two_smallest_numbers(numbers: list):
    return sum(sorted(numbers)[:2])

    # numbers.sort()
    # lowest_numbers = [numbers[0], numbers[1]]

    # return sum(lowest_numbers)


if __name__ == "__main__":
    print(sum_two_smallest_numbers([8, 3, 2, 9]))  # 5
    print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))  # 7
    print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))  # 3453455
    print(sum_two_smallest_numbers([0, 12, 3, 7]))  # 3


# ex174: ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. If the function is passed a valid PIN string, return true, else return false.
# Examples (Input --> Output)
# "1234"   -->  true
# "12345"  -->  false
# "a234"   -->  false
def validate_pin(pin: str):
    return pin.isnumeric() and len(pin) in [4, 6]


if __name__ == "__main__":
    print(validate_pin("1234"))  # True
    print(validate_pin("895404"))  # True
    print(validate_pin("12345"))  # False
    print(validate_pin("a234"))  # False


# ex175: # Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#, empty table in COBOL) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).
# Examples:
# divisors(12) --> [2, 3, 4, 6]
# divisors(25) --> [5]
# divisors(13) --> "13 is prime"
def divisors(number):
    return [num for num in range(2, number) if number % num == 0] or f"{number} is prime"


if __name__ == "__main__":
    print(divisors(12))  # [2, 3, 4, 6]
    print(divisors(25))  # [5]
    print(divisors(13))  # 13 is prime


# ex176: # Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest. Write a function that returns both the minimum and maximum number of the given list/array.
# Examples (Input --> Output)
# [1,2,3,4,5] --> [1,5]
# [2334454,5] --> [5,2334454]
# [1]         --> [1,1]
def min_max(numbers: list):
    return [sorted(numbers)[i] for i in range(0, -2, -1)]


if __name__ == "__main__":
    print(min_max([8, 4, 2, 6, 1, 2, 8]))  # [1, 8]
    print(min_max([0, 5]))  # [0, 5]
    print(min_max([23, 12, 5, -8, 2]))  # [-8, 23]


# ex177: Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input("Digite a sua altura:\n>>> "))
peso_ideal = (72.7 * altura) - 58

print(f"Seu peso ideal é {peso_ideal}")


# ex178: Crie uma função que recebe qualquer valor como parâmetro e retorne o tupo de dado deste valor
def tipo_de_dado(valor):
    return f"Este valor tem o tipo de dado {type(valor).__name__}"


if __name__ == "__main__":
    print(tipo_de_dado("Guido criou o que chamamos de python!"))  # Este valor tem o tipo de dado str
    print(tipo_de_dado(2 < 4))  # Este valor tem o tipo de dado bool
    print(tipo_de_dado(12 + 5))  # Este valor tem o tipo de dado int
    print(tipo_de_dado([1, 2, 3, 4, 5]))  # Este valor tem o tipo de dado list


# ex179: Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b. Note: a and b are not ordered!
def get_sum(a, b):
    return sum([i for i in range(a, b+1)] if a < b else [i for i in range(b, a+1)])


if __name__ == "__main__":
    print(get_sum(1, 0))
    print(get_sum(1, 2))
    print(get_sum(0, 1))
    print(get_sum(1, 1))
    print(get_sum(-1, 0))
    print(get_sum(-1, 2))


# ex180:You are going to be given a non-empty string. Your job is to return the middle character(s) of the string. If the string's length is odd, return the middle character. If the string's length is even, return the middle 2 characters.
# Examples:
# "test" --> "es"
# "testing" --> "t"
# "middle" --> "dd"
# "A" --> "A"
def get_middle(s):
    length = (len(s) // 2)
    return s[length-1:length+1] if len(s) % 2 == 0 else s[length]


if __name__ == "__main__":
    print(get_middle("test"))  # es
    print(get_middle("middle"))  # dd
    print(get_middle("half"))  # al


# ex181: Remove First and Last Character: Your goal is to write a function that removes the first and last characters of a string. You're given one parameter, the original string. Important: Your function should handle strings of any length ≥ 2 characters. For strings with exactly 2 characters, return an empty string.

# Examples
# 'eloquent' --> 'loquen'
# 'country'  --> 'ountr' 
# 'person'   --> 'erso'
# 'ab'       --> '' (empty string)
# 'xyz'      --> 'y'
def remove_char(s):
    return s[1:-1]


if __name__ == "__main__":
    print(remove_char("eloquent"))  # loquen
    print(remove_char("JavaScript"))  # avaScrip
    print(remove_char("Python"))  # ytho


# ex182: Trolls are attacking your comment section! A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat. Your task is to write a function that takes a string and return a new string with all vowels removed. For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
def disemvowel(s):
    for v in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
        s = s.replace(v, "")

    return s


if __name__ == "__main__":
    print(disemvowel("This website is for losers LOL!"))  # Ths wbst s fr lsrs LL!
    print(disemvowel("We gonna put'n trash this SITE!"))  # W gnn pt'n trsh ths ST!


# ex183: Descending Order: Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.
# Examples:
# Input: 42145 Output: 54421
# Input: 145263 Output: 654321
# Input: 123456789 Output: 987654321
def descending_order(num):
    return int("".join(sorted([numero for numero in str(num)])[::-1]))


if __name__ == "__main__":
    print(descending_order(42145))  # 54421
    print(descending_order(145263))  # 654321
    print(descending_order(123456789))  # 987654321


# ex184: Create a function which answers the question "Are you playing banjo?". If your name starts with the letter "R" or lower case "r", you are playing banjo!
# The function takes a name as its only argument, and returns one of the following strings:
# name + " plays banjo" 
# name + " does not play banjo"
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name.lower().startswith("r") else f"{name} does not play banjo"


if __name__ == "__main__":
    print(are_you_playing_banjo("Renan"))  # Renan plays banjo
    print(are_you_playing_banjo("Carlos"))  # Carlos does not play banjo
    print(are_you_playing_banjo("John"))  # John does not play banjo


# ex185: Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative or non-integer. If the array does not contain any numbers then you should return 0.
# Examples
# Input: [1, 5.2, 4, 0, -1]
# Output: 9.2

# Input: []
# Output: 0

# Input: [-2.398]
# Output: -2.398
def sum_array(a):
    return sum(a)


if __name__ == "__main__":
    print(sum_array([1, 5.2, 4, 0, -1]))  # 9.2
    print(sum_array([]))  # 0
    print(sum_array([-2.398]))  # -2.398


# ex186: Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).
# For example,
# [True,  True,  True,  False,
#   True,  True,  True,  True ,
#   True,  False, True,  False,
#   True,  False, False, True ,
#   True,  True,  True,  True ,
#   False, False, True,  True]
# The correct answer would be 17.
def count_sheeps(sheeps):
    return sheeps.count(True)


if __name__ == "__main__":
    print(count_sheeps([True,  True,  True,  False,
    True,  True,  True,  True ,
    True,  False, True,  False,
    True,  False, False, True ,
    True,  True,  True,  True ,
    False, False, True,  True]
    ))  # 17


# ex187: Implement a function which convert the given boolean value into its string representation. Note: Only valid inputs will be given.
def boolean_to_string(b):
    return "True" if b else "False"


if __name__ == "__main__":
    print(boolean_to_string(True))  # "True"
    print(boolean_to_string(False))  # "False"


# ex188: In this simple assignment you are given a number and have to make it negative. But maybe the number is already negative?
# Examples
# make_negative(1);  # return -1
# make_negative(-5); # return -5
# make_negative(0);  # return 0
def make_negative( number ):
    return -abs(number)


if __name__ == "__main__":
    print(make_negative(1))  # -1
    print(make_negative(-5))  # -5
    print(make_negative(0))  # 0


# ex189: Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
# [1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
# [1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
# [] --> []
def invert(lst):
    return [-x or x for x in lst]


if __name__ == "__main__":
    print(invert([1, -2, 3, -4, 5]))


# ex190: Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse).
def opposite(number):
    return -number


if __name__ == "__main__":
    print(opposite(12))  # -12
    print(opposite(-23))  # 23
    print(opposite(-15))  # 15
    print(opposite(434))  # -434


# ex191: Given an array of integers. Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative. If the input is an empty array or is null, return an empty array.
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
def count_positives_sum_negatives(arr):
    return [] if not arr else [len(list(filter(lambda x: x > 0, arr))), sum(list(filter(lambda x: x < 0, arr)))]

if __name__ == "__main__":
    print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))  # [10, -65]
    print(count_positives_sum_negatives([0, 1]))  # [1, 0]
    print(count_positives_sum_negatives([23, -9, -1, 2]))  # [2, -10]
    print(count_positives_sum_negatives([15, 23, 34, 34, 34, 15]))  # [6, 0]


# ex192: Build a function that returns an array of integers from n to 1 where n>0.
# Example : n=5 --> [5,4,3,2,1]
def reverse_seq(n):
    return [x for x in range(n, 0, -1)]


if __name__ == "__main__":
    print(reverse_seq(12))  # [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(reverse_seq(25))  # [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(reverse_seq(2))  # [2, 1]
    print(reverse_seq(-1))  # []


# ex193: Sentence Smash
# Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!
# Example
# ['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'
def smash(words):
    return " ".join(words)


if __name__ == "__main__":
    print(smash(["Hello", "World!"]))  # Hello World!
    print(smash(["flame", "astro"]))  # flame astro


# ex194: Description: We need a function that can transform a string into a number. What ways of achieving this do you know? Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.
# Examples
# "1234" --> 1234
# "605"  --> 605
# "1405" --> 1405
# "-7" --> -7
def string_to_number(s):
    return int(s)

if __name__ == "__main__":
    print(string_to_number("28931"))  # 28931
    print(string_to_number("34552"))  # 34552
    print(string_to_number("4"))  # 3
    print(string_to_number("42343124"))  # 42343124


# ex195: We need a function that can transform a number (integer) into a string.
# What ways of achieving this do you know?
# Examples (input --> output):
# 123  --> "123"
# 999  --> "999"
# -100 --> "-100"
def number_to_string(num):
    return str(num)


if __name__ == "__main__":
    print(number_to_string(123))  # "123"
    print(number_to_string(999))  # "999"
    print(number_to_string(-100))  # "-100"


# ex196: In this kata you are required to, given a string, replace every letter with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return it.
# Example
# Input = "The sunset sets at twelve o' clock." -> "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"
def alphabet_position(text):
    alphabet = ['.', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return " ".join([str(alphabet.index(x)) for x in text.lower() if x.isalpha()])


if __name__ == "__main__":
    print(alphabet_position("The sunset sets at twelve o' clock."))  # 20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11
    print(alphabet_position("Jorge is going to launch"))  # 10 15 18 7 5 9 19 7 15 9 14 7 20 15 12 1 21 14 3 8
    print(alphabet_position("Hikaru buys a porsche and play chess while driving"))  # 8 9 11 1 18 21 2 21 25 19 1 16 15 18 19 3 8 5 1 14 4 16 12 1 25 3 8 5 19 19 23 8 9 12 5 4 18 9 22 9 14 7


# ex197: Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
# Example (Input => Output):
# 35231 => [1,3,2,5,3]
# 0     => [0]
def digitize(n):
    return list(reversed([int(s) for s in str(n)]))


if __name__ == "__main__":
    print(digitize(35231))  # [1, 3, 2, 5, 3]
    print(digitize(890324))  # [4, 2, 3, 0, 9, 8]
    print(digitize(2198))  # [8, 9, 1, 2]


# ex198: Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.
# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
# Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.
def get_grade(s1, s2, s3):
    s = sum([s1, s2, s3]) / 3
    return "A" if s <= 100 and s >= 90 else "B" if s >= 80 and s < 90 else "C" if s >= 70 and s < 80 else "D" if s >= 60 and s < 70 else "F"


if __name__ == "__main__":
    print(get_grade(95, 90, 93))  # A
    print(get_grade(39, 100, 89))  # C
    print(get_grade(54, 76, 100))  # C
    print(get_grade(22, 15, 67))  # F


# ex199: The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc. Given a year, return the century it is in.
# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20
# 2742 --> 28
def century(year):
    return year // 100 if year % 100 == 0 else (year // 100) + 1


if __name__ == "__main__":
    print(century(1189))  # 12
    print(century(2232))  # 23
    print(century(1900))  # 19


# ex200: Given an array of integers, return a new array with each value doubled. For example:
# [1, 2, 3] --> [2, 4, 6]
def maps(a):
    return list(map(lambda i: i * 2, a))


if __name__ == "__main__":
    print(maps([1, 2, 3]))  # [2, 4, 6]
    print(maps([8, 16, 24]))  # [16, 32, 48]
    print(maps([128, 256, 512]))  # [256, 512, 1024]


# ex201: Given an array of ones and zeroes, convert the equivalent binary value to an integer.
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

# Examples:

# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5
# Testing: [1, 0, 0, 1] ==> 9
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 1, 0] ==> 6
# Testing: [1, 1, 1, 1] ==> 15
# Testing: [1, 0, 1, 1] ==> 11
def binary_array_to_number(arr):
    return sum([(b+1) ** i for i, b in enumerate(reversed(arr)) if b])


if __name__ == "__main__":
    print(binary_array_to_number([0, 1, 1, 0]))  # 6
    print(binary_array_to_number([0, 0, 0, 1]))  # 1
    print(binary_array_to_number([0, 0, 0, 0]))  # 0


# ex202: The wave (known as the Mexican wave in the English-speaking world outside North America) is an example of metachronal rhythm achieved in a packed stadium when successive groups of spectators briefly stand, yell, and raise their arms. Immediately upon stretching to full height, the spectator returns to the usual seated position. The result is a wave of standing spectators that travels through the crowd, even though individual spectators never move away from their seats. In many large arenas the crowd is seated in a contiguous circuit all the way around the sport field, and so the wave is able to travel continuously around the arena; in discontiguous seating arrangements, the wave can instead reflect back and forth through the crowd. When the gap in seating is narrow, the wave can sometimes pass through it. Usually only one wave crest will be present at any given time in an arena, although simultaneous, counter-rotating waves have been produced.

# In this simple Kata your task is to create a function that turns a string into a Mexican Wave. You will be passed a string and you must return an array of strings where an uppercase letter is a person standing up.

# Rules
# 1.  The input string will always consist of lowercase letters and spaces, but may be empty, in which case you must return an empty array. 2.  If the character in the string is whitespace then pass over it as if it was an empty seat

# Examples
# "hello" => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]
# " s p a c e s " => [ " S p a c e s ", " s P a c e s ", " s p A c e s ", " s p a C e s ", " s p a c E s ", " s p a c e S "]
def wave(people):
    return [f"{people[:i]}{people[i].upper()}{people[i+1:]}" for i in range(len(people)) if people[i].isalpha()]


if __name__ == "__main__":
    print(wave("Flame astro"))  # ['Flame astro', 'FLame astro', 'FlAme astro', 'FlaMe astro', 'FlamE astro', 'Flame Astro', 'Flame aStro', 'Flame asTro', 'Flame astRo', 'Flame astrO']
    print(wave("Einstein"))  # ['Einstein', 'EInstein', 'EiNstein', 'EinStein', 'EinsTein', 'EinstEin', 'EinsteIn', 'EinsteiN']


# ex203: Given a list of integers, determine whether the sum of its elements is odd or even.
# Give your answer as a string matching "odd" or "even".
# If the input array is empty consider it as: [0] (array with a zero).
# Examples:
# Input: [0]
# Output: "even"

# Input: [0, 1, 4]
# Output: "odd"

# Input: [0, -1, -5]
# Output: "even"
def odd_or_even(arr):
    return "even" if sum(arr) % 2 == 0 else "odd"


if __name__ == "__main__":
    print(odd_or_even([12, 3, 2, 2, 2, 2, 1]))  # even
    print(odd_or_even([21, 8]))  # odd
    print(odd_or_even([0]))  # even


# ex204: Crie uma função que separe vogais e consoantes
def separa_vogais_consoantes(string):
    vogais = [l for l in string.lower() if l in "aáâãàeéêèiíìîoóòôõuúùû"]
    consoantes = [l for l in string.lower() if not l in "aáâãàeéêèiíìîoóòôõuúùû" and l.isalpha()]

    return vogais, consoantes


if __name__ == "__main__":
    print(separa_vogais_consoantes("Python!"))  # (['o'], ['p', 'y', 't', 'h', 'n'])
    print(separa_vogais_consoantes("3JavaScript"))  # (['a', 'a', 'i'], ['j', 'v', 's', 'c', 'r', 'p', 't'])
    print(separa_vogais_consoantes("A matemática é incrível!"))  # (['a', 'a', 'e', 'á', 'i', 'a', 'é', 'i', 'í', 'e'], ['m', 't', 'm', 't', 'c', 'n', 'c', 'r', 'v', 'l'])


# ex205: Crie uma função que calcula porcentagens
def calcula_porcentagem(x, y):
    return f"{x}% de {y} é {x * y / 100}"


if __name__ == "__main__":
    print(calcula_porcentagem(25, 150))  # 25% de 150 é 37.5
    print(calcula_porcentagem(35, 890))  # 35% de 890 é 311.5
    print(calcula_porcentagem(78, 964))  # 78% de 964 é 751.92


# ex206: Given an array of integers, return the element that appears only once in the array.
def unic(arr):
    return [n for n in arr if arr.count(n) == 1][-1]


if __name__ == "__main__":
    print(unic([15, 15, 15, 12]))  # 12
    print(unic([3, 3, 3, 2, 3, 3]))  # 2
    print(unic([25, 12, 12, 12, 12, 12]))  # 25


# ex207 :Create a function with two arguments that will return an array of the first n multiples of x. Assume both the given number and the number of times to count will be positive numbers greater than 0. Return the results as an array or list ( depending on language ).
# Examples
# x = 1, n = 10 --> [1,2,3,4,5,6,7,8,9,10]
# x = 2, n = 5  --> [2,4,6,8,10]
def count_by(x, n):
    return [d for d in range(x, n * x+1, x)]

if __name__ == "__main__":
    print(count_by(1, 10))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(count_by(2, 5))  # [2, 4, 6, 8, 10]
    print(count_by(50, 5))  # [50, 100, 150, 200, 250]


# ex208: Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string (alphabetical ascending), the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.
# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


if __name__ == "__main__":
    print(longest("dosadsakd", "djasldk"))  # adjklos
    print(longest("xyaabbbccccdefww", "xxxxyyyyabklmopq"))  # abcdefklmopqwxy
    print(longest("abcdefghijklmnopqrstuvwxyz", "abcdefghijklmnopqrstuvwxyz"))  # abcdefghijklmnopqrstuvwxyz


# ex209: Efetue o cálculo da quantidade de litros de combustível gastos durante uma viagem. Considere: distancia = tempo * velocidade. litros = distancia / 12
tempo = int(input("Digite o tempo da viagem em horas: "))
velocidade = int(input("Digite a velocidade da viagem em km/h: "))

distancia = tempo * velocidade
litros = distancia / 12

print(f"Distância percorrida: {distancia}")
print(f"O total de litros gastos foram {litros}.")


# ex210: Efetue cálculo e apresente o valor de uma prestação de um bem em atraso, utilizando a forma PRESTAÇÃO = VALOR + (VALOR * (TAXA / 100) * TEMPO)
valor = float(input("Digite o valor do bem em atraso: "))
taxa = float(input("Digite a taxa de juros: "))
tempo = int(input("Digite o tempo em dias: "))

prestacao = valor + (valor * (taxa / 100) * tempo)

print(f"O valor da prestação é de R${prestacao}.")


# ex211: Elaborar um programa que leia dois valores numéricos reais desconhecidos representados pelas variáveis A e B. Calcular e apresentar os resultados das quatro operações aritméticas básicas.
A = float(input('Digite o primeiro número: '))
B = float(input('Digite o segundo número: '))

print(f"A soma entre {A} e {B} é {A + B}")
print(f"A subtração entre {A} e {B} é {A - B}")
print(f"A multiplicação entre {A} e {B} é {A * B}")
print(f"A divisão entre {A} e {B} é {A / B}")


# ex212: Construir um programa que calcule e apresente em metros por segundo o valor da velocidade de um projétil que percorre uma distância em quilômetros a um espaço de tempo em minutos. Utilize a fórmula VELOCIDADE = (DISTÂNCIA * 1000) / (TEMPO * 60)
distancia = float(input("Digite a distância em quilômetros: "))
tempo = int(input("Digite o tempo em minutos: "))

velocidade = (distancia * 1000) / (tempo * 60)
print(f"A velocidade do projétil é de {velocidade} m/s.")


# ex213: Efetuar a leitura de dois valores numéricos inteiros representados pelas variáveis A e B e apresentar o resultado da diferença do maior valor pelo menor valor.
A = float(input("Digite o valor A: "))
B = float(input("Digite o valor B: "))

if A > B:
    print(f"A diferença entre {A} e {B} é de {A - B}")
elif A < B:
    print(f"A diferença entre {B} e {A} é de {B - A}")
else:
    print(f"Ambos são iguais, resultando em 0.")


# ex214: Efetuar a leitura de um valor numérico inteiro positivo ou negativo representado pela variável N e apresentar o valor lido como sendo positivo. Dica: se o valor lido for menor que zero, ele deve ser multiplicado por -1.
N = int(input("Digite um número inteiro: "))

if N >= 0:
    formula = N * 1
else:
    formula = N * -1

print(f"O valor de {N} absoluto é {formula}.")


# ex215: Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno representadas pelas variáveis N1, N2, N3 e N4. Calcular a média aritmética (variável MD) desse aluno e apresentar a mensagem "Aprovado" se a média obtida for maior ou igual a 5; caso contrário, apresentar a mensagem "Reprovado". Informar também, após a apresentação das mensagens, o valor da média obtida pelo aluno.
N1 = float(input('Digite a primeira nota: '))
N2 = float(input('Digite a segunda nota: '))
N3 = float(input('Digite a terceira nota: '))
N4 = float(input('Digite a quarta nota: '))

MD = (N1 + N2 + N3 + N4) / 4

if MD >= 5:
    print("Aprovado")
else:
    print("Reprovado")


print(f"A média é de {MD}")


# ex216: Ler três valores inteiros representados pelas variáveis A, B e C e apresentar os valores lidos dispostos em ordem crescente.
A = int(input('Digite o primeiro número: '))
B = int(input('Digite o segundo número: '))
C = int(input('Digite o terceiro número: '))

lista = [str(A), str(B), str(C)]

print(f'Os números em ordem crescente são {", ".join(sorted(lista))}')


# ex217: Fazer a leitura de quatro valores numéricos inteiros representados pelas variáveis A, B, C e D. Apresentar apenas os valores que sejam divisíveis por 2 e 3.
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))

for n in [A, B, C, D]:
    if n % 2 == 0 and n % 3 == 0:
        print(f"{n} é divisível por 2 e por 3.")


# ex218: Ler cinco valores numéricos inteiros (variáveis A, B, C, D e E), identificar e apresentar o maior e o menor valores informados
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))
D = int(input("Digite o valor de D: "))
E = int(input("Digite o valor de E: "))

valores = sorted([A, B, C, D, E])

print(f"O menor valor é {valores[0]}.")
print(f"O maior valor é {valores[-1]}.")


# ex219: Efetuar a leitura de um valor numérico inteiro que esteja na faixa de valores de 1 até 9. O programa deve apresentar a mensagem "O valor está na faixa permitida", caso o valor informado esteja entre 1 e 9. Se o valor estiver fora da faixa, o programa deve apresentar a mensagem "O valor está fora da faixa permitida".
n = int(input("Digite um valor numérico inteiro: "))

if n >= 1 and n <= 9:
    print("O valor está na faixa permitida")
else:
    print("O valor está fora da faixa permitida")


# ex220: Efetuar a leitura de três valores inteiros desconhecidos representados pelas variáveis A, B e C. Somar os valores fornecidos e apresentar o resultado somente se for maior ou igual a 100.
A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

soma = A + B + C

if soma >= 100:
    print("A soma é maior ou igual a 100.")
else:
    print("A soma está abaixo de 100.")


# ex221: Ler um número inteiro qualquer e multiplicá-lo por dois. Apresentar o resultado da multiplicação somente se o resultado for maior que 30.
n = int(input("Digite um número inteiro qualquer: "))
resultado = n * 2

if resultado > 30:
    print(f"O resultado é {resultado}")


# ex222: Elaborar um programa que apresente como resultado os quadrados dos números inteiros existentes na faixa de valores de 15 a 200.
for i in range(15, 201):
    print(i ** 2)


# ex223: Construir um programa que apresente a soma dos cem primeiros números naturais (1+2+3+ ... +98+99+100).
soma = 0

for i in range(1, 101):
    soma += i

print(f"A soma dos cem primeiros números naturais é de {soma}")  # A soma dos cem primeiros números naturais é de 5050


# ex224: Elaborar um programa que apresente o somatório dos valores pares existentes na faixa de 1 até 500.
soma = 0

for i in range(0, 501, 2):
    soma += i

print(f"A soma dos valores pares existentes na faixa de 1 até 500 é de {soma}")  # A soma dos valores pares existentes na faixa de 1 até 500 é de 62750


# ex225: Elaborar um programa que leia dez valores numéricos reais e apresente no final o somatório e a média dos valores lidos.
soma = 0

for i in range(10):
    n = float(input("Digite um número real: "))
    soma += n

print(f"A soma dos números é {soma}")
print(f"A média dos números é {soma / 10}")


# ex226: Elaborar um programa que leia oito elementos inteiros em uma matriz A do tipo vetor. Construir uma matriz 8 de mesma dimensão com os elementos da matriz A multiplicados por 3. O elemento 8[1] deve ser implicado pelo elemento A[1] * 3, o elemento 8[2] implicado pelo elemento A[2] * 3 e assim por diante, até 8. Apresentar a matriz 8.
lista_A = []

for i in range(8):
    lista_A.append(int(input("Digite um número inteiro: ")))

lista_B = lambda lista: [lista[i] * 3 for i in range(8)]
print(lista_B(lista_A))


# ex227: Imagine uma máquina que possua somente as operações aritméticas de soma e subtração. Escreva um algoritmo para fazer uma multiplicação.

def multiplicacao(a, b):
    soma = 0

    for _ in range(b):
        soma += a

    return soma


if __name__ == "__main__":
    print(multiplicacao(15, 3))  # 45
    print(multiplicacao(12, 7))  # 84
    print(multiplicacao(28, 95))  # 2660


# ex228: Criar uma aplicação que pergunte dois números inteiros. Se não forem iguais, sorteie 0 ou 1. Se for 0, o menor número ganha. Mas se for 1, ganha o maior número.
from random import randint

jogador1 = int(input("Digite o valor de A: "))
jogador2 = int(input("Digite o valor de B: "))

if jogador1 != jogador2:
    numero = randint(0, 1)
    print(f"Número sorteado: {numero}")

    if (numero == 0 and jogador1 < jogador2) or (numero == 1 and jogador1 > jogador2):
        print("Jogador 1 Ganhou!")
    else:
        print("Jogador 2 Ganhou!")
else:
    print(f"Empate")


# ex229: Crie uma função que aceite uma lista de inteiros como parâmetro e retorne cada elemento da lista multiplicado por 3 apenas se este resultar em par.
def pares_triplicados(lista):
    return [x * 3 for x in lista if x * 3 % 2 == 0]


if __name__ == "__main__":
    print(pares_triplicados([12, 5, 2, 10]))  # [36, 6, 30]
    print(pares_triplicados([15, 64, 128, 512, 78]))  # [192, 384, 1536, 234]
    print(pares_triplicados([27, 39, 21, 15]))  # []


# ex230: Given an array of integers, find the one that appears an odd number of times. There will always be only one integer that appears an odd number of times.
# Examples
# [7] should return 7, because it occurs 1 time (which is odd).
# [0] should return 0, because it occurs 1 time (which is odd).
# [1,1,2] should return 2, because it occurs 1 time (which is odd).
# [0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
# [1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).

def find_it(seq):
    return [n for n in seq if seq.count(n) % 2 == 1][0]


if __name__ == "__main__":
    print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1]))  # 4
    print(find_it([0,1,0,1,0]))  # 0
    print(find_it([1,1,2]))  # 2


# ex231: Saudação Personalizada: Peça ao usuário para digitar seu nome e, em seguida, imprima uma saudação personalizada, como "Olá, [Nome do Usuário]!".
nome = input("Digite o seu nome: ")
print(f"Olá, {nome}!")


# ex232: Leia dois nomes de pessoas e os imprima em ordem alfabética.
nome1 = input("Digite o nome da primeira pessoa: ")
nome2 = input("Digite o nome da segunda pessoa: ")

print(", ".join(sorted([nome1, nome2])))


# ex233: Sorteie um número entre 1 e 10 e peça ao usuário para tentar adivinhá-lo. Quando o usuário acertar o número, informe quantas tentativas foram necessárias.
from random import randint

numero = randint(1, 10)
tentativas = 0

while True:
    escolha = int(input("Tente acertar um número de 1 a 10: "))
    while escolha not in range(1, 11):
        escolha = int(input("Por favor, digite corretamente.\nTente acertar um número de 1 a 10: "))

    if escolha == numero:
        print(f"Tentativas necessárias: {tentativas}")
        break
    else:
        print("Tente novamente.")
        tentativas += 1


# ex234: Create a class SoftwareEngineer with "name", "age" and "skills" with parameter. Create a method "about" which says about the Software Engineer
class SoftwareEngineer:
    def __init__(self, name, age, skills):
        self.name = name
        self.age = age
        self.skills = skills

    def about(self):
        print(f"{self.name} is a Software Enginner, with {self.age} years old. He/She has the skills: {", ".join(self.skills)}")


if __name__ == "__main__":
    user001 = SoftwareEngineer("Flame", 34, ["Python", "JavaScript", "HTML", "CSS", "C", "C++", "Linux", "PowerShell", "Git", "GitHub", "Java", "Arduino", "Rapsberry PI"])
    user001.about()  # Flame is a Software Enginner, with 34 years old. He/She has the skills: Python, JavaScript, HTML, CSS, C, C++, Linux, PowerShell, Git, GitHub, Java, Arduino, Rapsberry PI

    user002 = SoftwareEngineer("Julia", 25, ["HTML", "CSS", "React", "Vue", "Tailwind", "Bootstrap", "Git", "GitHub", "JavaScript", "SQL"])
    user002.about()  # Julia is a Software Enginner, with 25 years old. He/She has the skills: HTML, CSS, React, Vue, Tailwind, Bootstrap, Git, GitHub, JavaScript, SQL


# ex235: Média Simples: Peça ao usuário para digitar três notas e calcule a média aritmética.
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

media = sum([n1, n2, n3]) / 3
print(f"A sua média é {media}")


# ex236: Verificar Idade para Votar: Peça a idade do usuário e diga se ele pode votar (idade >= 16).
idade = int(input("Digite a sua idade: "))

if idade >= 16:
    print("Você pode votar!")
else:
    print("Você não tem idade suficiente para votar.")


# ex237: Desconto Simples: Peça o valor de um produto e aplique um desconto de 10%, imprimindo o valor final.
valor = float(input("Digite o valor do produto: "))
resultado = valor - (valor * 10) / 100

print(f"O preço do produto com 10% de desconto é R${resultado}")


# ex238: Aumento de Salário: Peça o salário de um funcionário e aplique um aumento de 5%, imprimindo o novo salário.
salario = float(input("Digite o seu salário: "))
aumento = salario + (salario * 5) / 100

print(f"Seu salário com aumento de 5% é de R${aumento}")


# ex239: Mês do Ano: Peça um número de 1 a 12 e imprima o mês do ano correspondente.
MESES = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

mes = int(input("Digite um mês do ano no formato numérico [1-12]: "))
while mes not in range(1, 13):
    mes = int(input("Por favor, digite um número entre 1 a 12.\nDigite um mês do ano no formato numérico [1-12]: "))

print(f"Mês selecionado: {MESES[mes-1]}")


# ex240: Verificar Vogal ou Consoante: Peça uma letra e diga se é vogal ou consoante.
def vogal_consoante(letra: str) -> str:
    return ["Vogal" if letra.lower() in ["a", "e", "i", "o", "u"] else "Consoante"][0] if letra.isalpha() else "Digite uma letra."

if __name__ == "__main__":
    print(vogal_consoante("A"))  # Vogal
    print(vogal_consoante("D"))  # Consoante
    print(vogal_consoante("&"))  # Digite uma letra.


# ex241: Substring - Peça duas palavras. Verifique se a segunda palavra está contida na primeira.
def substring(p1, p2):
    return p2 in p1


if __name__ == "__main__":
    print(substring("Python", "yth"))  # True
    print(substring("JavaScript", "avo"))  # False
    print(substring("HTML, CSS, React", "3"))  # False


# ex242: Formatar CPF: Peça um CPF (apenas números) e formate-o como XXX.XXX.XXX-XX.
def formata_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


if __name__ == "__main__":
    print(formata_cpf("12345678900"))  # 123.456.789-00
    print(formata_cpf("67489326455"))  # 674.893.264-55
    print(formata_cpf("88976325373"))  # 889.763.253-73


# ex243: Formatar Telefone: Peça um número de telefone (apenas números) e formate-o como (XX) XXXXX-XXXX.
def formata_telefone(telefone) -> str:
    return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}" if len(telefone) == 11 else ""


if __name__ == "__main__":
    print(formata_telefone("51937665634"))  # (51) 93766-5634
    print(formata_telefone("67945342231"))  # (67) 94534-2231
    print(formata_telefone("76987665343"))  # (76) 98766-5343


# ex244: Verificar Idade para Categoria: Peça a idade e classifique em: Criança (0-12), Adolescente (13-17), Adulto (18-59), Idoso (60+).
idade = int(input("Digite a sua idade: "))

if idade >= 0 and idade <= 12:
    print("Criança")
elif idade > 12 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade < 59:
    print("Adulto")
elif idade >= 60 and idade <= 100:
    print("Idoso")
else:
    print("Idade inválida.")


# ex245: Remover Consoantes - Peça uma palavra e imprima-a sem as consoantes.
def remove_consoantes(palavra):
    return "".join([l for l in palavra.lower() if l in ["a", "e", "i", "o", "u", " "]])


if __name__ == "__main__":
    print(remove_consoantes("JavaScript e Python"))  # aai e o
    print(remove_consoantes("Universo e os Multi-Paradoxos"))  # uieo e o uiaaoo
    print(remove_consoantes("Saturno tem ~274 Luas."))  # auo e  ua


# ex246: Remover Elementos Falsy: Dada uma lista, remova todos os elementos que são considerados "falsy" (0, None, False, [], "").
def remove_falsy(lista):
    return [l for l in lista if l is False][0]


if __name__ == "__main__":
    print(remove_falsy([0, None, False, [], ""]))  # False


# ex247: Dado listas dentro de uma outra lista pai, crie uma função que retorne apenas UMA lista com seus respectivos elementos. Exemplo: [["Python"], ["JavaScript"], [5], [True]] -> ["Python", "JavaScript", 5, True]
def lista_unica(lista: list):
    return [element[0] for element in lista]


if __name__ == "__main__":
    lista1 = [["Python"], ["JavaScript"], [5], [True]]
    print(lista_unica(lista1))  # ['Python', 'JavaScript', 5, True]

    lista2 = [[False], ["Linux"], ["GitHub"], [6.78]]
    print(lista_unica(lista2))  # [False, 'Linux', 'GitHub', 6.78]


# ex248: Peça ao usuário 3 números inteiros e diga se eles são iguais ou não
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 == n2 and n1 == n3:
    print("Os números são iguais")
else:
    print("Os números são diferentes")


# ex249: Crie um programa para contagem regressiva para lançamento de foguete de 10 a 0
from time import sleep

# i = 10
# while i >= 1:
#     print(f"{i}...")
#     sleep(1)
#     i -= 1
# print("Lançar!!!")

for i in range(10, 0, -1):
    print(f"{i}...")
    sleep(1)
print("Lançar!!!")


# ex250: Crie uma função que receba x e y como valores inteiros e retorne uma lista de pares e uma lista de ímpares desses ranges.
def pares_impares(x, y):
    pares = [str(n) for n in range(x, y+1) if n % 2 == 0]
    impares = [str(n) for n in range(x, y+1) if n % 2 == 1]

    return (
        f"Ímpares: {", ".join(impares)}\n"
        f"Pares: {", ".join(pares)}"
    )


if __name__ == "__main__":
    print(pares_impares(15, 29))  # Ímpares: 15, 17, 19, 21, 23, 25, 27, 29; Pares: 16, 18, 20, 22, 24, 26, 28
    print(pares_impares(1, 10))  # Ímpares: 1, 3, 5, 7, 9; Pares: 2, 4, 6, 8, 10
    print(pares_impares(25, 50))  # Ímpares: 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49;Pares: 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50


# ex251: Crie uma função que receba uma matriz (Array/Lista bidimensional) com outras sublistas dentro da matriz com números inteiros dentro das sublistas e retorne cada sublista da matriz ordenada com 4 elementos.
# Regras: O argumento da função deve conter uma quantidade indeterminada de sublistas, mas a contagem de cada número deve ser 4. Exemplo: [[2, 1, 1, 1], [2, 2, 1, 2]] -> Explicação: 2 e 1 aparecem 4 vezes na matriz, mas em sublistas diferentes.
# Exemplo: [[2, 1, 1, 1], [2, 2, 1, 2]] -> Deve retornar: [[1, 1, 1, 1], [2, 2, 2, 2]]
# Exemplo: [[4, 3, 2, 1], [1, 1, 3, 1], [2, 4, 3, 2], [4, 4, 3, 2]] -> Deve retornar: [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
# Exemplo: [[7, 3, 4, 4], [4, 3, 7, 3], [4, 7, 7, 3]] -> Deve retornar: [[3, 3, 3, 3], [4, 4, 4, 4], [7, 7, 7, 7]]
def matriz_ordenada(matriz):
    return [sorted([n for l in matriz for n in l])[i-4:i] for i in range(0, len(matriz*4)+1, 4)][1:]


if __name__ == "__main__":
    print(matriz_ordenada([[2, 1, 1, 1], [2, 2, 1, 2]]))  # [[1, 1, 1, 1], [2, 2, 2, 2]]
    print(matriz_ordenada([[4, 3, 2, 1], [1, 1, 3, 1], [2, 4, 3, 2], [4, 4, 3, 2]]))  # [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
    print(matriz_ordenada([[7, 3, 4, 4], [4, 3, 7, 3], [4, 7, 7, 3]]))  # [[3, 3, 3, 3], [4, 4, 4, 4], [7, 7, 7, 7]]


# ex252: Crie uma função que receba uma hora do dia como parâmetro e retorne a seção do dia por extenso
def mensagem(hora: int):
    return "Bom dia!" if hora >= 6 and hora <= 11 else "Boa tarde!" if hora >= 12 and hora <= 17 else "Boa noite!" if hora >= 18 and hora <= 23 else "Hora de dormir!" if hora == 24 or hora >= 0 and hora <= 5 else "Hora inválida."


if __name__ == "__main__":
    print(mensagem(1))  # Hora de dormir!
    print(mensagem(62))  # Hora inválida.
    print(mensagem(24))  # Hora de dormir!
    print(mensagem(12))  # Boa tarde!
    print(mensagem(7))  # Bom dia!
    print(mensagem(17))  # Boa tarde!


# ex253: Count the number of Duplicates
# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

# Example
# "abcde" -> 0 # no characters repeats more than once
# "aabbcde" -> 2 # 'a' and 'b'
# "aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
# "indivisibility" -> 1 # 'i' occurs six times

def duplicate_count(text):
    letters = []

    for string in text.lower():
        if string not in letters and text.lower().count(string) > 1:
            letters.append(string)

    return len(letters)


if __name__ == "__main__":
    print(duplicate_count("abcdeaB"))
    print(duplicate_count("Wm18tVKzlsW6uPYCy6JAvsss5Y642VLxKOJcTPqcsb"))


# ex254: Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).

# Examples
# n = 0  ==> [1]        # [2^0]
# n = 1  ==> [1, 2]     # [2^0, 2^1]
# n = 2  ==> [1, 2, 4]  # [2^0, 2^1, 2^2]
def powers_of_two(n):
    return [2 ** i for i in range(0, n+1)]


if __name__ == "__main__":
    print(powers_of_two(0))  # [1]
    print(powers_of_two(1))  # [1, 2]
    print(powers_of_two(2))  # [1, 2, 4]
    print(powers_of_two(3))  # [1, 2, 4, 8]
    print(powers_of_two(4))  # [1, 2, 4, 8, 16]
    print(powers_of_two(5))  # [1, 2, 4, 8, 16, 32]
    print(powers_of_two(35))  # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824, 2147483648, 4294967296, 8589934592, 17179869184, 34359738368]


# ex255: Crie uma função que receba um texto como parâmetro e retorne o texto embaralhado, sem nenhuma ordem.
from random import randint

def embaralha_texto(texto):
    letra = ""
    lista = []
    tamanho = len(texto)
    numero = randint(0, tamanho-1)

    while len(lista) != tamanho:
        while numero in lista:
            numero = randint(0, tamanho-1)

        letra += texto[numero]
        lista.append(numero)

    return letra


if __name__ == "__main__":
    print(embaralha_texto("Flame"))  # maleF;  Fmael
    print(embaralha_texto("Ghost Fly"))  #  loGthysF;  Gtshy oFl
    print(embaralha_texto("Astronomia"))  # nsAmairoto;  onstoiramA


# ex256: Your function takes two arguments:
# current father's age (years)
# current age of his son (years)
# Сalculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - (son_years_old * 2))


if __name__ == "__main__":
    print(twice_as_old(34, 11))  # 12
    print(twice_as_old(23, 45))  # 67
    print(twice_as_old(33, 19))  # 5


# ex257: You will be given a list of strings. You must sort it alphabetically (case-sensitive, and based on the ASCII values of the chars) and then return the first value.
# The returned value must be a string, and have "***" between each of its letters.
# You should not remove or add elements from/to the array.
def two_sort(array):
    return "***".join(list(sorted(array)[0]))


if __name__ == "__main__":
    print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))  # b***i***t***c***o***i***n
    print(two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]))  # a***r***e
    print(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]))  # c***o***d***e


# ex258: altERnaTIng cAsE <=> ALTerNAtiNG CaSe
# Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:

# "hello world".toAlternatingCase() === "HELLO WORLD"
# "HELLO WORLD".toAlternatingCase() === "hello world"
# "hello WORLD".toAlternatingCase() === "HELLO world"
# "HeLLo WoRLD".toAlternatingCase() === "hEllO wOrld"
# "12345".toAlternatingCase()       === "12345"                   // Non-alphabetical characters are unaffected
# "1a2b3c4d5e".toAlternatingCase()  === "1A2B3C4D5E"
# "String.prototype.toAlternatingCase".toAlternatingCase() === "sTRING.PROTOTYPE.TOaLTERNATINGcASE"
# As usual, your function/method should be pure, i.e. it should not mutate the original string.
def to_alternating_case(string: str):
    return string.swapcase()


if __name__ == "__main__":
    print(to_alternating_case("Flame"))


# ex259: In this kata you will create a function that takes in a list and returns a list with the reverse order.
# Examples (Input -> Output)
# * [1, 2, 3, 4]  -> [4, 3, 2, 1]
# * [9, 2, 0, 7]  -> [7, 0, 2, 9]
def reverse_list(list1):
    # return list(reversed(list1))
    # return list1[::-1]
    list2 = []

    for e in list1:
        list2.insert(0, e)

    return list2


if __name__ == "__main__":
    print(reverse_list([1, 2, 3, 4]))  # [4, 3, 2, 1]
    print(reverse_list([9, 12, 4, 5, 3]))  # [3, 5, 4, 12, 9]
    print(reverse_list([9, 45, 2, 3, 1]))  # [1, 3, 2, 45, 9]


# ex260: Write a program that takes a string, (1) capitalizes the first letter, (2) creates a list containing each word, and (3) searches for the last occurrence of ”a” in the first word.
string = input("Type the string: ")

print(f"Capitalized: {string.capitalize()}")
print(f"Words: {string.split()}")
print(f"Last occurrence of \"a\" in the first word: {string.rfind("a")}")


# ex261: Write a program that replaces all instances of ”one” with ”one (1)”. For this exercise, capitalization does not matter, so it should treat ”one”, ”One”, and ”oNE” identically.
string = input("Type a string: ")

print(f"{string.lower().replace("one", "one (1)")}")


# ex262: Use a list comprehension to construct the list [’ab’, ’ac’, ’ad’, ’bb’, ’bc’, ’bd’].
print([fix + var for fix in ["a", "b"] for var in ["b", "c", "d"]])  # ['ab', 'ac', 'ad', 'bb', 'bc', 'bd']


# ex263: Use a slice on the above list to construct the list [’ab’, ’ad’, ’bc’].
original_list = [fix + var for fix in ["a", "b"] for var in ["b", "c", "d"]]
print(original_list[::2])  # ['ab', 'ad', 'bc']
