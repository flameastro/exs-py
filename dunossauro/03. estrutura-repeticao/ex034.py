# ex034: Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
numero = int(input("Insira um número inteiro: "))

divisores = [divisivel for divisivel in range(1, (numero // 2) + 1) if numero % divisivel == 0]

if len(divisores) > 1:
    print(f"{numero} não é um número primo (número composto)")
else:
    print(f"{numero} é um número primo.")

