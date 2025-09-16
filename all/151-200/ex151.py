# ex151: Crie uma função que cria senhas criptografadas (letras randômicas)
import random

def criptografar_senha(tamanho: int):
    if tamanho > 82 or tamanho < 8:
        return "Tamanho inválido. O tamanho deve ser entre 8 e 82 caracteres"

    criptografia = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()%-_=+-&*?"
    senha = "".join(random.sample(criptografia, tamanho))

    return senha

try:
    tamanho = int(input("Digite o tamanho da senha (8-82):\n>>> "))
    quantidade = int(input("Digite a quantidade de senhas a gerar (1 a 100):\n>>> "))

    if quantidade < 1 or quantidade > 100:
        print("A quantidade de senhas deve ser entre 1 a 100.")
    else:
        for i in range(quantidade):
            print(criptografar_senha(tamanho))

except Exception as e:
    print(f"Erro: {e}")
