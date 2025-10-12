# ex277: Crie um programa completo que pede ao usuário três notas e retorne a média. Utilize avisos, verificações e repetições.
print("Atenção: Insira \".\" ao invés de \",\".")

try:
    nota1 = float(input("Digite aqui a sua primeira nota (Ex. 7.91): "))
    while nota1 < 0 or nota1 >= 11:
        print("OOps, por favor, digite um valor válido.")
        nota1 = float(input("Digite aqui a sua primeira nota (Ex. 7.91): "))

    nota2 = float(input("Digite aqui a sua segunda nota (Ex. 9.45): "))
    while nota2 < 0 or nota2 >= 11:
        print("OOps, por favor, digite um valor válido.")
        nota2 = float(input("Digite aqui a sua segunda nota (Ex. 9.45): "))

    nota3 = float(input("Digite aqui a sua terceira nota (Ex. 7): "))
    while nota3 < 0 or nota3 >= 11:
        print("OOps, por favor, digite um valor válido.")
        nota3 = float(input("Digite aqui a sua terceira nota (Ex. 7): "))

    media = (nota1 + nota2 + nota3) / 3
    print(f"A sua média é {round(media, 2)}.")
except KeyboardInterrupt as keyInterrupt:
    print(f"Você interrompeu o programa: {keyInterrupt}")
except ValueError as value_error:
    print(f"Você digitou um valor diferente do esperado. Por favor, certifique-se de que escreveu corretamente.")
except Exception as e:
    print(f"Algum erro indesejado ocorreu. Por favor, entre em contato com o administrador em https://github.com/flameastro")
