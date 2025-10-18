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
