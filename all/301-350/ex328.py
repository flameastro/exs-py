# ex328: Você foi contratado para desenvolver um sistema de exibição do boletim digital de um curso de inglês. Seu sistema deve armazenar e apresentar a informação de 15 alunos.
# Cada aluno passa por 3 avaliações (prova oral, prova escrita e conversação). Além da nota dessas avaliações, seu sistema ainda deve registrar a média final de cada aluno.
alunos = []
for aluno in range(15):
    print(f"---- ALUNO {aluno+1} ----")

    nome = input("Nome do(a) Aluno(a): ")
    prova_oral = float(input("Qual foi sua nota na prova oral? "))
    prova_escrita = float(input("Qual foi sua nota na prova escrita? "))
    conversacao = float(input("Qual foi sua nota em conversação? "))
    media = (prova_oral + prova_escrita + conversacao) / 3

    alunos.append([nome, prova_oral, prova_escrita, conversacao, media])


print("INFORMAÇÕES DOS ALUNOS")
print(f"{"ALUNO":<10} {"NOME":<20} {"MEDIA"}")
for posicao, aluno in enumerate(alunos):
    print(f"{posicao+1:<10} {aluno[0]:<20} {aluno[-1]}")
