#meu jeito
import datetime
import time
ano = int(input('Digite o ano e falaremos se é bissexto, se quer saber ano atual digite 0: '))

if ano == 0:
    ano = int(time.strftime("%Y", time.gmtime()))
    conf = ano % 4 and ano % 100 != 0 or ano % 400 == 0
    if conf == 0:
        print('O ano atual, {} é bissexto!'.format(time.strftime("%Y", time.gmtime())))
    else:
        print('O ano atual, {} não é bissexto!'.format(time.strftime("%Y", time.gmtime())))
else:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('O ano de {} é um ano bissexto!'.format(ano))
    else:
        print('O ano de {} não é um ano bissexto!'.format(ano))

print('Gostou de saber?')
print('-'*10)
#Professor
print('{}'.format(datetime.date.today().year))