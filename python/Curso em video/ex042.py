import math
from time import sleep
l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

if l2 < l1+l3 and l2 > abs(l1 -l3 ):
    print('É um triângulo!')
    sleep(1)
    if l1 != l2 and l1 != l3 and l2 != l3:
        print('É um triângulo escaleno.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('É um triângulo isósceles.')
    elif l1 == l2 and l1 == l3 and l2 == l3:
        print('É um triângulo equilátero')
else:
    print('Não é possível formar um triangulo.')
