# ex270: Uma empresa vai conceder um aumento diferenciado a seus funcionários segundo os seguintes critérios: 
# quem ganha até 1000 reais (inclusive) terá aumento de 20 %;
# entre 1000 e 2000 (inclusive), aumento de 18 %;
# entre 2000 e 4000 (inclusive) aumento de 15 %
# e acima de 4000 aumento de 10 %.
#  Escreva um programa que, dado um valor de salário, calcule o novo valor após o aumento.
salario = float(input("Digite o seu salário: "))

if salario <= 1000:
    salario += (salario * 20) / 100
elif salario > 1000 and salario <= 2000:
    salario += (salario * 18) / 100
elif salario > 2000 and salario <= 4000:
    salario += (salario * 15) / 100
elif salario > 4000:
    salario += (salario * 10) / 100

print(f"Seu salário com o aumento ajustado é de R${salario}.")
