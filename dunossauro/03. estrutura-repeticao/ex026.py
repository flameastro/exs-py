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
