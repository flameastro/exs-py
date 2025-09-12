# ex107: Faça um programa que verifique se uma letra digitada é vogal ou consoante.
def verifica_vogal_consoante(letra: str):
    vogais = ['a', 'á', 'à', 'ã', 'â', 'e', 'é', 'è', 'ê', 'í', 'ì', 'î', 'i', 'o', 'ó', 'ò', 'ô', 'õ', 'ú', 'ù', 'û', 'u']

    try:
        if not letra.isalpha() or len(letra) != 1:
            return 'Por favor, digite uma letra válida'
    except AttributeError as attr_e:
        return f"A função aceita apenas letras. Erro: {attr_e}"
    except Exception as e:
        return f"Erro: {e}"

    if letra.lower() in vogais:
        return f'vogal'

    return f'consoante'


if __name__ == "__main__":
    print(verifica_vogal_consoante("a"))  # vogal
    print(verifica_vogal_consoante(6))  # A função aceita apenas letras. Erro: 'int' object has no attribute 'isalpha'
    print(verifica_vogal_consoante(""))  # Por favor, digite uma letra válida
    print(verifica_vogal_consoante("ABC"))  # Por favor, digite uma letra válida
    print(verifica_vogal_consoante("é"))  # vogal
    print(verifica_vogal_consoante("w"))  # consoante
