# ex002: Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
usuario = input("Crie um nome de usuário: ").strip()
senha = input("Crie uma senha: ").strip()

if usuario == "admin" and senha == "admin":
    print("Uau, que belo nome e senha para serem invadidos!")

while usuario == senha:
    print("Ooops, certifique-se de inserir uma senha diferente do seu nome de usuário!")
    usuario = input("Crie um nome de usuário: ").strip()
    senha = input("Crie uma senha: ").strip()
