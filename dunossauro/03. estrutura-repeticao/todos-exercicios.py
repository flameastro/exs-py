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


# ex026: Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
eleitores = int(input("Qual o número total de eleitores?\n>>> "))
while eleitores not in range(1, 101):
    print("Insira um número adequado - Entre 1 a 100.")
    eleitores = int(input("Qual o número total de eleitores?\n>>> "))

votos = []
for eleitor in range(eleitores):
    print("Seja bem vindo, eleitor! Aqui está uma pequena lista dos candidatos que você pode votar: ")
    print("1 para votar em José dos Campos")
    print("2 para votar em Marcos do Peixaral")
    print("3 para votar em Frangolina Victória Regina.")

    voto = int(input("Insira o número do candidato:\n>>> "))
    while voto not in range(1, 4):
        print("Por favor, considere inserir um voto válido.")
        voto = int(input("Insira o número do candidato:\n>>> "))

    votos.append(voto)


candidato1 = votos.count(1)
candidato2 = votos.count(2)
candidato3 = votos.count(3)

print(f" RESULTADO DA VOTAÇÃO ".center(50, "-"))
print(f"{'Candidato':<20} Qntd. Votos")
print(f"{'1':<20} {candidato1}")
print(f"{'2':<20} {candidato2}")
print(f"{'3':<20} {candidato3}")

if candidato1 > candidato2 and candidato1 > candidato3:
    print("O candidato 1 é o vencedor!!!")
elif candidato2 > candidato1 and candidato2 > candidato3:
    print("O candidato 2 é o vencedor!!!")
elif candidato3 > candidato1 and candidato3 > candidato2:
    print("O candidato 3 é o vencedor!!!")
elif candidato1 == candidato2 and candidato1 == candidato3:
    print("Todos empataram.")
elif candidato1 == candidato2 and candidato1 != candidato3:
    print(f"Houve um empate entre candidato 1 e candidato 2.")
elif candidato1 == candidato3 and candidato1 != candidato2:
    print(f"Houve um empate entre candidato 1 e candidato 3.")
elif candidato2 == candidato3 and candidato2 != candidato1:
    print(f"Houve um empate entre candidato 2 e candidato 3.")


# ex027: Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos.
turmas = int(input("Insira a quantidade de turmas:\n>>> "))
while turmas not in range(1, 25):
    print("Considere inserir um valor entre 1 a 25 turmas.")
    turmas = int(input("Insira a quantidade de turmas:\n>>> "))

total = 0

for turma in range(turmas):
    alunos = int(input(f"Quantos alunos há na turma {turma+1}?\n>>> "))
    while alunos not in range(10, 41):
        print("⚠️ A turma deve possui entre 10 a 40 alunos.")
        alunos = int(input(f"Quantos alunos há na turma {turma+1}?\n>>> "))

    total += alunos

media = total / turmas

print(f"A média de alunos por turma é de {media:.2f}")


# ex028: Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um.
quantidade_cds = int(input("Quantos CDs o colecionador possui? "))
while quantidade_cds not in range(1, 1001):
    print("Por favor, considere inserir uma quantidade válida.")
    quantidade_cds = int(input("Quantos CDs o colecionador possui? "))

total = 0

for cd in range(quantidade_cds):
    valor = float(input(f"Qual foi o valor em reais gasto pelo CD {cd+1}? R$"))
    while valor not in range(0, 10**9):
        print("Por favor, considere inserir um valor válido.")
        valor = float(input(f"Qual foi o valor em reais gasto pelo CD {cd+1}? R$"))

    total += valor

media = total / quantidade_cds

print(f"A média dos valores dos cds em reais é R${media:.2f}")


# ex029: O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o número de itens que o cliente comprou e ao lado o valor da conta. Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme o exemplo abaixo:

# Lojas Quase Dois - Tabela de preços
# 1 - R$ 1.99
# 2 - R$ 3.98
# ...
# 50 - R$ 99.50
print("Lojas Quase Dois - Tabela de preços")
preco = 1.99

for i in range(1, 51):
    print(f"{i} - R$ {(preco * i):.2f}")


# ex030: O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

# Preço do pão: R$ 0.18
# Panificadora Pão de Ontem - Tabela de preços
# 1 - R$ 0.18
# 2 - R$ 0.36
# ...
# 50 - R$ 9.00
print("Panificadora Pão de Ontem - Tabela de preços")
preco = 0.18

