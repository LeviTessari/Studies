from random import randint
i = 0
print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
while True:
    m = randint(1, 10)
    n = int(input('Digite um valor: '))
    q = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    valor = m +n
    print('-'*20)
    if valor % 2 == 0 and q == 'P':
        print(f'Você jogou {n} e o Levi {m}. Total de {valor} deu PAR.')
    elif valor % 2 != 0 and q == 'I':
        print(f'Você jogou {n} e o Levi {m}. Total de {valor} deu ÍMPAR.')
    else:
        print('PERDEDOR!! LEO OTARIO NUHUAHAHAHAHAHAH!!! LEVI WIIINNNNSS')
        print('-' * 20)
        break
        # elif valor % 2 == 0 and q == 'I':
        # print('VOCÊ PERDEU')
        # print('-' * 20)
        # break
        # elif valor % 2 != 0 and q == 'P':
        # print('VOCÊ PERDEU')
        # print('-' * 20)
        # break
    print('-' * 20)
    i += 1
print(f'GAME OVER! Você venceu {i} vezes')