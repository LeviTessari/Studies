#meu jeito
import random, time
print('\033[35m<=>\033[m'*10+' \033[34mJO KEM PÔ\033[m '+'\033[35m<=>\033[m'*10)
print('''Vamos jogar JOKEMPÔ!
Quero só ver você conseguir ganhar!
Escolha um deles e perca:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
n = int(input('Qual deles você vai escolher para me desafiar? '))
n1 = random.randint(0, 2)
print('\033[31mJO\033[m')
time.sleep(1)
print('\033[32mKEM\033[m')
time.sleep(1)
print('\033[33mPô\033[m')
time.sleep(1)
print('\033[36m#=\033[m'*30)

if n == n1:
    if n == 0:
        vencedor = 'PEDRA'
    elif n == 1:
        vencedor = 'PAPEL'
    elif n == 2:
        vencedor = 'TESOURA'
    print('\033[33mEMPATOUU\033[33m! Escolhemos {} juntos!!'.format(vencedor))
elif n > n1 and n != n1 and n != 0 and n1 != 0 and n < 3:
    vencedor = 'TESOURA'
    perdedor = 'PAPEL'
    print('Você me \033[34mvenceu\033[m! Escolhi {} e você {}. '.format(perdedor, vencedor))
elif n1 > n and  n != n1 and n != 0 and n1 != 0 and n1 < 3:
    vencedor = 'TESOURA'
    perdedor = 'PAPEL'
    print('Eu \033[32mGANHEI\033[m! Escolhi {} e você {}. '.format(vencedor, perdedor))
elif n > n1 and n != n1 and n != 1 and n1 != 1 and n < 3:
    vencedor = 'PEDRA'
    perdedor = 'TESOURA'
    print('Eu \033[32mGANHEI\033[m! Escolhi {} e você {}. '.format(vencedor, perdedor))
elif n1 > n and n != n1 and n != 1 and n1 != 1 and n1 < 3:
    vencedor = 'PEDRA'
    perdedor = 'TESOURA'
    print('Você me \033[34mvenceu\033[m! Escolhi {} e você {}. '.format(perdedor, vencedor))
elif n > n1 and n != n1 and n != 2 and n1 != 2 and n < 3:
    vencedor = 'PAPEL'
    perdedor = 'PEDRA'
    print('Você me \033[35mvenceu\033[m! Escolhi {} e você {}. '.format(perdedor, vencedor))
elif n1 > n and n != n1 and n != 2 and n1 != 2 and n1 < 3:
    vencedor = 'PAPEL'
    perdedor = 'PEDRA'
    print('Eu \033[32mGANHEI\033[m! Escolhi {} e você {}. '.format(vencedor, perdedor))
else:
    print('\033[31mVOCÊ \033[32mESTÁ \033[33mQUERENDO \033[34mME \033[35mENGANAR!')
print('\033[36m#=\033[m'*30)

#professor
itens = ( 'Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('''Vamos jogar JOKEMPÔ!
Quero só ver você conseguir ganhar!
Escolha um deles e perca:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual deles você vai escolher para me desafiar? '))
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))

if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print(' EMPATE ')
    elif jogador == 1:
        print(' JOGADOR VENCE ')
    elif jogador == 2:
        print(' COMPUTADOR VENCE ')
    else:
        print(' JOGADA INVALIDA ')
if computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print(' COMPUTADOR VENCE ')
    elif jogador == 1:
        print(' EMPATE ')
    elif jogador == 2:
        print(' JOGADOR VENCE ')
    else:
        print(' JOGADA INVALIDA ')
if computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print(' JOGADOR VENCE ')
    elif jogador == 1:
        print(' COMPUTADOR VENCE ')
    elif jogador == 2:
        print(' EMPATE ')
    else:
        print(' JOGADA INVALIDA ')
