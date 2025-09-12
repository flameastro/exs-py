# ex128: Crie uma agenda que armazena o nome da pessoa, ID da pessoa, número do telefone, idade. Sua agenda deve possibilitar:
# (1) – inserir um contato
# (2) – Remover um contato
# (3) – buscar um contato pelo Código.

def mostrar():
    print('Cadastrados'.center(50, '-'))
    for elemento in agenda:
        print(elemento)

agenda = []

while True:
    menu = int(input('Digite o menu:\n1: Inserir um contato\n2: Remover um contato\n3: Ver um contato\n4: Sair\n'))
    while menu < 0 or menu > 4:
        menu = int(input('Opção inválida. Digite novamente:\n1: Inserir um contato\n2: Remover um contato\n3: Ver um contato\n4: Sair\n'))

    if menu == 1:
        nome = input('Digite o nome da pessoa: ').strip().title()
        codigo = len(agenda) + 1

        for elemento in agenda:
            while elemento[1] == codigo:
                codigo = int(input('Este código já existe. Digite novamente: '))
        telefone = int(input('Digite o telefone da pessoa: '))
        idade = int(input('Digite a idade da pessoa: '))
        agenda.append([codigo, nome, telefone, idade])

    elif menu == 2:
        mostrar()

        remover = int(input('Digite o código que quer remover: '))
        for elemento in agenda:
            if elemento[0] == remover:
                print(f'Usuário {elemento[1]} com o ID de {elemento[0]} removido com sucesso.')
                agenda.remove(elemento)

    elif menu == 3:
        mostrar()

        buscar = int(input('Digite um contato pelo seu código (ID): '))
        for elemento in agenda:
            if elemento[0] == buscar:
                print(f"O nome da pessoa é {elemento[1]}, possui o ID {elemento[0]}, tem o telefone {elemento[2]} e tem {elemento[3]} anos.")
        else:
            if elemento[0] != buscar:
                print('Não foi possível identificar este usuário.')

    elif menu == 4:
        break
