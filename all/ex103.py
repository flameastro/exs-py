# ex103: Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem.
def salario_funcionario():
    try:
        funcionario = input('Digite o nome do funcionário: ')
        salario = float(input('Digite o salário do funcionário: '))
    except ValueError as value_e:
        return f"O salário deve ser um número. Erro: {value_e}"
    except Exception as e:
        return f"Ocorreu um erro: {e}"

    return f'O(a) funcionário(a) {funcionario} tem um salário de R${salario}.'


if __name__ == "__main__":
    print(salario_funcionario())
    # if salario_funcionario(salario="e") -> O salário deve ser um número. Erro: could not convert string to float: 'e'
