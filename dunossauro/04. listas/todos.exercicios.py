# ex001: Faça um programa que leia um vetor de 5 números inteiros e mostre-os.
vetor = []
for x in range(5):
    vetor.append(int(input("Insira um número: ")))

print(vetor)


# ex002: Faça um programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
vetor = []
for x in range(10):
    vetor.append(int(input("Insira um número: ")))

print(list(reversed(vetor)))


# ex003: Faça um programa que leia 4 notas, mostre as notas e a média na tela.
soma = 0
for n in range(4):
    nota = int(input(f"Digite a {["primeira", "segunda", "terceira", "quarta"][n]} nota: "))
    while nota not in range(0, 11):
        print("Insira uma nota válida.")
        nota = int(input(f"Digite a {["primeira", "segunda", "terceira", "quarta"][n]} nota: "))

    soma += nota

media = soma / 4

print(f"Média: {media:.2f}")


# ex004: Faça um programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
consoantes = 0
for i in range(10):
    caractere = input("Digite um caractere: ").upper().strip()
    while not caractere.isalpha() or len(caractere) != 1:
        print("Certifique-se de inserir uma letra válida.")
        caractere = input("Digite um caractere: ").upper().strip()

    if caractere not in ["A", "E", "I", "O", "U"]:
        consoantes += 1

print(f"Foram inseridos ao todo {consoantes} consoantes.")


# ex005: Faça um programa que leia 10 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
par = []
impar = []
numeros = []

for i in range(10):
    numero = int(input("Insira um número: "))

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

    numeros.append(numero)


print(f"Números inseridos: {numeros}")
print(f"Números PARES: {par}")
print(f"Números ÍMPARES: {impar}")


# ex006: Faça um programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
medias = []

for aluno in range(10):
    notas = []

    for n in range(4):
        nota = float(input(f"Digite a nota do aluno {aluno+1}: "))
        while nota < 0 or nota > 10:
            print("Por favor, considere inserir uma nota válida.")
            nota = float(input(f"Digite a nota do aluno {aluno+1}: "))

        notas.append(nota)

    media = sum(notas) / 4
    medias.append(str(media))

aprovados = len([x for x in medias if float(x) >= 7])
print(f"O número de alunos com média superior a 7 é {aprovados}.")


# ex007: Faça um programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
numeros = []
multiplicacao = 1
soma = 0
for x in range(5):
    numero = int(input("Digite um numero inteiro: "))

    numeros.append(str(numero))

    multiplicacao *= numero
    soma += numero


print(f"A soma dos números informados é de {soma}")
print(f"A multiplicação entre os números resulta em {multiplicacao}")
print(f"Os números informados são {", ".join(numeros)}")


# ex008: Faça um programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
idades = []
alturas = []

for x in range(5):
    idade = int(input("Idade: "))
    while idade not in range(0, 121):
        print("Por favor, insira um valor adequado.")
        idade = int(input("Idade: "))

    altura = float(input("Altura: "))
    while altura < 0 or altura > 3:
        print("Por favor, digite um valor para a altura que seja válido.")
        altura = float(input("Altura: "))

    idades.append(idade)
    alturas.append(altura)


print(idades[::-1])
print(alturas[::-1])


# ex009: Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
lista = []
for i in range(10):
    numero = int(input("Insira um número inteiro: "))
    lista.append(str(numero ** 2))

print(f"Lista com o cálculo dos quadrados dos elementos: {", ".join(lista)}")


# ex010: Faça um programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
lista1 = []
lista2 = []

for i in range(5):
    valor = input("Insira qualquer valor (vetor 1): ")
    lista1.append(valor)

for i in range(5):
    valor = input("Insira qualquer valor (vetor 2): ")
    lista2.append(valor)

lista = []
for i in range(5):
    lista.append(lista1[i])
    lista.append(lista2[i])

print(lista)


# ex011: Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
lista1 = []
lista2 = []
lista3 = []

for _ in range(5):
    valor = input("Insira qualquer valor (vetor 1): ")
    lista1.append(valor)

for _ in range(5):
    valor = input("Insira qualquer valor (vetor 2): ")
    lista2.append(valor)

