# Estrutura Condicional
# ex001: Faça um programa que peça dois números e imprima o maior deles.
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))

if n1 > n2:
    print(f"{n1} é maior que {n2}")
elif n2 > n1:
    print(f"{n2} é maior que {n1}")
else:
    print("Ambos são iguais...")


# ex002: Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print("POSITIVO")
elif numero < 0:
    print("NEGATIVO")
else:
    print("NULO (0)")


# ex003: Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino
# M - Masculino
# Sexo Inválido.
letra = input("Digite o seu gênero (M/F): ")

if letra == "M":
    print("Masculino")
elif letra == "F":
    print("Feminino")
else:
    print("Sexo inválido")


# ex004: Faça um programa que verifique se uma letra digitada é vogal ou consoante.
letra = input("Digite uma letra: ").lower()

if len(letra) == 1:
    VOGAIS = ["a", "e", "i", "o", "u"]
    CONSOANTES = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    if letra in VOGAIS:
        print("A letra digitada é uma VOGAL.")
    elif letra in CONSOANTES:
        print("A letra digitada é uma CONSOANTE.")
    else:
        print("Ooops, você não inseriu uma letra do alfabeto, certifique-se de inserir uma das 26 letras do alfabeto.")
else:
    print(f"Por favor, insira uma letra. Você inseriu uma palavra com {len(letra)} caracteres.")


# ex005: Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.
nota1 = float(input("Digite a primeira nota: "))
while nota1 not in range(0, 11):
    print("Por favor, certifique-se de inserir uma nota válida.")
    nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))
while nota2 not in range(0, 11):
    print("Por favor, certifique-se de inserir uma nota válida.")
    nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com Distinção")
else:
    print("Oops, algo deu errado! Por favor, tente novamente.")


# ex006: Faça um programa que leia três números e mostre o maior deles.
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))

if n1 > n2 and n1 > n3:
    print(f"O maior número é o primeiro -> {n1}")
elif n2 > n1 and n2 > n3:
    print(f"O maior número é o segundo -> {n2}")
elif n3 > n1 and n3 > n2:
    print(f"O maior número é o terceiro -> {n3}")
else:
    if n1 == n2 and n1 == n3:
        print(f"Todos são iguais -> {n1}")
    elif n1 == n2:
        print(f"Ambos o primeiro e o segundo número são iguais -> {n1}")
    elif n2 == n3:
        print(f"Ambos o segundo e o terceiro número são iguais -> {n2}")
    elif n1 == n3:
        print(f"Ambos o primeiro e o terceiro números sao iguais -> {n1}")


# ex007: Faça um programa que leia três números e mostre o maior e o menor deles:
n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = int(input("Digite o terceiro número inteiro: "))

if n1 < n2 and n1 < n3:
    print(f"O menor número é o primeiro -> {n1}")
elif n2 < n1 and n2 < n3:
    print(f"O menor número é o segundo -> {n2}")
elif n3 < n1 and n3 < n2:
    print(f"O menor número é o terceiro -> {n3}")
else:
    if n1 == n2 and n1 == n3:
        print(f"Todos são iguais -> {n1}")
    elif n1 == n2:
        print(f"Ambos o primeiro e o segundo número são iguais -> {n1}")
    elif n2 == n3:
        print(f"Ambos o segundo e o terceiro número são iguais -> {n2}")
    elif n1 == n3:
        print(f"Ambos o primeiro e o terceiro números sao iguais -> {n1}")


# ex008: Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:
produto1 = float(input("Informe o primeiro produto: "))
produto2 = float(input("Informe o segundo produto: "))
produto3 = float(input("Informe o terceiro produto: "))

if produto1 < produto2 and produto1 < produto3:
    print(f"Você deve comprar o primeiro produto -> {produto1}")
elif produto2 < produto1 and produto2 < produto3:
    print(f"Você deve comprar o segundo produto -> {produto2}")
