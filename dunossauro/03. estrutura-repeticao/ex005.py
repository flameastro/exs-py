# ex005: Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
habitantesA = int(input("Digite o total de habitantes do país A: "))
while habitantesA not in range(0, 10**12):
    print(f"Por favor, insira uma quantidade válida.")
    habitantesA = int(input("Digite o total de habitantes do país A: "))

taxa_crescimentoA = float(input("Digite a porcentagem da taxa de crescimento do país A: %"))
while taxa_crescimentoA <= 0:
    print("Certifique-se de inserir um valor adequado.")
    taxa_crescimentoA = float(input("Digite a porcentagem da taxa de crescimento do país A: %"))

habitantesB = int(input("Digite o total de habitantes do país B: "))
while habitantesB not in range(0, 10**12):
    print(f"Por favor, insira uma quantidade válida.")
    habitantesB = int(input("Digite o total de habitantes do país B: "))

taxa_crescimentoB = float(input("Digite a porcentagem da taxa de crescimento do país B: %"))
while taxa_crescimentoB <= 0:
    print("Certifique-se de inserir um valor adequado.")
    taxa_crescimentoB = float(input("Digite a porcentagem da taxa de crescimento do país B: %"))

if taxa_crescimentoB > taxa_crescimentoA:
    print("Ooops, não é possível fazer o cálculo quando a taxa de crescimento do país B é maior que a do país A.")
else:
    anos = 0
    while habitantesA < habitantesB:
        habitantesA += (habitantesA * taxa_crescimentoA) / 100
        habitantesB += (habitantesB * taxa_crescimentoB) / 100

        anos += 1

    print(f"Seram necessários {anos} anos para que o país A ultrapasse do país B em população.")
