# ex278: Crie um programa que pergunte ao usuário seu nome, sua idade e seu endereço e imprima as suas informações num formato JSON (ou dicionário)
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
endereco = input("Digite o seu endereço: ")

informacoes = {
    "Nome": nome,
    "Idade": idade,
    "Endrereço": endereco
}

print(informacoes)