for i in range(1, 51):
    print(f"{i} - R$ {preco}")


# ex031: O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

# Lojas Tabajara
# Produto 1: R$ 2.20
# Produto 2: R$ 5.80
# Produto 3: R$ 0
# Total: R$ 9.00
# Dinheiro: R$ 20.00
# Troco: R$ 11.00
print("Lojas Tabajara")
total = 0
i = 1
while True:
    preco = float(input(f"Produto {i}: R$ "))
    while preco < 0:
        print("Certifique-se de inserir um valor positivo.")
        preco = float(input(f"Produto {i}: R$ "))

    total += preco

    if preco == 0:
        break

    i += 1

print(f"Total: {total:.2f}")

dinheiro = float(input("Dê o dinheiro ao caixa: R$ "))
if dinheiro >= total:
    troco = dinheiro - total
    print(f"Total: {total:.2f}")
    print(f"Dinheiro: {dinheiro:.2f}")
    print(f"Troco: {troco:.2f}")
else:
    print("Oops, não é possível realizar o pagamento, pois o dinheiro é menor que o total da compra.")


# ex032: Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
# Fatorial de: 5 5! = 5 . 4 . 3 . 2 . 1 = 120
numero = int(input("Insira o número que deseja descobrir o fatorial: "))
fatorial = 1

for i in range(1, numero+1):
    fatorial *= i

print(f"Fatorial de {numero}! = {" . ".join([str(x) for x in range(numero, 0, -1)])} = {fatorial}")


# ex033: O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
print(" Instruções ".center(50, "-"))
print("Digite uma temperatura em graus celsius")
print("Digite -0.1 para sair")
print("".center(50, "-"))
temperaturas = []
contador = 1

while True:
    temperatura = float(input(f"Insira a temperatura {contador}: "))

    if temperatura == -0.1:
        break

    temperaturas.append(temperatura)
    contador += 1

menor = min(temperaturas)
maior = max(temperaturas)
media = sum(temperaturas) / len(temperaturas)

print(f"A menor temperatura registrada foi {menor:.2f} graus celsius.")
print(f"A maior temperatura registrada foi {maior:.2f} graus celsius.")
print(f"A média das temperaturas registradas é de {media:.2f} graus celsius.")


# ex034: Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
numero = int(input("Insira um número inteiro: "))

