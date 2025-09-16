# ex088: Smith criou uma loja de produtos. Ele tem uma conta especial para ele mesmo, com mais de 100 mil clientes em sua loja. Ele precisa que você crie uma função que retorne uma mensagem agradável se a senha for a de Smith. Caso contrário, retorne uma mensagem de boas-vindas ao Cliente.
def verifica_usuario(usuario, senha):
    if usuario == "admin" and senha == 'admin':
        return 'O Criador entrou!'

    return 'Olá, usuário!'


if __name__ == "__main__":
    print(verifica_usuario("SmithFan", "ILoveSmith"))  # Olá, usuário!
    print(verifica_usuario("admin", "admin"))  # O Criador entrou!
    print(verifica_usuario("Smith", "password"))  # Olá, usuário!
