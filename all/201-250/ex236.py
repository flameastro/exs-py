# ex236: Verificar Idade para Votar: Peça a idade do usuário e diga se ele pode votar (idade >= 16).
idade = int(input("Digite a sua idade: "))

if idade >= 16:
    print("Você pode votar!")
else:
    print("Você não tem idade suficiente para votar.")
