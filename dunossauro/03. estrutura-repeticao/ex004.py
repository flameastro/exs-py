# ex004: Supondo que a população de um país A seja da ordem de 80_000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja 200_000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
paisA = {
    "habitantes": 80000,
    "taxa de crescimento": 0.03
}

paisB = {
    "habitantes": 200000,
    "taxa de crescimento": 0.015
}

anos = 0
while paisA["habitantes"] < paisB["habitantes"]:
    paisA["habitantes"] += paisA["habitantes"] * paisA["taxa de crescimento"]
    paisB["habitantes"] += paisB["habitantes"] * paisB["taxa de crescimento"]

    anos += 1

print(f"Em {anos} anos, o País A terá {paisA['habitantes']:.0f} habitantes e o País B terá {paisB['habitantes']:.0f}.")