for _ in range(5):
    valor = input("Insira qualquer valor (vetor 2): ")
    lista3.append(valor)

lista = []
for i in range(5):
    lista.append(lista1[i])
    lista.append(lista2[i])
    lista.append(lista3[i])

print(lista)


# ex012: Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
idades = []
alturas = []

for aluno in range(30):
    idade = int(input("Idade: "))
    while idade not in range(0, 80):
        print("Por favor, insira um valor adequado.")
        idade = int(input("Idade: "))

    altura = float(input("Altura: "))
    while altura < 0 or altura > 3:
        print("Por favor, digite um valor para a altura que seja válido.")
        altura = float(input("Altura: "))

    idades.append(idade)
    alturas.append(altura)

media = sum(alturas) / 30
altura_inferior = 0

for i in range(30):
    if idades[i] > 13 and alturas[i] < media:
        altura_inferior += 1

print(f"A quantidade total de alunos que possui mais de 13 anos e há uma altura inferior em relação à média é de: {altura_inferior}")


# ex013: Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, ...).
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []
for i in range(12):
    temperatura = float(input(f"Temperatura do mês {meses[i]}: "))
    temperaturas.append(temperatura)

media = sum(temperaturas) / 12
print(f"A média das temperaturas é de {media:.2f}")

i = 0
while i < 12:
    if temperaturas[i] > media:
        print(meses[i])

    i += 1


# ex014: Utilizando listas, faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Devia para a vítima?"
# "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
perguntas = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
pontos = 0
for x in range(5):
    print(perguntas[x])
    resposta = input("Responda: ").upper().strip()

    while resposta not in ["S", "N"]:
        print("Insira S para SIM e N para NÃO")
        resposta = input("Responda: ").upper().strip()

    if resposta == "S":
        pontos += 1

if pontos == 5:
    classificacao = "Assasino"
elif pontos >= 3:
    classificacao = "Cúmplice"
elif pontos > 1:
    classificacao = "Suspeita"
else:
    classificacao = "Inocente"

print(f"A pessoa possui {pontos} pontos.")
print(f"Classificação: {classificacao}")


# ex015: Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:

# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;
notas = []
while True:
    nota = float(input("Nota: "))
    if nota == -1:
        break

    while nota < 0 or nota > 10:
        print("Por favor, certifique-se de inserir um valor válido.")
        nota = float(input("Nota: "))

    notas.append(nota)


if len(notas) != 0:
    soma = sum(notas)
    media = soma / len(notas)

    print(f"{'Quantidade de valores lidos':40} {len(notas)}")
    print(f"{'Valores informados':40} {", ".join([str(x) for x in notas])}")
    print(f"{'Valores informados (ordem inversa)':40} {", ".join([str(x) for x in notas[::-1]])}")
    print(f"{'Soma dos valores informados':40} {soma:.2f}")
    print(f"{'Média dos valores informados':40} {media:.2f}")
    print(f"{'Quantidade de valores acima da média':40} {len([x for x in notas if x > media])}")
    print(f"{'Quantidade de valores abaixo de 7':40} {len([x for x in notas if x < 7])}")
    print("-- END! --")
else:
    print("Impossível realizar operações sem nenhum dado.")


# ex016: Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:

# $200 - $299
# $300 - $399
# $400 - $499
# $500 - $599
# $600 - $699
# $700 - $799
# $800 - $899
# $900 - $999
# $1000 em diante
valor_semana = 200
porcentagem = 0.09
intervalos = [0] * 9

