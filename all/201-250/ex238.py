# ex238: Aumento de Salário: Peça o salário de um funcionário e aplique um aumento de 5%, imprimindo o novo salário.
salario = float(input("Digite o seu salário: "))
aumento = salario + (salario * 5) / 100

print(f"Seu salário com aumento de 5% é de R${aumento}")