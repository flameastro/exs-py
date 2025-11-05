# ex012: Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os caracteres embaralhados. Por exemplo: se a função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
from random import randint
def embaralha_palavra(palavra: str):
    palavra_embaralhada = ""
    numeros = []

    while len(palavra_embaralhada) != len(palavra):
        numero = randint(0, len(palavra)-1)
        while numero in numeros:
            numero = randint(0, len(palavra)-1)

        numeros.append(numero)
        palavra_embaralhada += palavra[numero]

    return palavra_embaralhada

if __name__ == "__main__":
    print(embaralha_palavra("Python"))  # Pnhoyt; Pnhoy; nPohyt; tnyPho
    print(embaralha_palavra("JavaScript"))  # JapvitaSrc; caivrJSpat; SJtcpaivra; rviaapSJct
    print(embaralha_palavra("Albert Einstein"))  # AneibntEltie rs; lsEnn tiAtebier; eAt irsbnentEli; siAlebintr Eten
