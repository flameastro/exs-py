# ex011: As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes. Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.
salario = float(input("Digite o valor do seu salário: "))

if salario <= 280:
    aumento = salario * 0.20
    percentual = 20
elif salario > 280 and salario <= 700:
    aumento = salario * 0.15
    percentual = 15
elif salario > 700 and salario <= 1500:
    aumento = salario * 0.10
    percentual = 10
elif salario > 1500:
    aumento = salario * 0.05
    percentual = 5

print(" Detalhes ".center(25, "-"))
print(f"O salário antes do aumento era de R${salario}")
print(f"O percentual do aumento aplicado sobre o salário foi de {percentual}%")
print(f"O valor do aumento foi de R${aumento}")
print(f"O novo salário com o aumento é de R${salario + aumento}")
