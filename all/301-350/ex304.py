# ex304: A cifra de Cesar é um tipo de substituição na qual cada letra do texto é substituída por outra, que se apresenta no alfabeto abaixo dela um número fixo de vezes. Por exemplo, com uma troca de três posicões, ‘A’ seria substituído por ‘D’, ‘B’ se tornaria ‘E’, e assim por diante. Implemente um programa que faça uso desse Código de César entre com uma string e retorne a string codificada. Exemplo:
# String: a ligeira raposa marrom saltou sobre o cachorro cansado
# Nova string: D OLJHLUD UDSRVD PDUURP VDOWRX VREUH R FDFKRUUR FDQVDGR
def cifra_de_cesar(texto, numero):
    alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    texto_criptografado = ""

    for letra in texto.lower():
        if letra not in alfabeto:
            texto_criptografado += letra
            continue

        indice = alfabeto.index(letra)
        # print(indice)
        # print(indice+numero)

        if indice+numero > 24:
            indice = indice - 26
            # print(indice)

        nova_letra = alfabeto[indice+numero]
        texto_criptografado += nova_letra

    return texto_criptografado


if __name__ == "__main__":
    print(cifra_de_cesar("Python", 1))  # qzuipo
    print(cifra_de_cesar("Cifra de Cesar", 1))  # djgsb ef dftbs
    print(cifra_de_cesar("Cifra de Cesar", 26))  # cifra de cesar
    print(cifra_de_cesar("testando", 8))  # bmabivlw
    print(cifra_de_cesar("a ligeira raposa marrom saltou sobre o cachorro cansado", 3))  # d oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr
