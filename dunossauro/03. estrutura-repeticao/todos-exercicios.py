# ex001: Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = int(input("Digite uma nota entre 0 a 10: "))
while nota not in range(0, 11):
    print("Por favor, insira uma nota entre 0 a 10.")
    nota = int(input("Digite uma nota entre 0 a 10: "))

print(f"A nota digitada foi {nota}")


# ex002: Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
usuario = input("Crie um nome de usuário: ").strip()
senha = input("Crie uma senha: ").strip()

if usuario == "admin" and senha == "admin":
    print("Uau, que belo nome e senha para serem invadidos!")

while usuario == senha:
    print("Ooops, certifique-se de inserir uma senha diferente do seu nome de usuário!")
    usuario = input("Crie um nome de usuário: ").strip()
    senha = input("Crie uma senha: ").strip()


# ex003: Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 2 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Estado Civil: 's', 'c', 'v', 'd';
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
salario = float(input("Digite o seu salário: "))
estado_civil = input("Digite o seu estado civil: ").lower().strip()

print("Nome válido" if len(nome) > 2 else "Nome inválido")
print("Idade válida" if idade in range(0, 151) else "Idade inválida")
print("Salário válido" if salario > 0 else "Salário inválido")
print("Estado Civil válido" if estado_civil in ['s', 'c', 'v', 'd'] else "Estado Civil inválido")


# ex004: Supondo que a população de um país A seja da ordem de 80_000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200_000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
paisA = {
    "habitantes": 80000,
    "taxa de crescimento": 0.03
}

paisB = {
    "habitantes": 200000,
    "taxa de crescimento": 0.015
}

anos = 0
while paisA["habitantes"] < paisB["habitantes"]:
    paisA["habitantes"] += paisA["habitantes"] * paisA["taxa de crescimento"]
    paisB["habitantes"] += paisB["habitantes"] * paisB["taxa de crescimento"]

    anos += 1

print(f"Em {anos} anos, o País A terá {paisA['habitantes']:.0f} habitantes e o País B terá {paisB['habitantes']:.0f}.")


# ex005: Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
habitantesA = int(input("Digite o total de habitantes do país A: "))
while habitantesA not in range(0, 10**12):
    print(f"Por favor, insira uma quantidade válida.")
    habitantesA = int(input("Digite o total de habitantes do país A: "))

taxa_crescimentoA = float(input("Digite a porcentagem da taxa de crescimento do país A: %"))
while taxa_crescimentoA <= 0:
    print("Certifique-se de inserir um valor adequado.")
    taxa_crescimentoA = float(input("Digite a porcentagem da taxa de crescimento do país A: %"))

habitantesB = int(input("Digite o total de habitantes do país B: "))
while habitantesB not in range(0, 10**12):
    print(f"Por favor, insira uma quantidade válida.")
    habitantesB = int(input("Digite o total de habitantes do país B: "))

taxa_crescimentoB = float(input("Digite a porcentagem da taxa de crescimento do país B: %"))
while taxa_crescimentoB <= 0:
    print("Certifique-se de inserir um valor adequado.")
    taxa_crescimentoB = float(input("Digite a porcentagem da taxa de crescimento do país B: %"))

if taxa_crescimentoB > taxa_crescimentoA:
    print("Ooops, não é possível fazer o cálculo quando a taxa de crescimento do país B é maior que a do país A.")
else:
    anos = 0
    while habitantesA < habitantesB:
        habitantesA += (habitantesA * taxa_crescimentoA) / 100
        habitantesB += (habitantesB * taxa_crescimentoB) / 100

        anos += 1

    print(f"Seram necessários {anos} anos para que o país A ultrapasse do país B em população.")


# ex006: Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
numeros = []
for numero in range(1, 21):
    print(numero)
    numeros.append(str(numero))

print(", ".join(numeros))


# ex007: Faça um programa que leia 5 números e informe o maior número.
numeros = []

for i in range(5):
    numero = int(input(f"Insira o {i+1}o número inteiro: "))
    numeros.append(numero)

print(f"O maior número inserido foi {sorted(numeros)[-1]}")


# ex008: Faça um programa que leia 5 números e informe a soma e a média dos números.
soma = 0
for i in range(5):
    numero = float(input(f"Digite o {i+1}o número: "))
    soma += numero

media = soma / 5
print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")


# ex009: Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
print(", ".join([str(numero) for numero in range(1, 51, 2)]))


# ex010: Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
n1 = int(input("Insira o primeiro número inteiro: "))
n2 = int(input("Insira o segundo número inteiro: "))

if n1 > n2:
    for numero in range(n1, n2-1, -1):
        print(numero)
else:
    for numero in range(n1, n2+1):
        print(numero)


# ex011: Altere o programa anterior para mostrar no final a soma dos números.
n1 = int(input("Insira o primeiro número inteiro: "))
n2 = int(input("Insira o segundo número inteiro: "))

soma = 0
if n1 > n2:
    for numero in range(n1, n2-1, -1):
        print(numero)
        soma += numero
else:
    for numero in range(n1, n2+1):
        print(numero)
        soma += numero

print(f"A soma dos números é: {soma}")


# ex012: Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50
numero = int(input("Qual o número da tabuada deseja? "))

for i in range(1, 11):
    print(f"{numero} X {i} = {numero * i}")


# ex013: Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

if expoente == 0:
    print(1)
else:
    resultado = base
    for i in range(1, abs(expoente)):
        resultado *= base

    if expoente < 0:
        print(f"O resultado da exponenciação é {1 / resultado}")
    else:
        print(f"O resultado da exponenciação é {resultado}")


