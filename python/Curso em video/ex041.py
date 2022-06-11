from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
id = atual - ano
print('O atléta tem {} anos.'.format(id))

if id <= 9:
    clas = 'MIRIM'
elif 9 < id <= 14:
    clas = 'INFANTIL'
elif 14 < id <= 19:
    clas = 'JÚNIOR'
elif 19 < id <= 25:
    clas = 'SÊNIOR'
else:
    clas = 'MASTER'

print('Classificação: {}'.format(clas))
