from math import sqrt, pow, hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

#Não utilizando o mth
h = (ca**2 + co**2)**(1/2)
#utilizando sqrt
hip = sqrt(ca**2 + co**2)
#utilisando sqrt e pow
hi = sqrt(pow(ca, 2)+pow(co, 2))
#utilizando o comando hypot
hipo = hypot(co, ca)


print('A hipotenusa vai medir: {}'.format(h))
print('A hipotenusa vai medir: {}'.format(hip))
print('A hipotenusa vai medir: {}'.format(hi))
print('A hipotenusa vai medir: {}'.format(hipo))