# ex045: Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:

# 01 - E
# 02 - A
# 03 - C
# 04 - B
# 05 - B
# 06 - C
# 07 - D
# 08 - A
# 09 - B
# 10 - E
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
gabarito = {
    1: "E",
    2: "A",
    3: "C",
    4: "B",
    5: "B",
    6: "C",
    7: "D",
    8: "A",
    9: "B",
    10: "E"
}

resultados = []
while True:
    nota = 0

    for i in range(1, 11):
        questao = input("Assinale a alternativa correta: ").upper().strip()
        while questao not in ["A", "B", "C", "D", "E"]:
            print("Assinale uma alternativa correta (A - E)")
            questao = input("Assinale a alternativa correta: ").upper().strip()

        if gabarito.get(i) == questao:
            nota += 1

    print(f"Sua nota foi {nota}.")
    resultados.append(nota)

    continuar = input("Deseja continuar? [S/N]: ").upper().strip()
    while continuar not in ["S", "N"]:
        print("Certifique-se de inserir um valor correto. S para SIM e N para NÃO")
        continuar = input("Deseja continuar? [S/N]: ").upper().strip()

    if continuar == "N":
        break
    elif continuar == "S":
        continue

print(" RESULTADOS DAS PROVAS ".center(50, "="))
print(f"O maior acerto foi {max(resultados)}")
print(f"O menor acerto foi {min(resultados)}")
print(f"Total de alunos: {len(resultados)}")
print(f"Media de notas da turma: {(sum(resultados) / len(resultados)):.2f}")
print("Gabarito da prova")
for questao, reposta in gabarito.items():
    print(f"{questao} - {reposta}")
