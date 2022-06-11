import datetime
ano = int(input('Ano de nascimento: '))
anoatual = datetime.date.today().year
idade = anoatual-ano
alistamento = ano + 18
tempo = alistamento - anoatual
print('Quem nasceu em {} possui {} anos atualmente e deverá se alistar em {} !'.format(ano, idade, alistamento))
if idade < 18:
    print('Você ainda não possui idade para se alistar e deverá se alistar em {} anos.'.format(tempo))
elif idade > 18:
    print('Vocês já deveria ter se alistado faz {} anos.'.format(anoatual-alistamento))
else:
    print('Você deve se alistar neste ano!')
