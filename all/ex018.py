# ex018: Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).
x = float(input("Qual a posição de x? "))
y = float(input("Qual a posição de y? "))

if x > 0 and y > 0:
    print('Q1')
elif x > 0 and y < 0:
    print('Q4')
elif x < 0 and y < 0:
    print('Q3')
elif x < 0 and y > 0:
    print('Q2')
else:
    print('Origem')