elif produto3 < produto1 and produto3 < produto2:
    print(f"Você deve comprar o terceiro produto -> {produto3}")
else:
    if produto1 == produto2 and produto1 == produto3:
        print(f"Todos são iguais -> {produto1}")
    elif produto1 == produto2:
        print(f"Ambos o primeiro e o segundo produto são iguais -> {produto1}")
    elif produto2 == produto3:
        print(f"Ambos o segundo e o terceiro produto são iguais -> {produto2}")
    elif produto1 == produto3:
        print(f"Ambos o primeiro e o terceiro produto são iguais -> {produto1}")


# ex009: Faça um programa que leia três números e mostre-os em ordem decrescente
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

print(f"Os números em ordem decrescente são: {", ".join(sorted([str(numero) for numero in [n1, n2, n3]], reverse=True))}")


# ex010: Faça um programa que pergunte em que turno você estuda. Peça para digitar:
# M - Matutino
# V - Vespertino
# N - Noturno.
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
print("Selecione o seu turno correspondente.")
print("Digite M para Matutino")
print("Digite V para Vespertino")
print("Digite N para Noturno")

turno = input("Em que turno você estuda/trabalha? ").upper()

if turno == "M":
    print("Bom Dia!")
elif turno == "V":
    print("Boa Tarde!")
elif turno == "N":
    print("Boa Noite!")
else:
    print("Valor Inválido!")


# ex011: As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.
salario = float(input("Digite o valor do seu salário: "))

if salario <= 280:
    aumento = salario * 0.20
    percentual = 20
elif salario > 280 and salario <= 700:
    aumento = salario * 0.15
    percentual = 15
elif salario > 700 and salario <= 1500:
    aumento = salario * 0.10
    percentual = 10
elif salario > 1500:
    aumento = salario * 0.05
    percentual = 5

print(" Detalhes ".center(25, "-"))
print(f"O salário antes do aumento era de R${salario}")
print(f"O percentual do aumento aplicado sobre o salário foi de {percentual}%")
print(f"O valor do aumento foi de R${aumento}")
print(f"O novo salário com o aumento é de R${salario + aumento}")


# ex012: Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

# Desconto do IR:
# Salário Bruto até 900 (inclusive) -> isento
# Salário Bruto até 1500 (inclusive) -> desconto de 5%
# Salário Bruto até 2500 (inclusive) -> desconto de 10%
# Salário Bruto acima de 2500 -> desconto de 20%

# Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

# Salário Bruto: (5 * 220)        : R$ 1100,00
# (-) IR (5%)                     : R$   55,00
# (-) INSS ( 10%)                 : R$  110,00
# FGTS (11%)                      : R$  121,00
# Total de descontos              : R$  165,00
# Salário Liquido                 : R$  935,00
ganho_hora = float(input("Quantos reais você ganha por hora? "))
horas_mes = int(input("Quantas horas você trabalha por mês? "))

salario_bruto = ganho_hora * horas_mes
if salario_bruto <= 900:
    PORCENTAGEM_IR = 0
elif salario_bruto > 900 and salario_bruto <= 1500:
    PORCENTAGEM_IR = 5
elif salario_bruto > 1500 and salario_bruto <= 2500:
    PORCENTAGEM_IR = 10
elif salario_bruto > 2500:
    PORCENTAGEM_IR = 20

IR = salario_bruto * (PORCENTAGEM_IR / 100)
INSS = salario_bruto * 0.10
SINDICATO = salario_bruto * 0.03
FGTS = salario_bruto * 0.11

total_descontos = IR + INSS + SINDICATO
salario_liquido = salario_bruto - total_descontos

