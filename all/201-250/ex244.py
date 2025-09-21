# ex244: Verificar Idade para Categoria: Peça a idade e classifique em: Criança (0-12), Adolescente (13-17), Adulto (18-59), Idoso (60+).
idade = int(input("Digite a sua idade: "))

if idade >= 0 and idade <= 12:
    print("Criança")
elif idade > 12 and idade <= 17:
    print("Adolescente")
elif idade >= 18 and idade < 59:
    print("Adulto")
elif idade >= 60 and idade <= 100:
    print("Idoso")
else:
    print("Idade inválida.")
