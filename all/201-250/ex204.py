# ex204: Crie uma função que separe vogais e consoantes
def separa_vogais_consoantes(string):
    vogais = [l for l in string.lower() if l in "aáâãàeéêèiíìîoóòôõuúùû"]
    consoantes = [l for l in string.lower() if not l in "aáâãàeéêèiíìîoóòôõuúùû" and l.isalpha()]

    return vogais, consoantes


if __name__ == "__main__":
    print(separa_vogais_consoantes("Python!"))  # (['o'], ['p', 'y', 't', 'h', 'n'])
    print(separa_vogais_consoantes("3JavaScript"))  # (['a', 'a', 'i'], ['j', 'v', 's', 'c', 'r', 'p', 't'])
    print(separa_vogais_consoantes("A matemática é incrível!"))  # (['a', 'a', 'e', 'á', 'i', 'a', 'é', 'i', 'í', 'e'], ['m', 't', 'm', 't', 'c', 'n', 'c', 'r', 'v', 'l'])
