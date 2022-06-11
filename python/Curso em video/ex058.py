from random import randint
cont=1
computador = randint(1, 11)
usuario = int(input('Qual número você acha que estou pensando? '))
while usuario != computador:
    cont += 1
    if usuario > computador:
        print('Menos...')
    else:
        print('Mais...')
    usuario = int(input('Você errou escolhendo número {}. Vou ser bondoso, tente novamente: '.format(usuario)))
print('PARABÉNS!! Eu escolhi número {} e você escolheu o número {}. Estamos iguais, você apenas demorou {} tentativas! :)'.format(computador, usuario, cont))
