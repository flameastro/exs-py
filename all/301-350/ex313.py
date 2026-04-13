# ex313: Uma empresa concederá um reajuste salarial de 8,75% no próximo mês. Sua missão é elaborar um algoritmo que, a partir de dados inseridos pelo usuário, calcule o salário reajustado de um funcionário, exibindo, como resultado, seu nome, o valor de seu salário atual e o valor do salário reajustado.
salario = float(input("Insira o salário R$: "))
porcentagem_reajuste = 8.75

novo_salario = salario + (salario * (porcentagem_reajuste / 100))
print(f"O novo salário do funcionário é R${novo_salario}")
