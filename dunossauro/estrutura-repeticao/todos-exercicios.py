# ex001: Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
nota = int(input("Digite uma nota entre 0 a 10: "))
while nota not in range(0, 11):
    print("Por favor, insira uma nota entre 0 a 10.")
    nota = int(input("Digite uma nota entre 0 a 10: "))

print(f"A nota digitada foi {nota}")


# ex002: Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
usuario = input("Crie um nome de usuário: ").strip()
senha = input("Crie uma senha: ").strip()

if usuario == "admin" and senha == "admin":
    print("Uau, que belo nome e senha para serem invadidos!")

while usuario == senha:
    print("Ooops, certifique-se de inserir uma senha diferente do seu nome de usuário!")
    usuario = input("Crie um nome de usuário: ").strip()
    senha = input("Crie uma senha: ").strip()


# ex003: Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 2 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Estado Civil: 's', 'c', 'v', 'd';
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
salario = float(input("Digite o seu salário: "))
estado_civil = input("Digite o seu estado civil: ").lower().strip()

print("Nome válido" if len(nome) > 2 else "Nome inválido")
print("Idade válida" if idade in range(0, 151) else "Idade inválida")
print("Salário válido" if salario > 0 else "Salário inválido")
print("Estado Civil válido" if estado_civil in ['s', 'c', 'v', 'd'] else "Estado Civil inválido")
