from random import randint
from time import sleep
palpites = list()
print('-'*20)
print(f'{"JOGAR NA MEGA SENA":^20}')
print('-'*20)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('-==--==-'+f'SORTEANDO {jogos} JOGOS'+'-==--==-')
sleep(1)
for c in range(0, jogos):
    for i in range(0, 6):
        a = randint(1, 61)
        if a not in palpites:
            palpites.append(a)
    palpites.sort()
    print(f'Jogo {c+1}: {palpites}')
    palpites.clear()
    sleep(1)
print('-==--==-'+'<'+' BOA SORTE! '+'>'+'-==--==-')