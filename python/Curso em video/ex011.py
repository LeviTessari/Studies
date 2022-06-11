h = float(input('digite a altura da parede: '))
l = float(input('Digite a largura da parede: '))
area = h * l
tinta = area /2

print('Para uma parade de altura {} e largura {}, temos {} m², portanto será necessário {} litros de tinta'.format(h, l, area, tinta))