# ex014: Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
pares = 0
impares = 0
for i in range(10):
    numero = int(input(f"Insira o {i+1}o numero inteiro: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"A quantidade de números pares é de {pares}")
print(f"A quantidade de números impares é de {impares}")


# ex015: A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
quantidade = int(input("Digite o n-ésimo termo: "))
termos = []
termo = 1

for i in range(0, quantidade+1):
    if len(termos) != 0:
        termo = termo + int(termos[i-1])
    else:
        termos.append(str(termo))
    termos.append(str(termo))

print(f"Termos: {",".join(termos)}")


# ex016: A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
termos = []
termo = 1
i = 0

while True:
    if len(termos) != 0:
        termo = termo + int(termos[i-1])
    else:
        termos.append(str(termo))
    termos.append(str(termo))

    if termo >= 500:
        break

    i += 1

print(f"Termos: {",".join(termos)}")


# ex017: Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
numero = int(input("Insira o número que deseja descobrir o fatorial: "))
fatorial = 1

for i in range(1, numero+1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial} ({"x".join([str(x) for x in range(numero, 0, -1)])} = {fatorial})")


# ex018: Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
conjunto = []
while True:
    numero = int(input("Digite um número ou -1 para sair: "))

    if numero == -1:
        break

    conjunto.append(numero)

conjunto = sorted(conjunto)

maior = conjunto[-1]
menor = conjunto[0]

soma = 0
for numero in conjunto:
    soma += numero

print(f"O maior número do conjunto é: {maior}.")
print(f"O menor número do conjunto é: {menor}.")
print(f"A soma dos números do conjunto é: {soma}.")


# ex019: Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
conjunto = []
while True:
    numero = int(input("Digite um número entre 0 a 1000 ou 0 para sair: "))
    while numero not in range(0, 1001):
        print("Por favor, insira um número entre 0 a 1001.")
        numero = int(input("Digite um número entre 0 a 1000 ou 0 para sair: "))


    if numero == 0:
        break

    conjunto.append(numero)

conjunto = sorted(conjunto)

maior = conjunto[-1]
menor = conjunto[0]

soma = 0
for numero in conjunto:
    soma += numero

print(f"O maior número do conjunto é: {maior}.")
print(f"O menor número do conjunto é: {menor}.")
print(f"A soma dos números do conjunto é: {soma}.")


# ex020: Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.
quantidade = int(input("Quantas vezes deseja calcular o fatorial de algum número? "))
while quantidade not in range(0, 11):
    print("O valor da quantidade é muito alto. Tente um valor entre 0 a 10.")
    quantidade = int(input("Quantas vezes deseja calcular o fatorial de algum número? "))

for _ in range(quantidade):
    numero = int(input("Insira o número que deseja descobrir o fatorial: "))
    while numero not in range(1, 17):
        print("Por favor, certifique-se de inserir um valor válido.")
        numero = int(input("Insira o número que deseja descobrir o fatorial: "))

    fatorial = 1

    for i in range(1, numero+1):
        fatorial *= i

    print(f"O fatorial de {numero} é {fatorial} ({"x".join([str(x) for x in range(numero, 0, -1)])} = {fatorial})")


# ex021: Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.
numero = int(input("Insira um número inteiro: "))

divisores = [divisivel for divisivel in range(1, (numero // 2) + 1) if numero % divisivel == 0]

if len(divisores) > 1:
    print(f"{numero} não é um número primo (número composto)")
else:
    print(f"{numero} é um número primo.")


# ex022: Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
numero = int(input("Insira um número inteiro: "))

divisores = [str(divisivel) for divisivel in range(1, (numero // 2) + 1) if numero % divisivel == 0]

if len(divisores) > 1:
    print(f"{numero} não é um número primo (número composto)")
    print(f"Seus divisores são: {", ".join(divisores)}")
else:
    print(f"{numero} é um número primo.")


# ex023: Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
import math

N = int(input("Digite um número inteiro: "))
total_divisoes = 0

print(f"Números primos entre 1 e {N}:")

for num in range(2, N + 1):
    primo = True

    for i in range(2, int(math.sqrt(num)) + 1):
        total_divisoes += 1
        if num % i == 0:
            primo = False
            break
    if primo:
        print(num, end=' ')

print(f"\n\nTotal de divisões executadas: {total_divisoes}")


# ex024: Faça um programa que calcule e mostre a média aritmética de N notas.
quantidade = 0
soma = 0

while True:
    nota = float(input("Insira uma nota: "))
    while nota not in range(0, 11):
        print("Considere digitar uma nota válida.")
        nota = float(input("Insira uma nota: "))

    soma += nota
    quantidade += 1

    continuar = input("Deseja continuar? [S/N]: ").upper().strip()
    while continuar not in ["S", "N"]:
        print("Por favor, insira S para SIM e N para NÃO")
        continuar = input("Deeseja continuar? [S/N]: ").upper().strip()

    if continuar == "N":
        break

media = soma / quantidade

print(f"A média das notas é de {media:.2f}")


# ex025: Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
soma = 0
quantidade = 0

while True:
    idade = int(input("Insira a sua idade: "))

    while idade not in range(0, 121):
        print("Por favor, considere inserir uma idade válida.")
        idade = int(input("Insira a sua idade: "))

    soma += idade
    quantidade += 1

    continuar = input("Deseja continuar? [S/N] ").upper().strip()
    while continuar not in ["S", "N"]:
        print("Por favor, certifique-se de inserir S para SIM e N para NÃO")
        continuar = input("Deeseja continuar? [S/N] ").upper().strip()

    if continuar == "N":
        break


media = soma / quantidade

if media >= 0 and media <= 25:
    print("A média varia entre 0 a 25 - Turma Jovem")
elif media > 25 and media <= 60:
    print("A média varia entre 26 a 60 - Turma Adulta")
elif media > 60:
    print(f"A média varia dos 60+ - Turma Idosa")