divisores = [divisivel for divisivel in range(1, (numero // 2) + 1) if numero % divisivel == 0]

if len(divisores) > 1:
    print(f"{numero} não é um número primo (número composto)")
else:
    print(f"{numero} é um número primo.")


# ex035: Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
numero = int(input("Insira um número inteiro: "))

divisores = [divisivel for divisivel in range(1, (numero // 2) + 1) if numero % divisivel == 0]

if len(divisores) > 1:
    print(divisores)
else:
    print(f"{numero} não possui divisores, é um número primo.")


# ex036: Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
# Montar a tabuada de: 5
# Começar por: 4
# Terminar em: 7
# Vou montar a tabuada de 5 começando em 4 e terminando em 7:
# 5 X 4 = 20
# 5 X 5 = 25
# 5 X 6 = 30
# 5 X 7 = 35
# Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
numero = int(input("Montar a tabuada de: "))
comeco = int(input("Começar por: "))
termino = int(input("Terminar em: "))

if comeco >= termino:
    print("Opps, não é possível realizar a tabuada deste número.")
else:
    print(f"Vou montar a tabuada de {numero} começando em {comeco} e terminando em {termino}:")
    for x in range(comeco, termino+1):
        print(f"{numero} X {x} = {numero * x}")


# ex037: Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes
print(" INSTRUÇÕES ".center(50, "-"))
print("No campo da altura, preencha no formato metro.centimetros (exemplos: 1.65, 1.87, 1.86, 1.84, 2.13)")
print("No campo do peso, preencha no formato quilo.grama (ex: 87.50, 45.3, 125.65, 98.75, 56.75)")
print("Digite \"0\" para sair.")
alturas = []
pesos = []

while True:
    codigo = int(input("Digite o seu código da academia: "))
    if codigo == 0:
        break

    altura = float(input("Digite a sua altura: "))
    peso = float(input("Digite o seu peso: "))

    alturas.append(altura)
    pesos.append(peso)

if len(alturas) != 0:
    mais_alto = max(alturas)
    mais_baixo = min(alturas)
    mais_gordo = max(pesos)
    mais_magro = min(pesos)
    media_alturas = sum(alturas) / len(alturas)

    print(f"O cliente mais alto possui {mais_alto}cm.")
    print(f"O cliente mais baixo possui {mais_baixo}cm.")
    print(f"O cliente mais gordo possui {mais_gordo}kg.")
    print(f"O cliente mais magro possui {mais_magro}kg.")
    print(f"A média das alturas é de {media_alturas}cm.")
    print(f"O peso dos clientes é de: {", ".join([f'{str(peso)}kg' for peso in pesos])}")
else:
    print("Não é possível realizar operações sem dados.")


# ex038: Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

# Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
# Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
# A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
# Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
# v1
from datetime import date

salario = 1000
aumento = 0.015  # 1,5%
ano_inicial = 1995
ano_atual = date.today().year

for ano in range(1996, ano_atual + 1):
    salario += salario * aumento
    aumento *= 2

print(f"Salário atual em {ano_atual}: R$ {salario:.2f}")


# v2
from datetime import date

salario = float(input("Digite o salário inicial do funcionário: R$ "))
aumento = 0.015
ano_inicial = 1995
ano_atual = date.today().year

for ano in range(1996, ano_atual + 1):
    salario += salario * aumento
    aumento *= 2

print(f"Salário atual em {ano_atual}: R$ {salario:.2f}")


# ex039: Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
numeros = []
alturas = []
for i in range(10):
    numero_aluno = int(input("Digite o número do aluno: "))
    if numero_aluno in numeros:
        print("Este número de aluno já foi cadastrado. Considere-se inserir outro número.")
        numero_aluno = int(input("Digite o número do aluno: "))

    altura = float(input("Digite a altura do aluno: "))

    numeros.append(numero_aluno)
    alturas.append(altura)

altura_mais_alto = max(alturas)
altura_mais_baixo = min(alturas)
numero_mais_alto = numeros[alturas.index(altura_mais_alto)]
numero_mais_baixo = numeros[alturas.index(altura_mais_baixo)]

print(f"O aluno com a maior altura possui {altura_mais_alto}cm e tem o número {numero_mais_alto}")
print(f"O aluno com a menor altura possui {altura_mais_baixo}cm e tem o número {numero_mais_baixo}")


# ex040: Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:

# Código da cidade;
# Número de veículos de passeio (em 1999);
# Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
# Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
# Qual a média de veículos nas cinco cidades juntas;
# Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
maior_indice = -1
menor_indice = 999999
cidade_maior = 0
cidade_menor = 0
total_veiculos = 0
total_acidentes_menor2000 = 0
cont_menor2000 = 0

for i in range(5):
    print(f"\n--- Cidade {i+1} ---")
    codigo = int(input("Código da cidade: "))
    veiculos = int(input("Número de veículos de passeio: "))
    acidentes = int(input("Número de acidentes com vítimas: "))

    total_veiculos += veiculos

    if acidentes > maior_indice:
        maior_indice = acidentes
        cidade_maior = codigo

    if acidentes < menor_indice:
        menor_indice = acidentes
        cidade_menor = codigo

    if veiculos < 2000:
        total_acidentes_menor2000 += acidentes
        cont_menor2000 += 1

media_veiculos = total_veiculos / 5
if cont_menor2000 > 0:
    media_acidentes_menor2000 = total_acidentes_menor2000 / cont_menor2000
else:
    media_acidentes_menor2000 = 0

print("\n--- RESULTADOS ---")
print(f"Maior índice de acidentes: {maior_indice} (Cidade {cidade_maior})")
print(f"Menor índice de acidentes: {menor_indice} (Cidade {cidade_menor})")
print(f"Média de veículos nas 5 cidades: {media_veiculos:.2f}")
print(f"Média de acidentes nas cidades com menos de 2000 veículos: {media_acidentes_menor2000:.2f}")


# ex041: Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.

# Os juros e a quantidade de parcelas seguem a tabela abaixo:

# Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
# 1       0
# 3       10
# 6       15
# 9       20
# 12      25
# Exemplo de saída do programa:

# Valor da Dívida   Valor dos Juros     Quantidade de Parcelas      Valor da Parcela
# R$ 1.000,00       0                   1                           R$  1.000,00
# R$ 1.100,00       100                 3                           R$    366,00
# R$ 1.150,00       150                 6                           R$    191,67
divida = float(input("Valor da dívida: R$ "))

parcelas_juros = [
    (1, 0),
    (3, 10),
    (6, 15),
    (9, 20),
    (12, 25)
]

print("\nValor da Dívida\tValor dos Juros\tQuantidade de Parcelas\tValor da Parcela")

for qtd_parcelas, juros in parcelas_juros:
    valor_juros = divida * (juros / 100)
    valor_total = divida + valor_juros
    valor_parcela = valor_total / qtd_parcelas

    print(f"R$ {valor_total:10.2f}\tR$ {valor_juros:10.2f}\t{qtd_parcelas:>10}\t\tR$ {valor_parcela:10.2f}")


# ex042: Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
numeros = []
while True:
    numero = int(input("Insira um número: "))
    while numero > 100:
        print("Por favor, insira um número menor que 100.")
        numero = int(input("Insira um número: "))

    if numero <= 0:
        break

    numeros.append(numero)

media = sum(numeros) / len(numeros)
print(f"Média: {media:.2f}")

if media >= 0 and media <= 25:
    print("Os números informados estão no intervalo de 0 a 25.")
elif media >= 26 and media <= 50:
    print("Os números informados estão no intervalo de 26 a 50.")
elif media >= 51 and media <= 75:
    print("Os números informados estão no intervalo de 51 a 75.")
elif media >= 76 and media <= 100:
    print("Os números informados estão no intervalo de 76 a 100.")


# ex043: O cardápio de uma lanchonete é o seguinte:

# Especificação   Código  Preço
# Cachorro Quente 100     R$ 1,20
# Bauru Simples   101     R$ 1,30
# Bauru com ovo   102     R$ 1,50
# Hambúrguer      103     R$ 1,20
# Cheeseburguer   104     R$ 1,30
# Refrigerante    105     R$ 1,00
# Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago por item (preço * quantidade).
print("Especificação   Código  Preço")
print("Cachorro Quente 100     R$ 1,20")
print("Bauru Simples   101     R$ 1,30")
print("Bauru com ovo   102     R$ 1,50")
print("Hambúrguer      103     R$ 1,20")
print("Cheeseburguer   104     R$ 1,30")
print("Refrigerante    105     R$ 1,00")

codigo = int(input("Digite o código do item: "))
while codigo not in range(100, 106):
    print("Por favor, insira um código válido.")
    codigo = int(input("Digite o código do item: "))

quantidade = int(input("Digite a quantidade do item: "))

if codigo == 100 or codigo == 103:
    preco = 1.20
elif codigo == 101 or codigo == 104:
    preco = 1.30
elif codigo == 102:
    preco = 1.50
elif codigo == 105:
    preco = 1

print(f"O preço total do pedido é de R${preco * quantidade}")


# ex044: Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

# 1 , 2, 3, 4  - Votos para os respectivos candidatos
# (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:

# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
print(" INFORMAÇÕES SOBRE A ELEIÇÃO ".center(50, "-"))
print("1 - João Matheus Araújo")
print("2 - Felipe Gonçalves")
print("3 - Matheus Cândido ")
print("4 - Lucas Rafael dos Santos")
print("5 - Voto Nulo")
print("6 - Voto em Branco")

votos = []

while True:
    codigo = int(input("Digite o código de acordo com o candidato desejado: "))
    if codigo == 0:
        break

    while codigo not in range(1, 7):
        print("Certifique-se de inserir um código válido: ")
        codigo = int(input("Digite o código de acordo com o candidato desejado: "))

    votos.append(codigo)

print(f" RESULTADOS DA ELEIÇÃO ".center(50, "-"))
print(f"Total de votos: {len(votos)}") # EXTRA
print(f"Total de votos para o candidato 1 (João Matheus Araújo): {votos.count(1)}")
print(f"Total de votos para o candidato 2 (Felipe Gonçalves): {votos.count(2)}")
print(f"Total de votos para o candidato 3 (Matheus Cândido): {votos.count(3)}")
print(f"Total de votos para o candidato 4 (Lucas Rafael dos Santos): {votos.count(4)}")
print(f"Total de votos nulos: {votos.count(5)}")
print(f"Total de votos em branco: {votos.count(6)}")
print(f"Porcentagem de votos nulos sobre o total de votos: {((votos.count(5) / len(votos)) * 100):.2f}%")
print(f"Porcentagem de votos em branco sobre o total de votos: {((votos.count(6) / len(votos)) * 100):.2f}%")
