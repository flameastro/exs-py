# ex327: Crie um programa para simular a gratificação de um vendedor de uma loja de carros usados. O sistema deve solicitar o salário básico do funcionário e o mês que deseja simular o salário com a gratificação.
# A gratificação corresponde a 30% do salário básico do funcionário nos meses de janeiro até maio. De junho até novembro a gratificação corresponde a 40% do salário básico. Em dezembro, a gratificação equivale a 60% do salário. O sistema deve apresentar a gratificação dentro de uma função que receba o salário por parâmetro.
def calcula_gratificacao(salario):
    if mes in range(1, 6):
        gratificacao = 0.30
    elif mes in range(6, 12):
        gratificacao = 0.40
    elif mes == 12:
        gratificacao = 0.60

    salario = salario + (salario * gratificacao)
    return f"Seu salário com gratificação em {MESES[mes-1]} é: R${salario}"


MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
salario = float(input("Insira o seu salário atual: R$"))

print("Lista de Meses")
print("1 - Janeiro")
print("2 - Fevereiro")
print("3 - Março")
print("4 - Abril")
print("5 - Maio")
print("6 - Junho")
print("7 - Julho")
print("8 - Agosto")
print("9 - Setembro")
print("10 - Outubro")
print("11 - Novembro")
print("12 - Dezembro")

mes = int(input("Digite o mês que deseja simular a gratificação: "))
while mes not in range(1, 13):
    print("Por favor, insira um mês entre 1 a 12, com seus respectivos números")
    mes = int(input("Digite o mês que deseja simular a gratificação: "))

print(calcula_gratificacao(salario))
