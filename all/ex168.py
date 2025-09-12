# ex168: Dois amigos desejam trocar informações entre si num chat de bots. Os amigos querem conversar sobre hacking, e os bots filtram qualquer tipo de palavra inadequada e relacionada a hacking. Sabendo disso, os dois amigos criaram algumas substituições. A = 4; I = 1;E = 3;S = 5; O = 0.
# Crie uma função que receba uma string como parâmetro e retorne a string com as substituições.
# Atenção: APENAS PARA FINS DIDÁTICOS.
def substituir_caracteres(string: str) -> str:
    string = string.lower()
    string = string.replace("a", "4")
    string = string.replace("i", "1")
    string = string.replace("e", "3")
    string = string.replace("s", "5")
    string = string.replace("o", "0")

    return string

if __name__ == "__main__":
    print(substituir_caracteres("Que tal fazer um DDoS?"))  # qu3 t4l f4z3r um dd05?
    print(substituir_caracteres("Obaa! Aprendi SQL INJECTION!"))  # 0b44! 4pr3nd1 5ql 1nj3ct10n!
    print(substituir_caracteres("Instalei mais de 500 malwares nas vítimas!"))  # 1n5t4l31 m415 d3 500 m4lw4r35 n45 vít1m45!
