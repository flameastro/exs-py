# ex116: Crie uma classe chamada User. Crie dois atributos chamados nome e sobrenome e diversos outros atributos que normalmente são armazenados em um perfil de usuário. Crie um método chamado describe_user() que exiba um resumo das informações do usuário. Crie outro método chamado greet_user que exiba um cumprimento personalizado ao usuário.
class User:
    def __init__(self, ID: int = None, nome: str = None, sobrenome: str = None, idade: int = None, nascimento: str = None):
        self.ID = ID
        self.nome = nome.title()
        self.sobrenome = sobrenome.title()
        self.idade = idade
        self.nascimento = nascimento

    def describe_user(self):
        print(f'ID: {self.ID}, nome: {self.nome}, sobrenome: {self.sobrenome}, idade: {self.idade}, nascimento: {self.nascimento}')
  
    def greet_user(self):
        print(f'Olá, {self.nome} {self.sobrenome}!')

    def login(self):
        senha = input('Digite a sua senha: ')
        tentativas = 1
        while True:
            senha = int(input('Digite corretamente: '))
            if senha == 123456:
                print(f"Olá, {self.nome}. Seja bem-vindo(a).")
                break
            else:
                tentativas += 1
                print(f'Senha incorreta! {tentativas} tentativas já foram feitas.')


pedro = User(4, 'Pedro', 'Feitosa', 16, '23/06/2009')
pedro.describe_user()
pedro.greet_user()
pedro.login()
