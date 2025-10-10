# ex271: Considere que um ser humano pode ser classificado segundo sua idade nas seguintes faixas etárias:
# Bebê (nascimento até 3 anos).
# Criança (4 até 7 anos).
# Pré-adolescente (8 até 12 anos).
# Adolescente (13 até 20 anos).
# Jovem (21 a 40 anos).
# Meia-idade (41 até 64 anos).
# Idoso (65 anos em diante).
# Escreva um programa que solicite uma idade e imprima a classificação correspondente.
idade = int(input("Digite a sua idade: "))

if idade <= 3:
    classificacao = "Bebê"
elif idade > 3 and idade <= 7:
    classificacao = "Criança"
elif idade > 7 and idade <= 12:
    classificacao = "Pré-Adolescente"
elif idade > 12 and idade <= 20:
    classificacao = "Adolescente"
elif idade > 20 and idade <= 40:
    classificacao = "Jovem"
elif idade > 40 and idade <= 64:
    classificacao = "Meia-Idade"
elif idade > 64:
    classificacao = "Idoso"

print(f"Sua classificação é: {classificacao}")