while True:
    venda_bruta = float(input("Venda Bruta (0 para sair): R$"))
    if venda_bruta == 0:
        break

    while venda_bruta < 0 or venda_bruta > 100000:
        print("Por favor, insira um valor válido.")
        venda_bruta = float(input("Venda Bruta: R$"))

    salario = valor_semana + (porcentagem * venda_bruta)

    if salario >= 1000:
        intervalos[8] += 1
    else:
        indice = int((salario - 200) // 100)
        intervalos[indice] += 1

print("\nDistribuição de salários:")
for i in range(8):
    print(f"${200 + i*100} - ${299 + i*100}: {intervalos[i]} vendedores")
print(f"$1000 ou mais: {intervalos[8]} vendedores")


# ex017: Em uma competição de salto em distância, cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. A saída do programa deve ser conforme o exemplo abaixo:

# Atleta: Rodrigo Curvêllo

# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m
while True:
    saltos = []
    atleta = input("Atleta: ")
    if atleta == "":
        break

    for x in range(5):
        salto = float(input(f"{["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"][x]} Salto: "))
        while salto < 0 or salto > 50:
            print("Por favor, insira um valor correto.")
            salto = float(input(f"{["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"][x]} Salto: "))

        saltos.append(salto)

    media = sum(saltos) / 5

    print(" RESULTADO FINAL ".center(50, "-"))
    print(f"Atleta: {atleta.title()}")
    print(f"Saltos: {" - ".join(str(x) for x in saltos)}")
    print(f"Média dos saltos: {media:.2f}")
    print("-" * 50)


# ex018: Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23, correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:

# O total de votos computados; Os números e respectivos votos de todos os jogadores que receberam votos; O percentual de votos de cada um destes jogadores; O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.

# Observe que os votos inválidos e o zero final não devem ser computados como votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa. Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição apresentada na tela.
# Enquete: Quem foi o melhor jogador?

# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 11
# Número do jogador (0=fim): 10
# Número do jogador (0=fim): 50
# Informe um valor entre 1 e 23 ou 0 para sair!
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 9
# Número do jogador (0=fim): 0

# Resultado da votação:

# Foram computados 8 votos.


# Jogador         Votos           %
# 9               4               50,0%
# 10              3               37,5%
# 11              1               12,5%
# O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
votos = []
while True:
    numero_camisa = int(input("Número do jogador (0=fim): "))
    if numero_camisa == 0:
        break

    while numero_camisa < 0 or numero_camisa > 23:
        print("Informe um valor entre 1 e 23 ou 0 para sair!")
        numero_camisa = int(input("Número do jogador (0=fim): "))

    votos.append(numero_camisa)

print(f"Total de votos: {len(votos)}")
print(f"{'Jogador':<10} {'Pontos':<10} {'Porcentagem'}")
jogadores = []
quantidade_votos = []
for jogador in votos:
    if jogador not in jogadores:
        print(f"{jogador:<10} {votos.count(jogador):<10} {((votos.count(jogador) / len(votos)) * 100):.2f}%")
        jogadores.append(jogador)
        quantidade_votos.append(votos.count(jogador))


melhor_jogador = jogadores[quantidade_votos.index(max(quantidade_votos))]
qntd_votos_melhor_jogador = max(quantidade_votos)
print(f"O melhor jogador foi o número {melhor_jogador}, com {qntd_votos_melhor_jogador} votos, correspondendo a {((qntd_votos_melhor_jogador / len(votos)) * 100):.2f}% do total de votos. ")


# ex019: Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:

# "Qual o melhor Sistema Operacional para uso em servidores?"

# As possíveis respostas são:

# 1- Windows Server
# 2- Unix
# 3- Linux
# 4- Netware
# 5- Mac OS
# 6- Outro
# Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num vetor. Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

# Sistema Operacional     Votos   %
# -------------------     -----   ---
# Windows Server           1500   17%
# Unix                     3500   40%
# Linux                    3000   34%
# Netware                   500    5%
# Mac OS                    150    2%
# Outro                     150    2%
# -------------------     -----
# Total                    8800

# O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
print("Qual o melhor Sistema Operacional para uso em servidores?")
print("1- Windows Server")
print("2- Unix")
print("3- Linux")
print("4- Netware")
print("5- MacOS")
print("6- Outro")

SOs = ["Windows Server", "Unix", "Linux", "Netware", "MacOS", "Outro"]
votos = [0] * 6

while True:
    sistema_operacional = int(input("Escolha o sistema operacional (1-6) ou 0 para encerrar: "))

    if sistema_operacional == 0:
        break
    elif 1 <= sistema_operacional <= 6:
        votos[sistema_operacional - 1] += 1
    else:
        print("Valor inválido! Digite um número entre 0 e 6.")

total_votos = sum(votos)

print("\nSistema Operacional     Votos   %")
print("-" * 35)
for i in range(6):
    percentual = (votos[i] / total_votos) * 100 if total_votos > 0 else 0
    print(f"{SOs[i]:<22} {votos[i]:<7} {percentual:.2f}%")

print("-" * 35)
print(f"Total de votos: {total_votos}")

mais_votado = max(votos)
indice_vencedor = votos.index(mais_votado)
percentual_vencedor = (mais_votado / total_votos) * 100 if total_votos > 0 else 0

print(f"\nO Sistema Operacional mais votado foi o {SOs[indice_vencedor]}, "
      f"com {mais_votado} votos, correspondendo a {percentual_vencedor:.2f}% dos votos.")


# ex020: As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.

# Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:

# Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro;
# O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo;
# Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima.

# Ao final, o programa deverá apresentar:

# O salário de cada funcionário, juntamente com o valor do abono;
# O número total de funcionário processados;
# O valor total a ser gasto com o pagamento do abono;
# O número de funcionário que receberá o valor mínimo de 100 reais;
# O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.

# Projeção de Gastos com Abono
# ============================ 

# Salário: 1000
# Salário: 300
# Salário: 500
# Salário: 100
# Salário: 4500
# Salário: 0

# Salário    - Abono     
# R$ 1000.00 - R$  200.00
# R$  300.00 - R$  100.00
# R$  500.00 - R$  100.00
# R$  100.00 - R$  100.00
# R$ 4500.00 - R$  900.00

# Foram processados 5 colaboradores
# Total gasto com abonos: R$ 1400.00
# Valor mínimo pago a 3 colaboradores
# Maior valor de abono pago: R$ 900.00
print("Projeção de Gastos com Abono")
print("============================")

salarios = []
abonos = []

while True:
    salario = float(input("Salário: "))
    if salario == 0:
        break
    salarios.append(salario)

    abono = salario * 0.2
    if abono < 100:
        abono = 100
    abonos.append(abono)

print("\nSalário    - Abono")
for i in range(len(salarios)):
    print(f"R$ {salarios[i]:7.2f} - R$ {abonos[i]:7.2f}")

total_funcionarios = len(salarios)
total_gasto = sum(abonos)
qtd_minimo = abonos.count(100)
maior_abono = max(abonos) if abonos else 0

print(f"\nForam processados {total_funcionarios} colaboradores")
print(f"Total gasto com abonos: R$ {total_gasto:.2f}")
print(f"Valor mínimo pago a {qtd_minimo} colaboradores")
print(f"Maior valor de abono pago: R$ {maior_abono:.2f}")


# ex021: Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:

# O modelo do carro mais econômico;
# Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro.
# Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.

# Comparativo de Consumo de Combustível

# Veículo 1
# Nome: fusca
# Km por litro: 7
# Veículo 2
# Nome: gol
# Km por litro: 10
# Veículo 3
# Nome: uno
# Km por litro: 12.5
# Veículo 4
# Nome: Vectra
# Km por litro: 9
# Veículo 5
# Nome: Peugeout
# Km por litro: 14.5

# Relatório Final
# 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
# 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
# 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
# 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
# 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
# O menor consumo é do peugeout.
modelos = []
consumos = []

for i in range(5):
    print(f"Veículo {i + 1}")
    modelo = input("Nome: ").strip()
    consumo = float(input("Km por litro: "))
    modelos.append(modelo)
    consumos.append(consumo)
    print()

print("\nRelatório Final")

DISTANCIA = 1000
PRECO_GASOLINA = 2.25

menor_consumo = None
modelo_mais_economico = ""

for i in range(5):
    litros = DISTANCIA / consumos[i]
    custo = litros * PRECO_GASOLINA
    print(f"{i + 1} - {modelos[i]:15} - {consumos[i]:5.1f} - {litros:7.1f} litros - R$ {custo:6.2f}")

    if menor_consumo is None or litros < menor_consumo:
        menor_consumo = litros
        modelo_mais_economico = modelos[i]

print(f"\nO menor consumo é do {modelo_mais_economico}.")