print(f"Salário Bruto: ({ganho_hora} * {horas_mes})         : R$ {salario_bruto:.2f}")
print(f"(-) IR ({PORCENTAGEM_IR}%)                        : R$ {IR:.2f}")
print(f"(-) INSS (10%)                     : R$ {INSS:.2f}")
print(f"(-) Sindicato (3%)                 : R$ {SINDICATO:.2f}")
print(f"FGTS (11%)                         : R$ {FGTS:.2f}")
print(f"Total de Descontos                 : R$ {total_descontos:.2f}")
print(f"Salário Líquido                    : R$ {salario_liquido:.2f}")


# ex013: Faça um programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
print(" Tabela dos Valores ".center(50, "-"))
DIAS = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"]

for i in range(7):
    print(f"{i+1} - {DIAS[i]}")

numero = int(input("Digite um número que corresponde a um dia da semana: "))
while numero not in range(1, 8):
    print("Por favor, certifique-se de escolher um valor válido.")
    numero = int(input("Digite um número que corresponde a um dia da semana: "))

print(f"Você escolheu {DIAS[numero-1]}")


# ex014: Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

# Média de Aproveitamento  Conceito
# Entre 9.0 e 10.0         A
# Entre 7.5 e 9.0          B
# Entre 6.0 e 7.5          C
# Entre 4.0 e 6.0          D
# Entre 4.0 e zero         E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
nota1 = float(input("Digite a sua primeira nota: "))
while nota1 not in range(0, 11):
    print("Por favor, insira uma nota válida.")
    nota1 = float(input("Digite a sua primeira nota: "))

nota2 = float(input("Digite a sua segunda nota: "))
while nota2 not in range(0, 11):
    print("Por favor, insira uma nota válida.")
    nota2 = float(input("Digite a sua segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
    conceito = "A"
elif media >= 7.5 and media < 9:
    conceito = "B"
elif media >= 6 and media < 7.5:
    conceito = "C"
elif media >= 4 and media < 6:
    conceito = "D"
elif media >= 0 and media < 4:
    conceito = "E"


print(f"A primeira nota foi {nota1}")
print(f"A segunda nota foi {nota2}")
print(f"A média das notas é {media}")
print(f"O conceito é {conceito}")
print(f"Você foi... {'APROVADO' if conceito in ["A", "B", "C"] else 'REPROVADO'}")


# ex015: Faça um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;
lado1 = float(input("Digite o primeiro lado do triângulo: "))
lado2 = float(input("Digite o segundo lado do triângulo: "))
lado3 = float(input("Digite o terceiro lado do triângulo: "))

if (lado1 + lado2) > lado3:
    if lado1 == lado2 and lado1 == lado3:
        print("Triângulo Equilátero")
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print("Triângulo Isósceles")
    elif lado1 != lado2 and lado1 != lado3:
        print("Triângulo Escaleno")
else:
    print("Isso não é um triângulo.")


# ex016: Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

# Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
from math import sqrt

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if a == 0:
    print("Isso não é uma equação do segundo grau.")
else:
    DELTA = (b ** 2) * -4 * a * c

    if DELTA < 0:
        print(f"A equação não possui raízes reais.")
    elif DELTA == 0:
        print(f"A equação possui apenas uma raíz real.")
    else:
        print(f"A equação possui duas raízes reais.")
        conjunto = {(-b + sqrt(DELTA)) / (2 * a), (-b - sqrt(DELTA)) / (2 * a)}

        for x in conjunto:
            print(x)


# ex017: Faça um programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
ano = int(input("Insira um ano qualquer: "))

if (ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0)):
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto.")


# Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
def valida_data():
    data = input("Digite uma data no formato dd/mm/aaaa: ")
    if data.count("/") != 2:
        return "❌ Data inválida."

    data = data.split("/")
    for elemento in data:
        if not elemento.isnumeric():
            return "❌ Data inválida."

    if (len(data[0]) != 2 or int(data[0]) < 1 or int(data[0]) > 33) or (len(data[1]) != 2 or int(data[1]) < 1 or int(data[1]) > 12):
        return "❌ Data inválida."

    return "✅ Data válida."


print(valida_data())
