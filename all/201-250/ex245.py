# ex245: Remover Consoantes - Peça uma palavra e imprima-a sem as consoantes.
def remove_consoantes(palavra):
    return "".join([l for l in palavra.lower() if l in ["a", "e", "i", "o", "u", " "]])


if __name__ == "__main__":
    print(remove_consoantes("JavaScript e Python"))  # aai e o
    print(remove_consoantes("Universo e os Multi-Paradoxos"))  # uieo e o uiaaoo
    print(remove_consoantes("Saturno tem ~274 Luas."))  # auo e  ua
