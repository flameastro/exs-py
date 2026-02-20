# ex007: Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
# quantos espaços em branco existem na frase.
# quantas vezes aparecem as vogais a, e, i, o, u.
string = input("STRING: ").lower()
VOGAIS = ["a", "e", "i", "o", "u"]

numero_vogais = 0
for vogal in VOGAIS:
    numero_vogais += string.count(vogal)

print(f"Aparecem {sum([string.count(x) for x in VOGAIS])} vogais na string.")
print(f"A string possui {string.count(" ")} espaços em branco.")
