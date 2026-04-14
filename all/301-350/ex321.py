# ex321: Crie um programa para armazenar o nome do jogador e a quantidade de gols de 10 jogadores de um time. Ao finalizar a leitura dos jogadores, o algoritmo deve apresentar na tela o nome e a quantidade de gols do melhor jogador do time.
nomes = []
gols = []

mais_gols_nome = [""]
mais_gols = [0]

for jogador in range(10):
    print(f"- - - - - JOGADOR {jogador+1} - - - - -")
    nome = input("Nome do Jogador: ")
    nomes.append(nome)

    quantidade_gols = int(input("Quantidade de Gols: "))
    gols.append(quantidade_gols)

    if mais_gols[0] < quantidade_gols:
        mais_gols[0] = quantidade_gols
        mais_gols_nome[0] = nome
    elif mais_gols[0] == quantidade_gols:
        mais_gols_nome.append(nome)

if len(mais_gols_nome) > 1:
    print(f"Os jogadores com a maior quantidade de gols são {", ".join(mais_gols_nome)}")
    print(f"Os jogadores com a maior pontuação fizeram {mais_gols[0]} gols")
else:
    print(f"O jogador com a maior quantidade de gols é {mais_gols_nome[0]}")
    print(f"O jogador {mais_gols_nome[0]} fez {mais_gols[0]} gols")
