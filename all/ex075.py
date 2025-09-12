# ex075: Simule um caixa eletrônico, onde o usuário tem apenas 3 tentativas para digitar a senha correta. (senha="admin")
def caixa_eletronico():
    tentativas = 3

    while tentativas >= 1:
        senha = input("Olá, digite a sua senha:\n>>> ")

        if senha == "admin":
            print("Senha correta. Bem-vindo(a)!")
            tentativas = 0
        else:
            tentativas -= 1
            if tentativas != 0:
                print(f"Senha incorreta. Tentativas restantes: {tentativas}")
            else:
                print("Você excedeu o número máximo de tentativas. Tente novamente mais tarde.")


if __name__ == "__main__":
    caixa_eletronico()
