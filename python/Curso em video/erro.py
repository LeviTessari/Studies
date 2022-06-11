import math

angulo = math.radians(40)
M = 59.002
m = 73.295
mi = (M/(m*math.cos(angulo))) - math.tan(angulo)
print(mi)

a = 0.001/200
b = 0.001/135
c = 0.001/45

E = (a*a + b*b)**(1/2)
erro = E * mi
print(erro)

