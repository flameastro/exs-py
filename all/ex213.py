# ex213: Efetuar a leitura de dois valores numéricos inteiros representados pelas variáveis A e B e apresentar o resultado da diferença do maior valor pelo menor valor.
A = float(input("Digite o valor A: "))
B = float(input("Digite o valor B: "))

if A > B:
    print(f"A diferença entre {A} e {B} é de {A - B}")
elif A < B:
    print(f"A diferença entre {B} e {A} é de {B - A}")
else:
    print(f"Ambos são iguais, resultando em 0.")
