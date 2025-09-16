# ex129: Compactador RLE (Run-Length Encoding: "AAABBBCC" → "A3B3C2").

def compactador_RLE(string: str):
    if len(string) < 0:
        return "A frase deve ter mais de um caractere."

    if not string.isalpha():
        return "A frase deve conter somente letras do alfabeto, sem espaços."

    caracteres = []
    RLE = ""

    for letra in string:
        if letra not in caracteres:
            caracteres.append(letra)
            RLE += f"{letra}{string.count(letra)}"

    return f"Resultado do RLE: {RLE}"


print(compactador_RLE("compactadorRLE"))  # c2o2m1p1a2t1d1r1R1L1E1
print(compactador_RLE("Pyyyyyyyyyyyyython"))  # Resultado do RLE: P1y13t1h1o1n1
print(compactador_RLE("aaaaaaa"))  # Resultado do RLE: a7
