# ex004: Faça um programa que verifique se uma letra digitada é vogal ou consoante.
letra = input("Digite uma letra: ").lower()

if len(letra) == 1:
    VOGAIS = ["a", "e", "i", "o", "u"]
    CONSOANTES = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    if letra in VOGAIS:
        print("A letra digitada é uma VOGAL.")
    elif letra in CONSOANTES:
        print("A letra digitada é uma CONSOANTE.")
    else:
        print("Ooops, você não inseriu uma letra do alfabeto, certifique-se de inserir uma das 26 letras do alfabeto.")
else:
    print(f"Por favor, insira uma letra. Você inseriu uma palavra com {len(letra)} caracteres.")
