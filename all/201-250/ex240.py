# ex240: Verificar Vogal ou Consoante: Peça uma letra e diga se é vogal ou consoante.
def vogal_consoante(letra: str) -> str:
    return ["Vogal" if letra.lower() in ["a", "e", "i", "o", "u"] else "Consoante"][0] if letra.isalpha() else "Digite uma letra."

if __name__ == "__main__":
    print(vogal_consoante("A"))  # Vogal
    print(vogal_consoante("D"))  # Consoante
    print(vogal_consoante("&"))  # Digite uma letra.
