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
