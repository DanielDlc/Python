""" Raízes de uma equação de segundo grau """

import math

def delta():
    a = int(input("Digite o valor do coeficiente a: "))
    b = int(input("Digite o valor do coeficiente b: "))
    c = int(input("Digite o valor do coeficiente c: "))
    delta = b*b - 4 * a * c
    xv = -b/(2*a)
    yv = -delta/(4*a)
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = (-1*b + math.sqrt(delta)) / (2 * a)
        print(f'A equação possui apenas uma raíz: {raiz}')
    elif delta > 0:
        raiz_1 = (-1*b - math.sqrt(delta)) / (2 * a)
        raiz_2 = (-1*b + math.sqrt(delta)) / (2 * a)
        print(f'As raízes da equação são: {raiz_1} e: {raiz_2}')
    print(f"O vértice da parábola definida por y = {a}x^2 + {b}x + {c} : ({xv}, {yv})")

delta()
