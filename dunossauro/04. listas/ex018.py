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
