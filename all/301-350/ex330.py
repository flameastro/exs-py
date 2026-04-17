# ex330: Crie um programa que pergunte ao usuário o nome do aluno, a nota 1 e a nota 2 e calcule a média das notas 1 e 2, armazenando todos esses dados em um array, e em seguida, "cobrindo" todos eles com mais um array, formando assim uma matriz (listas de listas). O seu programa deve repetir isso até o usuário quiser parar. O final esperado é:
# ------------------- R E S U L T A D O S --------------------
# Número     Nome           Média
# [num cresc.] [nome]        [media]
#  ... 
# E em seguida, exibir a mensagem:
# Mostrar notas de qual aluno? [999 para parar]
# Ao usuário clicar o número do aluno, o programa deve exibir quais foram as notas daquele respectivo aluno.
quantidade = 0
boletim = []

while True:
    quantidade = 1
    print(f"--- Aluno {quantidade} ---")

    nome = input("Insira o nome: ").capitalize().strip()
    nota1 = float(input("Primeira nota: "))
    nota2 = float(input("Segunda nota: "))
    media = (nota1 + nota2) / 2

    boletim.append([nome, nota1, nota2, media])

    continuar = input("Deseja continuar? [S/N]: ").upper().strip()
    while continuar not in ["S", "N"]:
        print("Certifique-se de inserir um valor correto")
        continuar = input("Deseja continuar? [S/N]: ").upper().strip()
    if continuar == "N":
        break

print("------------------- R E S U L T A D O S --------------------")
print("Número     Nome           Média")
contador = 0

for linha in boletim:
    print(f"{contador:<10} {linha[0]:<10} {linha[-1]:>8}")
    contador += 1

while True:
    mostrar_notas = int(input("Mostrar notas de qual aluno? [999 para parar] "))
    if mostrar_notas == 999:
        print("Programa Finalizado")
        break
    try:
        print(f"Notas de {boletim[mostrar_notas][0]} são {boletim[mostrar_notas][1:3]}")
    except:
        print("Ocorreu um erro ao tentar acessar.")
print("------------------------------------------------------------")
