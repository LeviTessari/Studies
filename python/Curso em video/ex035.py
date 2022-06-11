#análisar triangulos
import math
n1= float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
n3 = float(input('Digite o terceiro valor: '))

if n1 < n2 + n3 and n1 > abs(n2-n3):
    print('É possível fazer um triangulo.')
else:
    print('Não é possível fazer um triangulo com estes valores.')