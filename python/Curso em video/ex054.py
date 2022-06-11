from datetime import date
M = 0
m = 0
anoatual = date.today().year
for i in range(1, 8):
    idade = int(input('Em que ano nasceu a {}ª pessoa?: '.format(i)))
    if anoatual - idade >= 21:
        M += 1
    else:
        m += 1
print('Existem {} pessoas maiores de idade e {} pessoas menores de idade.'.format(M, m))
